from flask import Flask, render_template, request
import hmac
import hashlib
import requests
import json
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def payment():
   if request.method == 'POST':
       data = request.get_json()

       def send_payment_request(userData):
           payload = {
               'amount': userData['amount'],
               'account': userData['accountNumber'],
               'expirationDate': userData['expirationDate'],
               'capture': True,
               'cvv2': userData['cvv2'],
               'transaction': random.randint(100, 1000),
               'batchID': random.randint(100, 1000),
               'industryType': 'E',
               'cardEntryMethod': 'X'
           }

           concat_payload = '/sale' + json.dumps(payload)

           # generate the ePISignature following the instructions in the "How To Authenticate" section of the Custom Pay API Integration Guide

           headers={
               'Content-Type': 'application/json',
               'EPI-Id': <your-epi-id>,
               'EPI-Signature': epi_signature
           }

           response = requests.post('https://epi.epxuap.com/sale', data=json.dumps(payload), headers=headers)

           return response.json()
      
       payment_result = send_payment_request(data)

       payment_result_json = json.dumps(payment_result['data']['text'])
  
       return payment_result_json
   else:
       return render_template('index.html')

if __name__ == '__main__':
   app.run()
