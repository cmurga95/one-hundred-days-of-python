import smtplib


# with smtplib.SMTP("smtp.gmail.com") as connection:

#     connection.starttls()
#     connection.login(user = my_email, password = password)
#     connection.sendmail(from_addr = my_email
#                         , to_addrs = "murga.carlos2013@gmail.com"
#                         , msg = "Subject: Motivational stuff\n\nThis is the body of the email"
#                         )
#     # connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

date_of_birth = dt.datetime(year = 1995, month = 12, day = 15)

print(date_of_birth)

with open("quotes.txt") as file:
    data = [x for x in file]

print(data[0])