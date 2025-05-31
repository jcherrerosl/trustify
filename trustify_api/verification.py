import os
import requests

OPEN_GATEWAY_TOKEN = os.getenv("OPEN_GATEWAY_TOKEN")
HEADERS = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {OPEN_GATEWAY_TOKEN}"
}

def verify_number(phone_number: str):
    url = "https://sandbox.opengateway.telefonica.com/apigateway/number-verification/v0/verify"
    payload = { "phoneNumber": phone_number }
    response = requests.post(url, json=payload, headers=HEADERS)
    return response.json()

def verify_identity(full_name: str):
    url = "https://sandbox.opengateway.telefonica.com/apigateway/kyc-match/v0/match"
    payload = { "name": full_name }
    response = requests.post(url, json=payload, headers=HEADERS)
    return response.json()
