import requests

url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count+1\""

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(deck["deck_id"])
