from .search_stock import get_stock
import time
from datetime import datetime, timedelta
from .notification import sendMail, sendSMS

def send_alert_background(alert_id, stockSymbol, stockPrice, notificationEmail, notificationNumber, notificationType, stockinterval, stockintervalType):
    send_Alert(alert_id, stockSymbol, stockPrice, notificationEmail, notificationNumber, notificationType, stockinterval, stockintervalType)

def send_Alert(alert_id, stockSymbol, stockPrice, notificationEmail, notificationNumber, notificationType, stockinterval, stockintervalType):
    stock_data = get_stock(stockSymbol)
    current_price = stock_data['currentPrice']
    input_stockPrice = float(stockPrice)
    threshold_loop(stockSymbol, input_stockPrice, notificationEmail, notificationNumber, notificationType, stockinterval, stockintervalType)

def threshold_loop(stockSymbol, input_stockPrice, notificationEmail, notificationNumber, notificationType, stockinterval, stockintervalType):
    if stockintervalType == "days":
        timer = stockinterval*24*60
    else:
        timer = stockinterval*60

    while True:
        threshold(stockSymbol, input_stockPrice, notificationEmail, notificationNumber, notificationType, stockinterval, stockintervalType)
        now = datetime.now()
        next_minute = (now + timedelta(minutes=timer)).replace(second=0, microsecond=0)
        time_to_wait = (next_minute - now).total_seconds()
        time.sleep(time_to_wait)

def threshold(stockSymbol, input_stockPrice, notificationEmail, notificationNumber, notificationType, stockinterval, stockintervalType):
    stock_data = get_stock(stockSymbol)
    current_price = stock_data['currentPrice']
    if current_price > input_stockPrice:
        if notificationType == "mail":
            sendMail(notificationEmail,stockSymbol, input_stockPrice, current_price)
        else:
            sendSMS(notificationNumber, stockSymbol, input_stockPrice, current_price)