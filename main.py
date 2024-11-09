# فایل main.py
import MetaTrader5 as mt5
import pandas as pd
import time
from config import *
from ichimoku import ichimoku
from trade_manager import has_open_trade, enter_trade
from momentum import is_momentum_high, is_reverse_cross_in_m1

if not mt5.initialize():
    print("Failed to initialize MT5")
    quit()

authorized = mt5.login(account_number, password=password, server=server)
if not authorized:
    print("Failed to connect to the trading account")
    quit()

print(f"Connected to account {account_number}")

previous_kijun_sen = None
while True:
    equity = mt5.account_info().equity

    data_m15 = pd.DataFrame(mt5.copy_rates_from_pos(symbol, timeframe_m15, 0, 200))
    data_m15 = ichimoku(data_m15, symbol_info.digits)

    new_kijun_sen = data_m15['kijun_sen'].iloc[-2]

    if is_momentum_high(data_m15, momentum_threshold):
        print("High momentum detected in M15")
        if is_reverse_cross_in_m1(data_m1, "buy"):
            print("Reverse cross detected, exiting trade.")

    time.sleep(60)
