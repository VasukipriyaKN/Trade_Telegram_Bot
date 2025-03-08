# Trade_Telegram_Bot

This project is a trading bot that fetches Indian Stock Index's information and provides sample trading strategies using the `yfinance` library. The bot can send updates via Telegram.

1. Install below packages
   pip install yfinance
   pip install python-telegram-bot

2. Create Telegram Bot and replace in BOT_TOKEN placeholder. (Bot.py Line No 8)

3. Run python main.py

### Symbols

The bot currently supports the following symbols:
- NIFTY: `^NSEI`
- SENSEX: `^BSESN`
- BANKNIFTY: `^NSEBANK`
- MIDCAP: `NIFTY_MID_SELECT.NS`
- FINNIFTY: `NIFTY_FIN_SERVICE.NS`
