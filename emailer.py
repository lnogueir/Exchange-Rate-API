from EmailAccount import Account
import smtplib
from smtplib import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



class Emailer:
	connected=False
	connection=None
	def __init__(self):
		self.emailer=Account()
		self.content=None

	def connect(self):
		if not Emailer.connected:
			try:
				connection = smtplib.SMTP('smtp.gmail.com',587)
				connection.ehlo()
				connection.starttls()
				connection.login(self.emailer.user,self.emailer.password)
			except SMTPResponseException as e:
				error_code=e.smtp_code
				error_message=e.smtp_error
				print('ERROR CONNECTING:'+str(error_message))
			else:
				Emailer.connected=True
				Emailer.connection = connection

	@classmethod
	def disconnect(cls):
		if cls.connected:
			cls.connection.close()
			cls.connected=False

	def make_email(self, rate):
		try:
			if not Emailer.connected:
				self.connect()
			msg = MIMEMultipart()
			msg["From"] = self.emailer.user
			msg["To"] = self.emailer.receiver
			msg["Subject"] = "Your Subject"
			body = "Your body on the email"
			msg.attach(MIMEText(body,'plain'))
			self.content = msg.as_string()
		except:
			self.disconnect()		



	def send_email(self):
		if Emailer.connected:    
			try:
				Emailer.connection.sendmail(self.emailer.user,self.emailer.receiver,self.content)
			except SMTPRecipientsRefused as e:
				refused = e.recipients
				print("ERROR: "+str(e.recipients))
			else:
				print("EMAIL SENT SUCCESSFULLY")






	    
