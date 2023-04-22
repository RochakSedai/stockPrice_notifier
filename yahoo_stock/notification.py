import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMail(notificationEmail,stockSymbol, input_stockPrice, current_price):
    sender_email = "usstockalerter@gmail.com"
    receiver_email = notificationEmail

    subject = "Stock Alert"
    message = "Stock price is higher than threshold. Symbol: "+stockSymbol+" Threshold Price: "+str(input_stockPrice)+" Current Price: "+str(current_price)
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
