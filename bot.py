import info
import strategy
import telegram
from telegram.ext import Application, CommandHandler
import logging

# Telegram bot token 
BOT_TOKEN = ''   # Add your bot token here

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# List of symbols
symbols = {
    "NIFTY    ": "^NSEI",
    "SENSEX   ": "^BSESN",
    "BANKNIFTY": "^NSEBANK",
    "MIDCAP   ": "NIFTY_MID_SELECT.NS",
    "FINNIFTY ": "NIFTY_FIN_SERVICE.NS"
}

# Command handler function
async def res_command(update, context):
    messages = []
    for name, symbol in symbols.items():
        info_object = info.StockInfo(symbol)
        strategy_object = strategy.Strategy1(symbol)
        result = strategy_object.result()
        message = f"<code>{name}  :  <b>{result[0]}</b>   -   {result[1]}</code>"
        messages.append(message)
    
    full_message = "\n".join(messages)
    try:
        await update.message.reply_text(full_message, parse_mode=telegram.constants.ParseMode.HTML)
    except telegram.error.NetworkError as e:
        logger.error(f"Network error occurred: {e}")
        await update.message.reply_text("Failed to send message due to network error")

async def info_command(update, context):
    messages = []
    for name, symbol in symbols.items():
        info_object = info.StockInfo(symbol)
        message = f"<code><b>{name}</b>\n\n"
        message += f"LTP  : {info_object.get_current_price()}\n"
        message += f"OPEN : {info_object.get_open_price()}\n"
        message += f"HIGH : {info_object.get_highest_price()}\n"
        message += f"LOW  : {info_object.get_lowest_price()}\n"
        message += f"PREV : {info_object.get_previous_close_price()}\n"
        message += f"RANGE: {info_object.get_today_price_range()}</code>\n"
        messages.append(message)
    
    full_message = "\n".join(messages)
    try:
        await update.message.reply_text(full_message, parse_mode=telegram.constants.ParseMode.HTML)
    except telegram.error.NetworkError as e:
        logger.error(f"Network error occurred: {e}")
        await update.message.reply_text("Failed to send message due to network error")

def main():
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(BOT_TOKEN).build()

    # Register the /res command handler
    application.add_handler(CommandHandler('res', res_command))

    # Register the /info command handler
    application.add_handler(CommandHandler('info', info_command))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()