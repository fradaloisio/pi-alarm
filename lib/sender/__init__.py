#sender here

import datetime
import smtplib

def emailAlert():
    to = ['xxxxxx']
    gmail_user = 'xxxxx'
    gmail_pwd = 'xxx'
    smtpserver = smtplib.SMTP("xxx", 25)
    subject = "ALARM!"
    smtpserver.ehlo_or_helo_if_needed()
    smtpserver.starttls()
    smtpserver.ehlo_or_helo_if_needed()
    smtpserver.login(gmail_user, gmail_pwd)
    header = 'To:' + ", ".join(to) + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + subject + '\n'
    msg = header + '\n' + 'Detection at '+str(datetime.datetime.utcnow())+' UTC\n\n'
    smtpserver.sendmail(gmail_user, to, msg)
    smtpserver.close()
