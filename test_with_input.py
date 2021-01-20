from exercise1 import payment

print('***TESTING***\n')
print('please input 16 Digit Credit Card. No spaces.')
ccn = input()
print('please input name of the card holder.')
ch= input()
print('please input expirdation date. ex. 12/25')
ed = input()
print('please input your 3 digit security code. (optional) leave blank if N/A ')
sc = input()
print('please input amount to pay.')
a = input()
a = float(a)

test = payment.PaymentInfo(ccn, ch ,ed ,sc ,a)
is_valid = test.validate()
print(f'Test info \n {ccn} \n {ch} \n {ed} \n {sc} \n {a} \n {test}')
print('Checking card validity....')

if is_valid:
    response = test.process_payment()
    if response:
        print(f'Payment is Processed by {response}', 200)
    else:
        print('Payment services are down. Please try again later', 504)
else:
    print('The request is invalid', 400)