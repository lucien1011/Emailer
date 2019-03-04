from .Core import Emailer
import os
from datetime import datetime

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
    curTime=(time.strftime("%H:%M:%S"))
    curDate=(time.strftime("%d/%m/%Y"))
    return curDate+" ; "+curTime 

def getDateDiff(d1Str,d2Str,d_format,mk_str=False):
    a = datetime.strptime(d1, date_format)
    b = datetime.strptime(d2, date_format)
    delta = b - a
    if mk_str and delta.days == 1: 
        return "tomorrow"
    else:
        return delta.days+" days"
