import smtplib, ssl
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template
from flask import render_template
import sys
sys.path.insert(1, 'D:/Python projects/StockMonitor')
import Templates.Email_template

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
        message = MIMEMultipart("alternative")
        message["Subject"] = "Stock(s) has risen significantly!"
        message["From"] = sender_email
        message["To"] = recipient_email
        text = """\
            ei tätä
            """
        html = Templates.Email_template.email_template_html
        t1 = Template(html)
        html_msg = t1.render(stocks=self.stock_dict)

        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html_msg, 'html')

        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, message.as_string())
