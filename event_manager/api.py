import frappe

 
def sendEmail(email_address,subject):
	frappe.sendmail(recipients = 'alskryasamt5@gmail.com',
		subject="Subject of the email",
		message= "Content of the email")