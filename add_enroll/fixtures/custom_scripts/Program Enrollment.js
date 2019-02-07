frappe.ui.form.on("Program Enrollment", {
	sinvoice: function(frm)
	{
		if( frm.doc.sinvoice == 0)
		{
		frm.set_value("invoice" , undefined);
		frm.set_value("_party" , undefined);
		frm.set_df_property("invoice", "hidden", 1);
		frm.set_df_property("invoice", "reqd", 0);
		frm.set_df_property("_party", "hidden", 1);
		frm.set_df_property("_party", "reqd", 0);
		frm.set_df_property("generate", "hidden", 1);
		}

		else{
		frm.set_df_property("invoice", "hidden", 0);
		frm.set_df_property("invoice", "reqd", 1);
		frm.set_df_property("_party", "hidden", 0);
		frm.set_df_property("_party", "reqd", 1);
		}
	}

	invoice: function(frm) {	
	if(frm.doc.invoice != undefined){	
		frm.set_df_property("generate", "hidden", 1);
		}

	else frm.set_df_property("generate", "hidden", 0);
	}


  	_party: function(frm) {	
		frm.set_value("invoice" , undefined);
		frm.set_df_property("generate", "hidden", 0);
		}

  	
  	generate: function(frm) {

  		if(frm.doc.sinvoice == 0) return;
  		if(frm.doc.courses == undefined || frm.doc.student == undefined || frm.doc._party == undefined)
  			{
  				frappe.msgprint("Form incomplete. Kindly fill the mandatory fields and try again."); return;
  			}
  		var crs = [], fee = [], i = 0;
		frm.doc.courses.forEach(function(rows){ crs[i] = rows.course; i++; });
		i = 0;frm.doc.fees.forEach(function(rows){ fee[i] = rows.fee_structure; i++; });
  		frappe.call({
            method: "add_enroll.add_enroll.program_enrollment.make_inv",
            args:{
                    'customer': frm.doc._party,
                    'customer_name': frm.doc.student_name,
                    'due_date': frm.doc.enrollment_date,
                    'courses': crs,
                    'fees':fee,
                   },
            async: false,
            callback: function(r)
            {
            	frm.set_value("invoice",r.message.name);
            	frm.set_df_property("generate", "hidden", 1); 
            }
        });
	}
});