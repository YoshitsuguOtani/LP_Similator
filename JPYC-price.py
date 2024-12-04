#CryptoNavi
#BTCUSD, ETHUSD, BTCETHUSD, 
#BTCJPY, ETHJPY, BTCETHJPY,
#BTCEUR, ETHEUR, BTCETHEUR,
import requests

def get_bitcoin_price():
    # CoinGeckoのAPIエンドポイント
    url = 'https://api.coingecko.com/api/v3/simple/price'
    # パラメータとしてビットコインの価格をUSDで取得
    params = {
        'ids': 'bitcoin',
        'vs_currencies': 'usd'
    }
    # GETリクエストを送信してレスポンスを取得
    response = requests.get(url, params=params)
    # レスポンスのJSONをパース
    data = response.json()
    # ビットコインの価格を取得
    price = data['bitcoin']['usd']
    return price
# ビットコインの現在の価格を取得して表示
bitcoin_price = round(get_bitcoin_price(), 2)
print(f"BTC/USD: ${bitcoin_price}")

def get_ethereum_price():
    # CoinGeckoのAPIエンドポイント
    url = 'https://api.coingecko.com/api/v3/simple/price'
    # パラメータとしてイーサリアムの価格をUSDで取得
    params = {
        'ids': 'ethereum',
        'vs_currencies': 'usd'
    }
    # GETリクエストを送信してレスポンスを取得
    response = requests.get(url, params=params)
    # レスポンスのJSONをパース
    data = response.json()
    # イーサリアムの価格を取得
    price = data['ethereum']['usd']
    return price
# イーサリアムの現在の価格を取得して表示
ethereum_price = round(get_ethereum_price(), 2)
print(f"ETH/USD: ${ethereum_price}")

BTCETH = round(bitcoin_price / ethereum_price, 2)
print(f"BTC/ETH Ratio: {BTCETH}")

def get_JPYC_price():
    # CoinGeckoのAPIエンドポイント
    url = 'https://api.coingecko.com/api/v3/simple/price'
    # パラメータとしてイーサリアムの価格をUSDで取得
    params = {
        'ids': 'jpy-coin',
        'vs_currencies': 'usd'
    }
    # GETリクエストを送信してレスポンスを取得
    response = requests.get(url, params=params)
    # レスポンスのJSONをパース
    data = response.json()
    # イーサリアムの価格を取得
    price = data['jpy-coin']['usd']
    return price
# イーサリアムの現在の価格を取得して表示
JPYC_price = round(get_JPYC_price(), 6)
#JPYC/USD: 1/JPYC
print(f"JPYC=$1USD: {round(1/JPYC_price, 2)}")