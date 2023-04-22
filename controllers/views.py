from flask import render_template, request, redirect, jsonify
from yahoo_stock.search_stock import get_stock, check_symbol
from yahoo_stock.threading import send_alert_background
from yahoo_fin import stock_info as si
import uuid
from threading import Thread
import sys
def index():
    return render_template('index.html')

def getstock(stock_symbol: str):
    if stock_symbol == None:
        # return render_template('stock.html')
        return render_template('output_stock.html')
    else:
        result = check_symbol(stock_symbol)
        print(result)
        if not result:
            return render_template('output_stock.html', error="Symbol doesnt exists")
        
        stock_data = get_stock(stock_symbol)
        return render_template('output_stock.html', data=stock_data)

    
def searchStock():
    if request.method == 'POST':
        req = request.form 
        if not req["stock"]:
            return redirect("/stock")
        
        return redirect(f'/stock/{req["stock"]}')



def subscribe():
    data = request.form
    stockSymbol=data['stock']

    result = check_symbol(stockSymbol)
    if not result:
        return render_template('index.html', error="Symbol doesnt exists")
    
    stockPrice=data['threshold']
    notificationEmail=data['email']
    notificationNumber = data['ph_no']
    notificationType = data['notification-type']
    stockinterval=data['time']
    stockintervalType = data['time-type']
    

    alert_id = str(uuid.uuid1())

    thread = Thread(target=send_alert_background, args=(alert_id, stockSymbol, stockPrice, notificationEmail, notificationNumber, notificationType, stockinterval, stockintervalType))
    thread.start()
    return jsonify({'status': 'success', 'message': 'Stock Alert Created', 'alert_id': alert_id})
