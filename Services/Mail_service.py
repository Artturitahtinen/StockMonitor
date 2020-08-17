import smtplib, ssl

class Mail_service:

    port = 465
    password = 

    def __init__(self, stock_dict){
        self.stock_dict = stock_dict
    }