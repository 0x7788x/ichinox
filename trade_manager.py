# فایل trade_manager.py
import MetaTrader5 as mt5

def has_open_trade(symbol):
    open_positions = mt5.positions_get(symbol=symbol)
    return len(open_positions) > 0

def enter_trade(symbol, equity, entry_price, sl_price, trade_type, risk_percentage):
    symbol_info = mt5.symbol_info(symbol)
    pip_value = 0.0001
    dollar_per_pip = 10
    volume_min = symbol_info.volume_min
    volume_max = symbol_info.volume_max
    volume_step = symbol_info.volume_step

    # محاسبه حجم معامله
    risk_amount = equity * risk_percentage
    distance_to_sl_pips = abs(entry_price - sl_price) / pip_value
    volume = risk_amount / (distance_to_sl_pips * dollar_per_pip)
    volume = max(volume_min, min(volume, volume_max))
    volume = (volume // volume_step) * volume_step

    # تنظیم درخواست معامله
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": mt5.ORDER_TYPE_BUY if trade_type == "buy" else mt5.ORDER_TYPE_SELL,
        "price": entry_price,
        "sl": sl_price,
        "magic": 234000,
        "comment": f"{trade_type.capitalize()} trade based on Ichimoku",
    }

    result = mt5.order_send(request)
    return result
