# Copyright (c) 2024, E2NEXT and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe import _
import frappe
class Attendee(Document):
 
 def validate(self):
     self.sql()

 def sql(self):

      attendees = frappe.db.sql(""" select COUNT(*) from tabAttendee where event = '{0}';""".format(self.event)) 

      for a in attendees: 
        attendeesCount = a 

      events = frappe.db.sql(""" select int_tohk from tabEvents where name = '{0}';""".format(self.event))

      for c in events: 
        maximumCount = c 

      if  attendeesCount == maximumCount:
        frappe.throw("Event exided allowed number")
      
 @frappe.whitelist()
 def frm_call(self):
   import time
   time.sleep(1)
   data = frappe.db.sql("""select attendee_name from tabAttendee WHERE event = '{0}';""".format(self.event),as_dict=1)
   for d in data:
       frappe.msgprint(_("{0}").format(d.attendee_name))

 def before_insert(self):
    frappe.sendmail(recipients=[self.email],
                    subject="Event Invitation",
                    message="You've been invited to attend the '{0}' event".format(self.event))