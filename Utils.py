from .Core import Emailer
import os

emailer = Emailer()

def sendQuickMail(sdAttrs,title,main):
    #emailer = Emailer()
    emailer.sendMail(
            os.environ["USER"]+"@"+os.environ["HOSTNAME"],
            sdAttrs,
            title,
            main,
            )

def getTimeStamp():
    #emailer = Emailer()
    return emailer.getTimeStr()
