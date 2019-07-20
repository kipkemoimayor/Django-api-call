import requests

def make_call():
    response= requests.get("https://api.airtable.com/v0/apptf9xPJazK1Lso8/Transactions?api_key=keyBuxrgTLexTtnqU")

    data=response.json()
    return data
