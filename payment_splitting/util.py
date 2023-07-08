import requests, json
from django.http import HttpResponse

def create_charge(apikey, amount):
    url = "https://api.zebedee.io/v0/charges"
    heads = {'Content-Type': 'application/json', 'apikey': apikey}
    payload = {
    "expiresIn": 300,
    "amount": str(amount),
    "description": "My Charge Description",
    "internalId": "11af01d092444a317cb33faa6b8304b8",
    "callbackUrl": "https://782f-2600-8800-4c41-2200-4bc-d780-8b60-8419.ngrok.io/callback"
    }
    res = requests.post(url, headers=heads, data=json.dumps(payload)).json()

    # {'id': 'b6c35a86-9808-4875-80fe-503d591ee1ff', 'unit': 'msats', 'slots': 0, 'minAmount': '1000000', 'maxAmount': '2000000', 'createdAt': '2022-05-20T07:48:48.183Z', 'expiresAt': None, 'internalId': '11af01d092444a317cb33faa6b8304b8', 'description': 'My Static Charge Description', 'callbackUrl': 'https://782f-2600-8800-4c41-2200-4bc-d780-8b60-8419.ngrok.io/callback', 'allowedSlots': 1, 'successMessage': 'Congratulations your donation was successful!', 'status': 'active', 'invoice': {'request': 'lnurl1dp68gurn8ghj7ctsdyh85etzv4jx2efwd9hj7a3s9aex2ut4v4ehgttnw3shg6tr943ksctjvajhxtmzxe3nxdtp8qmz6wfcxquz6dpcxu6j6wpsvejj6dfsxdjr2wf3v4jnzenx25wtcl', 'uri': 'lightning:lnurl1dp68gurn8ghj7ctsdyh85etzv4jx2efwd9hj7a3s9aex2ut4v4ehgttnw3shg6tr943ksctjvajhxtmzxe3nxdtp8qmz6wfcxquz6dpcxu6j6wpsvejj6dfsxdjr2wf3v4jnzenx25wtcl'}}
    return res

def create_static_charge(apikey):
    url = "https://api.zebedee.io/v0/static-charges"
    heads = {'Content-Type': 'application/json', 'apikey': apikey}
    payload = {
	"allowedSlots": 1,
    "minAmount": 1000000,
    "maxAmount": 2000000,
    "description": "My Static Charge Description",
    "internalId": "11af01d092444a317cb33faa6b8304b8",
    "callbackUrl": "https://782f-2600-8800-4c41-2200-4bc-d780-8b60-8419.ngrok.io/callback",
    "successMessage": "Congratulations your donation was successful!"
    }
    res = requests.post(url, headers=heads, data=json.dumps(payload)).json()

    # {'id': 'b6c35a86-9808-4875-80fe-503d591ee1ff', 'unit': 'msats', 'slots': 0, 'minAmount': '1000000', 'maxAmount': '2000000', 'createdAt': '2022-05-20T07:48:48.183Z', 'expiresAt': None, 'internalId': '11af01d092444a317cb33faa6b8304b8', 'description': 'My Static Charge Description', 'callbackUrl': 'https://782f-2600-8800-4c41-2200-4bc-d780-8b60-8419.ngrok.io/callback', 'allowedSlots': 1, 'successMessage': 'Congratulations your donation was successful!', 'status': 'active', 'invoice': {'request': 'lnurl1dp68gurn8ghj7ctsdyh85etzv4jx2efwd9hj7a3s9aex2ut4v4ehgttnw3shg6tr943ksctjvajhxtmzxe3nxdtp8qmz6wfcxquz6dpcxu6j6wpsvejj6dfsxdjr2wf3v4jnzenx25wtcl', 'uri': 'lightning:lnurl1dp68gurn8ghj7ctsdyh85etzv4jx2efwd9hj7a3s9aex2ut4v4ehgttnw3shg6tr943ksctjvajhxtmzxe3nxdtp8qmz6wfcxquz6dpcxu6j6wpsvejj6dfsxdjr2wf3v4jnzenx25wtcl'}}
    return res


def pay_to_ln_address(apikey, lnaddress, amount):
    url = "https://api.zebedee.io/v0/ln-address/send-payment"
    heads = {'Content-Type': 'application/json', 'apikey': apikey}
    print(amount)
    payload = {
        "lnAddress": lnaddress,
        "amount": str(amount) + "000",
        "description": "Payment split!"
    }
    res = requests.post(url, headers=heads, data=json.dumps(payload)).json()
    print(res)
    return res

def get_withdrawal(apikey):
    url = "https://api.zebedee.io/v0/withdrawal-requests"
    heads = {'Content-Type': 'application/json', 'apikey': apikey}
    payload = {
	"expiresIn": 300,
	"amount": "10000",
	"description": "My Withdrawal Description",
	"internalId": "test transaction",
	"callbackUrl": "https://2dfb-2600-8800-4c40-6400-34c1-5a0e-d61c-19f6.ngrok.io/callback"
    }
    res = requests.post(url, headers=heads, data=json.dumps(payload)).json()


    return res