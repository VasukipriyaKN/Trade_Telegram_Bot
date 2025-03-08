import info
import strategy
import bot

# CREATE OBJECT
symbol = info.SENSEX
info_object = info.StockInfo(symbol)

strategy_object = strategy.Strategy1(symbol)
result = strategy_object.result()
message = f"{symbol} {result[0]} {result[1]}"

# Run the bot
if __name__ == '__main__':
    bot.main()