#sender here

import datetime
import smtplib
import json

def emailAlert():
    with open("config.json") as json_file:
        json_cfg = json.load(json_file)
    to = [json_cfg["contact"]]
    user = json_cfg["sender"]["user"]
    pwd = json_cfg["sender"]["password"]
    smtpserver = smtplib.SMTP(json_cfg["sender"]["smtp_server"], json_cfg["sender"]["smpt_port"])
    subject = "PI-ALARM!"
    smtpserver.ehlo_or_helo_if_needed()
    smtpserver.starttls()
    smtpserver.ehlo_or_helo_if_needed()
    smtpserver.login(user, pwd)
    header = 'To:' + ", ".join(to) + '\n' + 'From: ' + user + '\n' + 'Subject: ' + subject + '\n'
    msg = header + '\n' + 'Detection at '+str(datetime.datetime.utcnow())+' UTC\n\n'
    smtpserver.sendmail(user, to, msg)
    smtpserver.close()
