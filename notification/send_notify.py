import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Email(object):

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.smtp = "smtp.gmail.com"

    def send_email(self, ad_password, ad_uid, ad_user_email):
        server = smtplib.SMTP(self.smtp,587)
        server.ehlo()
        server.starttls()
        server.login(self.email, self.password)
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = ad_user_email
        msg['Subject'] = "OpenLDAP Account Created"
        body = "Password: "+str(ad_password)+"\nUID: "+str(ad_uid)
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(self.email, ad_user_email, text)
