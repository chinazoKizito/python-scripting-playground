import smtplib



fromaddr = 'softmilkchinazo@gmail.com'
toaddrs = 'kizitochinazo@gmail.com'
msg = 'My boy, you are a python master'
username = 'softmilkchinazo@gmail.com'
password = '123456qw!'
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(username, password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
print('Email sent boss')
