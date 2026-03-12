import requests
import yfinance as yf


def get_crypto():
    url = (
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=bitcoin,ethereum,solana"
        "&vs_currencies=usd"
        "&include_24hr_change=true"
    )

    data = requests.get(url, timeout=10).json()

    return {
        "BTC": (
            data["bitcoin"]["usd"],
            data["bitcoin"]["usd_24h_change"],
        ),
        "ETH": (
            data["ethereum"]["usd"],
            data["ethereum"]["usd_24h_change"],
        ),
        "SOL": (
            data["solana"]["usd"],
            data["solana"]["usd_24h_change"],
        ),
    }


def get_fx():
    url = "https://open.er-api.com/v6/latest/USD"
    data = requests.get(url, timeout=10).json()

    usdkrw = data["rates"]["KRW"]
    usdjpy = data["rates"]["JPY"]

    return usdkrw, usdjpy


def get_index():
    tickers = {
        "S&P500": "^GSPC",
        "NASDAQ100": "^NDX",
        "KOSPI": "^KS11",
        "KOSDAQ": "^KQ11",
        "Gold": "GC=F",
        "WTI": "CL=F",
    }

    results = {}

    for name, ticker in tickers.items():
        try:
            data = yf.Ticker(ticker).history(period="5d", auto_adjust=False)

            if data.empty or "Close" not in data.columns:
                results[name] = (None, None)
                continue

            close_series = data["Close"].dropna()

            if len(close_series) < 2:
                results[name] = (round(float(close_series.iloc[-1]), 2), None) if len(close_series) == 1 else (None, None)
                continue

            price = float(close_series.iloc[-1])
            prev = float(close_series.iloc[-2])
            change = ((price - prev) / prev) * 100 if prev != 0 else None

            results[name] = (
                round(price, 2),
                round(change, 2) if change is not None else None,
            )

        except Exception as e:
            print(f"{name} 지수 수집 오류: {e}")
            results[name] = (None, None)

    return results


def get_market_data():
    crypto = get_crypto()
    usdkrw, usdjpy = get_fx()
    index = get_index()

    return {
        "USD/KRW": usdkrw,
        "USD/JPY": usdjpy,
        "crypto": crypto,
        "index": index,
    }