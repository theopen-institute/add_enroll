# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "add_enroll"
app_title = "Program Enrollment v2"
app_publisher = "Nobel Dahal"
app_description = "Augments Program Enrollment"
app_icon = "icon-paper-clip"
app_color = "black"
app_email = "iamtribulation@outlook.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/add_enroll/css/add_enroll.css"
# app_include_js = "/assets/add_enroll/js/add_enroll.js"

# include js, css files in header of web template
# web_include_css = "/assets/add_enroll/css/add_enroll.css"
# web_include_js = "/assets/add_enroll/js/add_enroll.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "add_enroll.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "add_enroll.install.before_install"
# after_install = "add_enroll.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "add_enroll.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

doc_events = {
 	"Program Enrollment": {
 		"before_submit": "add_enroll.add_enroll.program_enrollment_override.submit_override"
	}
 }



# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"add_enroll.tasks.all"
# 	],
# 	"daily": [
# 		"add_enroll.tasks.daily"
# 	],
# 	"hourly": [
# 		"add_enroll.tasks.hourly"
# 	],
# 	"weekly": [
# 		"add_enroll.tasks.weekly"
# 	]
# 	"monthly": [
# 		"add_enroll.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "add_enroll.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "add_enroll.event.get_events"
# }

#Fixtures, the heart and soul of this app
#----------------------------------------
fixtures = ["Custom Field","Custom Script"]

###################################################################
# NOTE: COMMENT OUT FIXTURE AND DELETE CUSTOM FIELD JSON AFtER DONE
###################################################################