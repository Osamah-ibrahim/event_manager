// Copyright (c) 2024, E2NEXT and contributors
// For license information, please see license.txt

frappe.ui.form.on("Attendee", {
avent_attendees: function(frm) {
    frm.call({
        doc: frm.doc,
        method: 'frm_call' ,
        freeze: true,
        freeze_message: __('calling frm_call Method'),
        callback: function(r) {
            frappe.msgprint(r.message)
        }

    })

},
});
