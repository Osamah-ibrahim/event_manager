import frappe

def sendEmail(email_address,self):
    frappe.sendmail(recipients = "alskryasamt5@gmail.com",
		subject="Event Invitation",
		message= "Content of the email")