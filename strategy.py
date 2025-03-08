import info

# DEFINE STRATEGY
class Strategy1:
    def __init__(self, ticker):
        self.ticket = ticker
        self.stock = info.StockInfo(ticker)

    def result(self):
        current_price = self.stock.get_current_price()
        open_price = self.stock.get_open_price()
        if current_price > open_price:
            return "UP", current_price
        elif current_price < open_price:
            return "DOWN", current_price
        else:
            return "SAME", current_price