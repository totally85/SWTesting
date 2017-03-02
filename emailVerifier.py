import re


# http://stackoverflow.com/questions/8022530/python-check-for-valid-email-address
def verifyEmail(x):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", x):
        return False
    else:
        return True
