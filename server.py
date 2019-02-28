# -*- coding: utf-8 -*-

import os

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

port = int(os.environ.get("PORT", 5000))

mock_credit_lock_contracts = [
  {
    "id": 1,
    "status": "pendingApproval",
    "company": "Stone",
    "financialInstitutionControlNumber": "12fds651ds",
    "financialInstitution": {
      "id": 1,
      "numberCode": "123",
      "ispb": "12345678",
      "name": "Itaú"
    },
    "merchantDocument": {
      "number": "11111111111111",
      "type": "cnpjRoot"
    },
    "bankAccount": {
      "branch": "1234",
      "accountNumber": "123456",
      "accountVerificationNumber": "1"
    },
    "retentionAmountsPerArrangement": [
      {
        "financialArrangement": "Visa",
        "currentMaximumDailyRetentionAmount": 10.02,
        "retentionAmountPerPeriod": [
          {
            "maximumDailyRetentionAmount": 11.00,
            "validFrom": "2018-02-20",
            "validTo": "2019-02-20"
          }
        ]
      }
    ],
    "validFrom": "2018-02-20",
    "validTo": "2019-02-20",
    "warrantyType": "None"
  }
]

mock_banks_response = [
  {
    "BankAccount": {
      "Id": 123,
      "AccountNumber": "01743",
      "AccountNumberVerificationCode": "1",
      "AffiliationCode": "string",
      "AgencyNumber": "8873",
      "AgencyNumberVerificationCode": None,
      "BankId": 0,
      "BankName": "string",
      "CentralizedPayment": True,
      "StatusId": 0,
      "TypeId": 1,
      "TypeName": "Conta Corrente"
    },
    "Mappings": [
      {
        "WalletTypeId": 2,
        "Locked": True
      },
      {
        "WalletTypeId": 3,
        "Locked": False
      }
    ]
  },
  {
    "BankAccount": {
      "Id": 321,
      "AccountNumber": "01743",
      "AccountNumberVerificationCode": "1",
      "AffiliationCode": "string",
      "AgencyNumber": "8873",
      "AgencyNumberVerificationCode": None,
      "BankId": 0,
      "BankName": "string",
      "CentralizedPayment": True,
      "StatusId": 0,
      "TypeId": 1,
      "TypeName": "Conta Corrente"
    },
    "Mappings": [
      {
        "WalletTypeId": 5,
        "Locked": False
      }
    ]
  }
]

mock_financial_institutions = [
    {
        "id": 1,
        "name": "Itaú",
        "documentNumber": "11.111.111/1111-11",
        "ispb": "12345678",
        "numberCode": "123"
    }
]

@app.route('/hello')
def hello():
    if not request.headers.get("cool_token"):
        return jsonify({
            "message": "You need to send me a cool token!"
        }), 401

    return jsonify({"message": "I'm cool and all"})


@app.route('/echo', methods=["POST"])
def post_stuff():
    if not request.headers.get("cool_token"):
        return jsonify({
            "message": "You need to send me a cool token!"
        }), 401

    return jsonify({"echo": request.data})

@app.route('/api/v1/acquirers/<acquirerKey>/merchants/<affiliationCode>/configuration/bank-accounts', methods=["GET"])
def mock_banks(acquirerKey, affiliationCode):
    return jsonify(mock_banks_response)

@app.route('/credit-lock-contracts', methods=["GET"])
def credit_lock_contracts():
    return jsonify(mock_credit_lock_contracts)

@app.route('/financial-institutions', methods=["GET"])
def financial_institutions():
    return jsonify(mock_financial_institutions)


app.run(host='0.0.0.0', threaded=True, port=port)
