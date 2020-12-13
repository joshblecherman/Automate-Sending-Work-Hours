import smtplib, ssl 
from socket import gaierror

context = ssl.create_default_context()

smtp_server = "smtp.gmail.com"
port_number = 465
sender = "joshblecherman@gmail.com"
PASSWORD = "ariAriari"
receiver = "jab1369@nyu.edu"

def createMessage(sender, receiver, month, period):

    with open('hours.txt', 'r') as file: 
        hours = file.read().splitlines() 
        hours = [line.split() for line in hours]
        start = hours.index([month]) + 1
        if period[0] == 15:
            while int(hours[start[0]]) < 15:
                start += 1
        hours = hours[start:]
         
    message = f"""From: {sender}
    To: {receiver}
    Subject: <Hours for {month} {period[0]} - {period[1]}>\n
    """
    total = 0
    for line in hours: 
        message += f"{month} {line[0]}: {line[1]}\n"
        total += int(line[1][0])
    message += f"Total: {total}\n\n"

    message += """Best, 
    Josh"""

    return message

month = input("Month: ")
period_start = input("Period(start): ")
period_end = input("Period(end): ")
period = period_start, period_end

message = createMessage(sender, receiver, month, period)

try: 
    #send your message with credentials specified above
    with smtplib.SMTP_SSL(smtp_server, context=context) as server:
        server.login(sender, PASSWORD)
        server.sendmail(sender, receiver, message)
    print('Sent')
except (gaierror, ConnectionRefusedError):
    print('Failed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
    print('Failed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))