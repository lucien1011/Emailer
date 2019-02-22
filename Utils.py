from .Core import Emailer
import os

def sendQuickMail(sdAttrs,title,main):
    emailer = Emailer()
    emailer.sendMail(
            os.environ["USERNAME"]+"@"+os.environ["HOSTNAME"],
            sdAttrs,
            title,
            main,
            )
