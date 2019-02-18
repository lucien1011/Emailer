from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib,time

class Emailer(object):
    def __init__(self):
        self.msg = MIMEMultipart()
        self.server = smtplib.SMTP("localhost")

    def sendMail(self,sdAddr,toAddr,subject,main):
        self.msg = MIMEMultipart()
        self.msg['From'] = sdAddr
        self.msg['To'] = toAddr
        self.msg['Subject'] = subject 
        self.msg.attach(MIMEText(main, 'plain'))

        text = self.msg.as_string()

        self.server = smtplib.SMTP("localhost")
        self.server.sendmail(sdAddr, toAddr, text)

    def getUserName(self):
        return str(os.environ['USER'])

    def getTimeStr(self):
        curTime=(time.strftime("%H:%M:%S"))
        curDate=(time.strftime("%d/%m/%Y"))
        return curDate+" ; "+curTime 

    def end():
        self.server.quit()
