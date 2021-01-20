import requests
from exercise1 import payment

ccn = '4100123427233234' #16 digit card number
ch = 'John Doe' #card holder
ed = '11/45' #expiration date
sc = '223' #3 digit security code
# sc = '' #to test blank security code
a = 89.22 #amount

print('***TESTING***\n')
test = payment.PaymentInfo(ccn, ch, ed, sc, a)
print(f'Test info \n {ccn} \n {ch} \n {ed} \n {sc} \n {a} \n {test}')
is_valid = test.validate()

print('Checking card validity....')

if is_valid:
    response = test.process_payment()
    if response:
        print(f'Payment is Processed by {response}', 200)
    else:
        print('Payment services are down. Please try again later', 504)
else:
    print('The request is invalid', 400)

print('\n\n***TESTING REQUESTS***')
response = requests.get("http://127.0.0.1:5000/?ccn=4100123427233234&ch=John Doe&ed=11/22&sc=223&a=688.22")
print(response)