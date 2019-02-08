# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import msgprint, _
from frappe.model.document import Document
from frappe.desk.reportview import get_match_cond, get_filters_cond
from erpnext.education.doctype.program_enrollment.program_enrollment import ProgramEnrollment
from frappe.utils import comma_and
from frappe import utils
import json
	

@frappe.whitelist()
def make_inv(customer, customer_name, due_date, courses, fees):
	count = 0        
	#courses and fees are lists that have the docnames from the front end
	courses = json.loads(courses)
	fees = json.loads(fees)
        udoc = frappe.new_doc("Sales Invoice")
        udoc.naming_series = "ACC-SINV-.YYYY.-"
        udoc.customer = customer
        udoc.customer_name = customer_name
	#Fees
	if(fees):
		for d in fees:
			#fetch fee_structure, it has the amount for the sales invoice, as well as..
			fee_structure = frappe.get_doc("Fee Structure", d)
			for e in fee_structure.components:
				fee_amount = e.amount
				#The fee category. This is have a new field for 
				#"Items" doctype, which will make sure each
				#course correlates to a proper item for identification
				fetched_item = frappe.get_doc("Fee Category", e.fees_category)
				if(fetched_item.item):
					udoc.append('items', {
					'item_code': fetched_item.item,
					'qty': '1',
					'rate': fee_amount,
					'amount': fee_amount,
					})
				count = count + 1
				#Only for checking if the sales invoice will turn out empty
				#In case none of the fee category or the Course doctypes
				#Have any items listed
	#For course
	if(courses):
		for i in range(len(courses)):	
			fdata = frappe.get_doc('Course', courses[i])		
			if(fdata.item):
				count= count + 1			
				udoc.append('items', {
				'item_code': fdata.item,
				'qty': '1',
				})
	udoc.posting_date = frappe.utils.nowdate()
	#Due date  = enrollment date	
	udoc.due_date = due_date
	#saves only if there is at least one potential tx
	if( count > 0 ):	
		udoc.save()
		return frappe.get_last_doc("Sales Invoice");	
	else:
		msgprint(_("Invoice couldn't be generated : None of your courses or fee structures have an item group assigned."))
		return			



def suppress(self):
	self.update_student_joining_date()
	if not self.invoice:
		self.make_fee_records()


def submit_override(doc, method):
	#msgprint(_("Overridden!"))	
	ProgramEnrollment.on_submit = suppress
