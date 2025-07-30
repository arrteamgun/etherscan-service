from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("API_KEY")
etherscan_api_url = os.getenv("ETHERSCAN_API_URL")

payload = {'module': 'proxy', 'action': 'eth_blockNumber', 'apikey': api_key}
resp = requests.get(etherscan_api_url, params=payload)
data = resp.json()
last_block = int(data['result'], 16)

counter = {}

for i in range(last_block-100, last_block):
    payload = {'module': 'proxy', 'action': 'eth_getBlockByNumber',
               'apikey': api_key, 'boolean': 'true', 'tag': f'{hex(i)}'}
    res = requests.get(etherscan_api_url, params=payload).json()

    transactions = res['result']['transactions']
    for t in transactions:
        t_from = t['from']
        t_to = t['to']
        t_value = int(t['value'], 16)

        counter[t_from] = counter.get(t_from, 0) + t_value
        counter[t_to] = counter.get(t_from, 0) - t_value

max_key = max(counter, key=counter.get)
max_value = counter[max_key]
print(f'Address with maximum changing for last 100 blocks: {max_key}.\nChanged on: {max_value}')