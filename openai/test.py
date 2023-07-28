import requests

url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"

querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"7d"}

headers = {
	"X-RapidAPI-Key": "a617d6467dmshac84323ce581a72p11caa9jsn1adf8bbcbd47",
	"X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)