import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
"This code preferred byte like message not EmailMessage"
email = EmailMessage()
email['from'] = 'softmilkchinazo@gmail.com'
email['to'] = 'kizitochinazo@gmail.com'
email['subject'] = 'you won 1000000 dollars'

email.set_content(html.substitute({'name': 'Kizito nwam', 'age': 25}), 'html')

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.ehlo()
    smtp.login('softmilkchinazo@gmail.com', '123456qw!')
    smtp.send(email)
    smtp.quit()
    smtp.close()

    print('all good boss')
