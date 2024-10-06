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

      attendees = frappe.db.sql(""" select COUNT(*) from tabAttendee; """,as_dict=1) 

      for a in attendees: 
        attendeesCount = a 

      events = frappe.db.sql(""" select int_tohk from tabEvents where name ='{0}';""".format(self.event),as_dict=1)

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