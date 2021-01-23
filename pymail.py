import smtplib
import getpass
import sys
import re


class colors:
    header = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end = '\033[0m'
    bold = '\033[1m'


print(f"{colors.header}PyMail{colors.end}")
print(f"{colors.bold}===================={colors.end}")
print()
print(f"{colors.green} TIP: If your using gmail remember to turn off \"Less secure app access\" in Google Account > Secrity")
print()

regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
try:
    server = smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
except Exception as err:
    print(f"{colors.red}Cannot connect to server.{colors.end}")
    print()
    print(err)



print(f"{colors.blue}LOGIN:{colors.end}")
print()

username = input(f"{colors.yellow}Email address > {colors.end}")
password = getpass.getpass(f"{colors.yellow}Email password 🔒 > {colors.end}")


if username == "":
    print(f"{colors.red}Please enter a email.{colors.end}")
    sys.exit()

if not re.search(regex, username):
    print(f"{colors.red}Please enter a vaild email address.{colors.end}")
    sys.exit()


if password == "":
    print(f"{colors.red}Please enter a password.{colors.end}")
    sys.exit()


print()
print(f"{colors.blue}Attempting to login...{colors.end}")
try:
    server.login(username, password)
    print(f"{colors.green}Login successful!{colors.end}")
except Exception as err:
    server.quit()
    print(f"{colors.red}Invaild credentials, please try again{colors.end}")
    print()
    print(err)
    print()
    sys.exit()

print()
print(f"{colors.blue}Send mail:{colors.end}")
print()

toEmail = input(f"{colors.yellow}To > {colors.end}")
message = input(f"{colors.yellow}Contents > {colors.end}")

if message == "":
    print(f"{colors.red}Please enter a message to send.{colors.end}")
    msg()

if toEmail == "":
    print(f"{colors.red}Please enter a email.{colors.end}")
    sys.exit()

if not re.search(regex, toEmail):
    print(f"{colors.red}Please enter a vaild email address.{colors.end}")
    sys.exit()

try:
    server.sendmail(username, toEmail, message)
    print(f"{colors.green}Email sent!{colors.end}")
except Exception as err:
    print(f"{colors.red}Invaild email{colors.end}")
    print()
    print(err)
    print()

server.quit()
sys.exit()
