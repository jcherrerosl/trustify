import os
import requests

def get_access_token():
    url = "https://sandbox.opengateway.telefonica.com/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": os.getenv("OPEN_GATEWAY_CLIENT_ID"),
        "client_secret": os.getenv("OPEN_GATEWAY_CLIENT_SECRET")
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=data, headers=headers)
    return response.json().get("access_token")

def verify_identity_and_number(phone, name):
    access_token = get_access_token()
    if not access_token:
        return None

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Número
    phone_url = "https://sandbox.opengateway.telefonica.com/apigateway/number-verification/v0/verify"
    phone_payload = { "phoneNumber": phone }
    phone_response = requests.post(phone_url, json=phone_payload, headers=headers)

    # Identidad (KYC Match)
    kyc_url = "https://sandbox.opengateway.telefonica.com/apigateway/kyc-match/v0/match"
    kyc_payload = { "consentReference": name }
    kyc_response = requests.post(kyc_url, json=kyc_payload, headers=headers)

    return {
        "Número verificado": phone_response.json(),
        "Coincidencia KYC": kyc_response.json()
    }
