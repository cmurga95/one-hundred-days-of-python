import smtplib

my_email = "cmmurgav@hotmail.com"
password = "uS-B8(ApJyY=r2C"
connection = smtplib.SMTP("smtp.live.com")
connection.starttls()
connection.login(user = my_email, password = password)
connection.sendmail(from_addr = my_email
                    , to_addrs = "murga.carlos2013@gmail.com"
                    , msg = "Hello")

