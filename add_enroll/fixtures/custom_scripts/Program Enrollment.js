frappe.ui.form.on("Program Enrollment", {
	sinvoice: function(cur_frm)
	{
		if( cur_frm.doc.sinvoice == 0)
		{
		cur_frm.set_value("invoice" , undefined);
		cur_frm.set_value("party" , undefined);
		cur_frm.set_df_property("invoice", "hidden", 1);
		cur_frm.set_df_property("invoice", "reqd", 0);
		cur_frm.set_df_property("party", "hidden", 1);
		cur_frm.set_df_property("party", "reqd", 0);
		cur_frm.set_df_property("generate", "hidden", 1);
		}

		else{
		cur_frm.set_df_property("invoice", "hidden", 0);
		cur_frm.set_df_property("invoice", "reqd", 1);
		cur_frm.set_df_property("party", "hidden", 0);
		cur_frm.set_df_property("party", "reqd", 1);
		}
	},

	invoice: function(cur_frm) {	
	if(cur_frm.doc.invoice != undefined){	
		cur_frm.set_df_property("generate", "hidden", 1);
		}

	else cur_frm.set_df_property("generate", "hidden", 0);
	},


  	party: function(cur_frm) {	
		cur_frm.set_value("invoice" , undefined);
		cur_frm.set_df_property("generate", "hidden", 0);
		},

  	
  	generate: function(cur_frm) {

  		if(cur_frm.doc.sinvoice == 0) return;
  		if(cur_frm.doc.courses == undefined || cur_frm.doc.student == undefined || cur_frm.doc.party == undefined)
  			{
  				frappe.msgprint("Form incomplete. Kindly fill the mandatory fields and try again."); return;
  			}
  		var crs = [], fee = [], i = 0;
		cur_frm.doc.courses.forEach(function(rows){ crs[i] = rows.course; i++; });
		i = 0;cur_frm.doc.fees.forEach(function(rows){ fee[i] = rows.fee_structure; i++; });
  		frappe.call({
            method: "add_enroll.add_enroll.program_enrollment_override.make_inv",
            args:{
                    'customer': cur_frm.doc.party,
                    'customer_name': cur_frm.doc.student_name,
                    'due_date': cur_frm.doc.enrollment_date,
                    'courses': crs,
                    'fees':fee,
                   },
            async: false,
            callback: function(r)
            {
            	cur_frm.set_value("invoice",r.message.name);
            	cur_frm.set_df_property("generate", "hidden", 1); 
            }
        });
	}
});