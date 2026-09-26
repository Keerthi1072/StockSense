import yfinance as yf


def get_stock_data(ticker, period="1y"):
    data = yf.download(
        ticker,
        period=period,
        auto_adjust=False,
        progress=False
    )

    return data