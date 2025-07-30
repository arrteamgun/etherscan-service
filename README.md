# etherscan-service

## Preparations - packages

First, you have to simply install dotenv package with venv:

```
python3 -m venv .ve 
```

Then activate it with

```
source .ve/bin/activate
```

Installing dotenv package:

```
pip install python-dotenv
```

## Preparations - .env

Then we have to add .env file to the root of the project:

```
API_KEY=your_api_key_from_etherscan
ETHERSCAN_API_URL=https://api.etherscan.io/api
```

How to get API_KEY: https://docs.etherscan.io/getting-started/viewing-api-usage-statistics

## How to run a file

```
cd app
python main.py
```