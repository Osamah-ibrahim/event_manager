# Copyright (c) 2024, E2NEXT and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe import _
import frappe
class Attendee(Document):
 
 def validate(self):
     if frappe.db.sql( f""" select COUNT(*) from tabAttendee; """)  == frappe.db.sql( f""" select * from tabEvents where name ="{self.event}" """):
        frappe.throw("Event exided allowed number")
        
 @frappe.whitelist()
 def frm_call(self,msg):
   import time
   time.sleep(5)
   frappe.msgprint(msg)