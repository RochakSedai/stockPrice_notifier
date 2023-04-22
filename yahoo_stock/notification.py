import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from twilio.rest import Client

def sendMail(notificationEmail,stockSymbol, input_stockPrice, current_price):
    sender_email = "usstockalerter@gmail.com"
    receiver_email = notificationEmail

    subject = "Stock Alert"
    message = "Hey Subscriber!!, Stock price of symbol"+stockSymbol+" is higher than threshold. Threshold Price: "+str(input_stockPrice)+" and Current Price: "+str(current_price)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, "aiigruiuswpusslo")
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)

def sendSMS(notificationNumber, stockSymbol, input_stockPrice, current_price):
    account_sid = 'ACf1807978d7331b24676d44a40577a312'
    auth_token = 'e421caf38466ecf5205613a2493f7449'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body="Hey Subscriber!!, Stock price of symbol"+stockSymbol+" is higher than threshold. Threshold Price: "+str(input_stockPrice)+" and Current Price: "+str(current_price),
            from_='+16813346935',
            to='+9779861923536'
        )
