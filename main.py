import MetaTrader5 as mt5
import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.max_rows', 20000)
pd.set_option('display.width', 1500)

currency_pare = 'GBPUSD'
timeframe = mt5.TIMEFRAME_M15

if mt5.initialize():
    print('ok')
else:
    print(mt5.last_error())

rates = mt5.copy_rates_from_pos(currency_pare, timeframe, 0, 1836240)

rate_frame = pd.DataFrame(rates)
rate_frame['time'] = pd.to_datetime(rate_frame['time'], unit='s')
rate_frame.to_csv('1.csv', index=False)
# print(rate_frame)
