# فایل momentum.py

def is_momentum_high(data_m15, threshold):
    distance = abs(data_m15['close'].iloc[-2] - data_m15['tenkan_sen'].iloc[-2])
    return distance > threshold

def is_reverse_cross_in_m1(data_m1, trade_type):
    if trade_type == "buy":
        return data_m1['tenkan_sen'].iloc[-3] > data_m1['kijun_sen'].iloc[-3] and data_m1['tenkan_sen'].iloc[-2] < data_m1['kijun_sen'].iloc[-2]
    elif trade_type == "sell":
        return data_m1['tenkan_sen'].iloc[-3] < data_m1['kijun_sen'].iloc[-3] and data_m1['tenkan_sen'].iloc[-2] > data_m1['kijun_sen'].iloc[-2]
    return False
