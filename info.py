import yfinance as yf

# DEFINE CONSTANTS
NIFTY     = "^NSEI"
SENSEX    = "^BSESN"
BANKNIFTY = "^NSEBANK"
MIDCAP    = "NIFTY_MID_SELECT.NS"
FINNIFTY  = "NIFTY_FIN_SERVICE.NS"

# DEFINE CLASSES
class StockInfo:
    def __init__(self, ticker):
        self.ticker = ticker
        self.stock = yf.Ticker(ticker)
    
    def get_current_price(self):
        price = self.stock.get_fast_info()['lastPrice']
        return round(price, 2)

    def get_highest_price(self):
        price = self.stock.get_fast_info()['dayHigh']
        return round(price, 2)

    def get_lowest_price(self):
        price = self.stock.get_fast_info()['dayLow']
        return round(price, 2)

    def get_open_price(self):
        price = self.stock.get_fast_info()['open']
        return round(price, 2)

    def get_previous_close_price(self):
        price = self.stock.get_fast_info()['previousClose']
        return round(price, 2)

    def get_today_price_range(self):
        range = self.get_highest_price() - self.get_lowest_price()
        return round(range, 2)

    def get_ohlc_of_given_date(self, date):  # date format: 'YYYY-MM-DD'
        data = self.stock.history(start=date, end=date)
        json_data = data.to_json(orient='records')
        return json_data

    def get_ohlc_of_given_period(self, start_date, end_date):  # date format: 'YYYY-MM-DD'
        data = self.stock.history(start=start_date, end=end_date)
        json_data = data.to_json(orient='records')
        return json_data

    def print_info(self):
        print(f"Current price of {self.ticker} is {self.get_current_price()}")
        print(f"Highest price of {self.ticker} today is {self.get_highest_price()}")
        print(f"Lowest price of {self.ticker} today is {self.get_lowest_price()}")
        print(f"Open price of {self.ticker} today is {self.get_open_price()}")
        print(f"Close price of {self.ticker} yesterday was {self.get_previous_close_price()}")

    def print_info_of_given_date(self, date):
        print(f"OHLC data of {self.ticker} on {date} is {self.get_ohlc_of_given_date(date)}")

    def print_info_of_given_period(self, start_date, end_date):
        print(f"OHLC data of {self.ticker} between {start_date} and {end_date} is {self.get_ohlc_of_given_period(start_date, end_date)}")