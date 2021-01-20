from flask import Flask, request, jsonify
import payment

app = Flask(__name__)

@app.route('/')
def ProcessPayment():
    if request.args:       
        CreditCardNumber = request.args['ccn']
        CardHolder = request.args['ch']
        ExpirationDate = request.args['ed']
        SecurityCode = request.args.get('sc') #optional
        Amount = request.args['a']
        test = payment.PaymentInfo(CreditCardNumber,CardHolder, ExpirationDate, SecurityCode, Amount)
        # /?ccn=4100123427233234&ch=John Doe&ed=11/22&sc=223&a=688.22 #testing URI queries
    else: #RUN THIS IF NO URL QUERIES
        test = payment.PaymentInfo('4100123427233234','John Doe', '02/25', '777', 69.22) 

    is_valid = test.validate()
    if is_valid:
        response = test.process_payment()
        if response:
            return f'Payment is Processed by {response}', 200
        else:
            return 'Payment services are down. Please try again later', 500
    else:
        return 'The request is invalid', 400

if __name__ == "__main__":
    app.run(debug=True)