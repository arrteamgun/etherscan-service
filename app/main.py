from dotenv import load_dotenv
import os
import requests


def get_last_block(url: str):
    payload = {'module': 'proxy',
               'action': 'eth_blockNumber', 'apikey': api_key}
    resp = requests.get(url, params=payload)
    data = resp.json()
    return int(data['result'], 16)


def get_transactions(api_key: str, url: str):
    payload = {'module': 'proxy', 'action': 'eth_getBlockByNumber',
               'apikey': api_key, 'boolean': 'true', 'tag': f'{hex(i)}'}
    res = requests.get(url, params=payload).json()
    return res['result']['transactions']


def main():
    load_dotenv()
    api_key = os.getenv("API_KEY")
    etherscan_api_url = os.getenv("ETHERSCAN_API_URL")
    counter = {}

    last_block = get_last_block(etherscan_api_url)

    for _ in range(last_block-100, last_block):
        transactions = get_transactions(api_key, etherscan_api_url)
        for t in transactions:
            t_from = t['from']
            t_to = t['to']
            t_value = int(t['value'], 16)
            counter[t_from] = counter.get(t_from, 0) + t_value
            counter[t_to] = counter.get(t_from, 0) - t_value

    max_key = max(counter, key=counter.get)
    max_value = counter[max_key]
    print(
        f'Address with maximum changing for last 100 blocks: {max_key}.\nChanged on: {max_value}')


if __name__ == "__main__":
    main()
