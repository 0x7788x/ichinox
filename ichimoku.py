# فایل ichimoku.py
import pandas as pd

def ichimoku(data, digits):
    high9 = data['high'].rolling(9).max()
    low9 = data['low'].rolling(9).min()
    data['tenkan_sen'] = (high9 + low9) / 2

    high26 = data['high'].rolling(26).max()
    low26 = data['low'].rolling(26).min()
    data['kijun_sen'] = (high26 + low26) / 2

    data['senkou_span_a'] = ((data['tenkan_sen'] + data['kijun_sen']) / 2).shift(26)

    high52 = data['high'].rolling(52).max()
    low52 = data['low'].rolling(52).min()
    data['senkou_span_b'] = ((high52 + low52) / 2).shift(26)

    data['chikou_span'] = data['close'].shift(-26)

    return data.round(digits)
