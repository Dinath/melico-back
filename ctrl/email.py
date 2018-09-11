
import smtplib
from config import Config
from email.mime.text import MIMEText

class Email:

    def send(json_email):
        
        msg = MIMEText(json_email['content'])
        
        msg['Subject'] = json_email['subject']
        msg['From'] = json_email['address']
        msg['To'] = Config.EMAIL_ADDRESS_RECEIVE

        s = smtplib.SMTP(Config.EMAIL_SMTP_HOST, Config.EMAIL_SMTP_PORT)
        s.starttls()
        s.login(Config.EMAIL_SMTP_USER, Config.EMAIL_SMTP_PASSWORD)
        s.send_message(msg)
        s.quit()
                