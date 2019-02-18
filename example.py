from Core import Emailer

emailer = Emailer()
emailer.sendMail(
        "klo@cern.ch",
        "klo@cern.ch",
        "Testing subject",
        "Testing my Emailer package",
        )
