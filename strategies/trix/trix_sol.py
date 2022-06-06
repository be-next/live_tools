import sys
import ta
import json
import logging

sys.path.append("./live_tools")

from utilities.spot_ftx import SpotFtx
from utilities.custom_indicators import Trix


# Init log
logging.basicConfig(format='%(asctime)s - %(levelname)s - Bot trix SOL - %(message)s', level=logging.INFO)
logging.info('Start')

# FTX connexion
logging.info("Connecting to FTX sub account...")

f = open(
    "./live_tools/secret.json",
)
secret = json.load(f)
f.close()

account_to_select = "bot#02_trade"

ftx = SpotFtx(
    apiKey=secret[account_to_select]["apiKey"],
    secret=secret[account_to_select]["secret"],
    subAccountName=secret[account_to_select]["subAccountName"],
)

logging.info("Connected to the FTX sub account " + secret[account_to_select]["subAccountName"])

#
pair_symbol = 'SOL/USD'
symbol_coin = 'SOL'
symbol_usd = 'USD'
timeframe = "1h"

# TRX parameters
trixWindow = 7
trixSignal = 21
stochWindow = 20
stochOverBought = 0.7
stochOverSold = 0.25

# Data load
logging.info("Start loading indicators...")
df = ftx.get_last_historical(pair_symbol, timeframe, 41)
#
min_order_amount = float(ftx.get_min_order_amount(pair_symbol))

# Compute indicators
trix = Trix(close=df['close'], trixLength=trixWindow, trixSignal=trixSignal)
df['TRIX_HISTO'] = trix.trix_histo()
df['STOCH_RSI'] = ta.momentum.stochrsi(close=df['close'], window=stochWindow)
logging.info("Indicators loaded")

print(df)
print(min_order_amount)

# -- Trade Functions --
# -- Condition to BUY market --
def buyCondition(row, previousRow = None):
    if (
        row['TRIX_HISTO'] >= 0
        and row['STOCH_RSI'] < stochOverBought
    ):
        return True
    else:
        return False

# -- Condition to SELL market --
def sellCondition(row, previousRow = None):
    if (
        row['TRIX_HISTO'] < 0
        and row['STOCH_RSI'] > stochOverSold
    ):
        return True
    else:
        return False


balance_coin = ftx.get_balance_of_one_coin(symbol_coin)
balance_usd = ftx.get_balance_of_one_coin(symbol_usd)

logging.info("Balance " + symbol_coin + " : " + str(balance_coin))
logging.info("Balance " + symbol_usd + " : " + str(balance_usd))

# iloc -2 to get the last completely close candle
row = df.iloc[-2]
row_time = df.index[-2]

logging.info("timestamp: " + str(row_time) + ", close: " + str(row['close']) + ", TRIX_HISTO: " + str(row['TRIX_HISTO']) + ", STOCH_RSI: " + str(row['STOCH_RSI']))

logging.info("Test sell conditions...")
if balance_coin > min_order_amount:
    if sellCondition(row):
        amount_to_sell = balance_coin
#        ftx.place_market_order(pair_symbol, "sell", amount_to_sell)
        logging.info("** Sell order: " + str(ftx.convert_amount_to_precision(pair_symbol, amount_to_sell)) + " " + symbol_coin + " at the price of ~" + str(row['close']) + " $")
    else:
        logging.info("* Sell conditions: False")
else:
    logging.info("* No coin to sell")

logging.info("Test buy conditions...")
if balance_usd > (min_order_amount * row['close']):
    if buyCondition(row):
        amount_to_buy = balance_usd / row["close"]
#        ftx.place_market_order(pair_symbol, "buy", amount_to_buy)
        logging.info( "** Buy order: " + str(ftx.convert_amount_to_precision(pair_symbol, amount_to_buy)) + " " + symbol_coin + " at the price of ~" + str(row['close']) + " $")
    else:
        logging.info("* Buy conditions: False")
else:
    logging.info("* Not enough " + symbol_usd + " to buy any coin")


logging.info('Finished')