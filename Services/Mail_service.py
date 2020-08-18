import smtplib, ssl


class Mail_service:

    def __init__(self, stock_dict, sender_email, password, recipient_email, smtp_server, port):
        self.stock_dict = stock_dict
        self.sender_email = sender_email
        self.password = password
        self.recipient_email = recipient_email
        self.smtp_server = smtp_server
        self.port = port

    def send_email(self):
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(self.smtp_server, self.port, context=context) as server:
            server.login(self.sender_email, self.password)
            message = """
            Subject: Stock(s) has risen significantly

            {stock_name} has risen over 50% from purchase price.
            Current price: {stock_price} €"""

            server.sendmail(self.sender_email, self.recipient_email, message.format(stock_name=stock_name, stock_price=stock_price))
