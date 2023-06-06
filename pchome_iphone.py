import requests
import json

num = 1
while num < 6:

	responce = requests.get('https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=iphone&page={}&sort=sale/dc'.format(num))
	jsonData = json.loads(responce.text)

	for item in jsonData['prods']:
		name = item['name']
		price = item['price']

		print(name + ' $' + str(price))

	num += 1