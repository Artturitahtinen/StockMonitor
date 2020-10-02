import smtplib, ssl
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template
import sys
sys.path.insert(1, 'D:/Python projects/StockMonitor')
import Templates.Email_template
import Services.Logging_service as Logging_service

config= configparser.ConfigParser()
config.read(r'D:/Python projects/StockMonitor/Configs/config.ini')

sender_email = config['MAIL']['sender_email']
password = config['MAIL']['password']
recipient_email = config['MAIL']['recipient_email']
smtp_server = config['MAIL']['smtp_server']
port = config['MAIL']['port']


class Mail_service:

    def __init__(self, stock_dict):
        self.stock_dict = stock_dict

    def send_email(self):
        Logging_service.logging.info('Trying to send email')
        message = MIMEMultipart("alternative")
        message["Subject"] = "Stock(s) has risen significantly!"
        message["From"] = sender_email
        message["To"] = recipient_email
        text = """\
            plain text alternative email message content
            """
        html = Templates.Email_template.email_template_html
        t1 = Template(html)
        html_msg = t1.render(stocks=self.stock_dict)

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html_msg, 'html')

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()

        Logging_service.logging.info('Mail template ready')

        try:
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                Logging_service.logging.info('Attempting login')
                server.login(sender_email, password)
                Logging_service.logging.info('Login to monitoringOmx successful')
                server.sendmail(sender_email, recipient_email, message.as_string())
                Logging_service.logging.info('Mail sent successfully')
        except Exception as e:
            Logging_service.logging.exception('Error happened: ' + e)
