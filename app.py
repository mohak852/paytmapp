from flask import Flask, jsonify
from Checksum import generate_checksum
app = Flask(__name__)

@app.route('/')
def checkout():
    MERCHANT_KEY = 'f8tI!05cG49PjgW6'
    param_dict = {
        'MID': 'fSduEn46698831465981',
        'ORDER_ID': str(868464),
        'TXN_AMOUNT': str(565165),
        'CUST_ID': "abc@abc.com",
        'INDUSTRY_TYPE_ID': 'WEBSTAGING',
        'WEBSITE': 'DEFAULT',
        'CHANNEL_ID': 'WAP',
    }
    param_dict['CHECKSUMHASH'] = generate_checksum(
        param_dict, MERCHANT_KEY)
    print(param_dict['CHECKSUMHASH'])
    return jsonify({'checksum': param_dict['CHECKSUMHASH']})

if __name__ == '__main__':
    app.run(debug=True)
