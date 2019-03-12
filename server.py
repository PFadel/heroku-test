# -*- coding: utf-8 -*-

import os

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

port = int(os.environ.get("PORT", 5000))

mock_credit_lock_contracts = [
  {
    "bankAccount": {
      "accountNumber": "123456",
      "accountVerificationNumber": "1",
      "branch": "1234"
    },
    "company": "Stone",
    "financialInstitution": {
      "id": 1,
      "numberCode": "123",
      "ispb": "6847",
      "name": "Banco Itaú S.A."
    },
    "financialInstitutionControlNumber": "12fds651ds",
    "id": 1,
    "merchantDocument": {
      "number": "12345678000101",
      "type": "cnpj"
    },
    "retentionAmountsPerArrangement": [
      {
        "currentMaximumDailyRetentionAmount": 0,
        "financialArrangement": "Master Crédito",
        "retentionAmountPerPeriod": [
          {
            "maximumDailyRetentionAmount": 10.02,
            "validFrom": "2019-02-01",
            "validTo": "2019-02-28"
          },
          {
            "maximumDailyRetentionAmount": 10.04,
            "validFrom": "2019-03-01",
            "validTo": "2019-03-20"
          },
        ],
      },
      {
        "financialArrangement": "Visa Crédito",
        "retentionAmountPerPeriod": [
          {
            "maximumDailyRetentionAmount": 4.08,
            "validFrom": "2019-02-22",
            "validTo": "2019-03-04"
          },
        ],
      },
      {
        "financialArrangement": "Elo Crédito",
        "retentionAmountPerPeriod": [
          {
            "maximumDailyRetentionAmount": 6.72,
            "validFrom": "2019-02-23",
            "validTo": "2019-02-28"
          },
        ],
      },
    ],
    "status": "inEffect",
    "validFrom": "2019-02-01",
    "validTo": "2019-03-20",
    "warrantyType": "None"
  },
  {
    "bankAccount": {
      "accountNumber": "567890",
      "accountVerificationNumber": "8",
      "branch": "3454"
    },
    "company": "Stone",
    "financialInstitution": {
      "id": 1,
      "numberCode": "345",
      "ispb": "01234567",
      "name": "Banco Triângulo"
    },
    "financialInstitutionControlNumber": "4328525037",
    "id": 2,
    "merchantDocument": {
      "number": "12345678000101",
      "type": "cnpj"
    },
    "retentionAmountsPerArrangement": [
      {
        "currentMaximumDailyRetentionAmount": 0,
        "financialArrangement": "Visa Crédito",
        "retentionAmountPerPeriod": [
          {
            "maximumDailyRetentionAmount": 11,
            "validFrom": "2019-02-24",
            "validTo": "2019-02-28"
          },
        ],
      },
    ],
    "status": "ended",
    "validFrom": "2019-02-01",
    "validTo": "2019-02-28",
    "warrantyType": "None"
  },
  {
    "bankAccount": {
      "accountNumber": "567890",
      "accountVerificationNumber": "8",
      "branch": "3454"
    },
    "company": "Stone",
    "financialInstitution": {
      "id": 1,
      "numberCode": "345",
      "ispb": "01234567",
      "name": "Banco Triângulo"
    },
    "financialInstitutionControlNumber": "4328525037",
    "id": 3,
    "merchantDocument": {
      "number": "12345678",
      "type": "cnjpRoot"
    },
    "retentionAmountsPerArrangement": [
      {
        "currentMaximumDailyRetentionAmount": 0,
        "financialArrangement": "Visa Crédito",
        "retentionAmountPerPeriod": [
          {
            "maximumDailyRetentionAmount": 11,
            "validFrom": "2019-02-24",
            "validTo": "2019-02-28"
          }
        ]
      }
    ],
    "status": "inEffect",
    "validFrom": "2019-01-01",
    "validTo": "2019-02-28",
    "warrantyType": "None"
  }
]

mock_bank_accounts = [
  {
    "id": 123,
    "accountNumber": "01743",
    "accountNumberVerificationCode": "1",
    "affiliationCode": "string",
    "branchNumber": "8873",
    "branchNumberVerificationCode": "1",
    "bankNumber": 0,
    "bankName": "string",
    "ISPB": 60872504,
    "centralizedPayment": True,
    "statusId": 2,
    "statusDescription": "Válida",
    "typeId": 1,
    "typeName": "Conta Corrente",
    "holderDocumentIdentifier": "123",
    "holderEntityType": 1,
    "holderName": "oie",
    "associatedWallets": [
      {
        "walletTypeId": 2,
        "isLocked": True
      },
      {
        "walletTypeId": 3,
        "isLocked": False
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

@app.route('/merchant-receivables-files', methods=["POST"])
def merchant_receivables_files():
    if not (request.json.get('documentNumber') and
            request.json.get('financialInstitutionNumberCode')):

        return jsonify({
            "message": "Missing obrigatory fields!"
        }), 400

    return jsonify({"echo": request.json}), 201

@app.route('/api/v1/acquirers/<acquirerKey>/merchants/<affiliationCode>/configuration/bank-accounts', methods=["GET"])
def bank_accounts(acquirerKey, affiliationCode):
    return jsonify(mock_bank_accounts)

@app.route('/credit-lock-contracts', methods=["GET"])
def credit_lock_contracts():
    return jsonify(mock_credit_lock_contracts)

@app.route('/financial-institutions', methods=["GET"])
def financial_institutions():
    return jsonify(mock_financial_institutions)

app.run(host='0.0.0.0', threaded=True, port=port)
