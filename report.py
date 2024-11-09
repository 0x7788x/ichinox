# فایل report.py
import csv
import datetime

# تابع ایجاد فایل گزارش
def create_report(filename="trade_report.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Symbol", "Type", "Entry Price", "Exit Price", "Volume", "Profit"])

# تابع ذخیره معامله در گزارش
def log_trade(symbol, trade_type, entry_price, exit_price, volume, profit, filename="trade_report.csv"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, symbol, trade_type, entry_price, exit_price, volume, profit])

# تابع نمایش گزارش
def print_report(filename="trade_report.csv"):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
