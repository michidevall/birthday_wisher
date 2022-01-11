import pandas as pd
import datetime
import smtplib
from email.message import EmailMessage
import os

def sendEmail(to, sub, msg):
    print(f"email to{to} \nsend with subject: {sub}\n message: {msg}")
    email = EmailMessage()
    email['from'] = 'Michi Devall'
    email['to'] = f"{to}"
    email['subject'] = f'{sub}'
    
    email.set_content(f'{msg}')
    
    with smtplib.SMTP(host)