import os

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

port = int(os.environ.get("PORT", 5000))

mock_consolidated_forecast = [
  {
    "Document": "DOC1",
    "FinancialArrangements": [
      {
        "FinancialArrangement": {
          "Id": 1,
          "Description": "foo"
        },
        "Forecast": {
          "TotalAmount": 1000,
          "FreeAmount": 650,
          "RetainableAmount": 350,
          "IsPotentiallyRetainable": False,
          "Affiliations": [
            {
              "AffiliationCode": "123123123",
              "TotalAmount": 700
            },
            {
              "AffiliationCode": "321321321",
              "TotalAmount": 300
            }
          ]
        }
      }
    ]
  },
  {
    "Document": "DOC2",
    "FinancialArrangements": [
      {
        "FinancialArrangement": {
          "Id": 2,
          "Description": "bar"
        },
        "Forecast": {
          "TotalAmount": 5000,
          "FreeAmount": 0,
          "RetainableAmount": 5000,
          "IsPotentiallyRetainable": True,
          "Affiliations": [
            {
              "AffiliationCode": "123123123",
              "TotalAmount": 700
            }
          ]
        }
      }
    ]
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

@app.route('/api/v1/acquirers/<acquirerKey>/merchants/financial-entries/consolidated-forecast', methods=["GET"])
def consolidated_forecast(acquirerKey):
    return jsonify(mock_consolidated_forecast)


app.run(host='0.0.0.0', threaded=True, port=port)
