import re
from datetime import date, datetime

class PaymentInfo(object):
    def __init__(self, number='', name='', expiration='', cvv='', amount=''):
        self.number = str(number).strip()
        self.name = str(name).strip()
        self.expiration = str(expiration).strip()
        self.cvv = str(cvv).strip()
        self.amount = float(amount)

    def __repr__(self):
        return "Credit Card with last four #{}".format(self.number[-4:])

    def validate(self):
        date_is_valid = self.validate_date() 
        amount_is_valid = self.validate_amount()
        card_is_valid = self.validate_card()

        if date_is_valid and amount_is_valid and card_is_valid:
            return True

    def validate_date(self):
        today = date.today()
        d1 = today.strftime("%y/%m")
        expiration = datetime.strptime(self.expiration, "%m/%y").date()
        d2 = expiration.strftime("%y/%m")

        if d1 < d2: #true if card is not expired
            return True

    def validate_amount(self):
        if self.amount > 0:
            return True

    def validate_card(self):
        if len(self.cvv) == 0 or self.cvv == '':
            self.cvv = '000'

        if self.number and self.name and self.expiration and self.cvv:
            if re.match(r'^[0-9]{16}$', self.number): #checks if card number is 16 digits
                if re.match(r'^[0-9]{3}$', self.cvv): #checks if cvv is 3 digits
                    return True
    
    def process_payment(self):
        is_valid = self.validate()
        gateway = self.get_gateway()

        return gateway

    def get_gateway(self):
        amount = self.amount
        is_online1 = True #simulate if payment gateway is online
        is_online2 = True

        if amount <= 20 and is_online1:
            return 'CheapPaymentGateway'
        elif amount <= 500 and amount >= 21:
            if is_online1 == True:
                return 'ExpensivePaymentGateway'
            elif is_online2 == True:
                return 'CheapPaymentGateway'
        elif amount > 500:
            if is_online1 == True:
                return 'PremiumPaymentGateway'
            elif is_online1 != True:
                count = 0
                for count in range (2): # 2 more tries
                    if is_online1 == True:
                        return 'PremiumPaymentGateway'

            
