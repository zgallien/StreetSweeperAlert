import datetime
import json
import os
import smtplib


""" Sick of getting tickets!

    Streetsweeper automated alert program.

    This script is run from a cronjob on my Raspberry Pi 3.

    If it is the day before street sweeping, an email will be sent to 
    all recipients.

"""


def run():
    """ Get tomorrow's date and determine if alert should be sent """
    tomorrow_str, tomorrow_day = tomorrow()

    if tomorrow_str == 'Monday' and 1 <= tomorrow_day <= 7:
    
        send_alert('Monday')
    
    elif tomorrow_str == 'Tuesday' and 2 <= tomorrow_day <= 8:
    
        send_alert('Tuesday')


def load_env():
    """ Load params """
    with open('.env.json', 'r') as f:

        env = json.load(f)

        return env


def send_alert(alert_day):
    """ Send email to all recipients """
    env = load_env()

    from_addr = env['email']
    email_pw = env['password']
    recipients = get_recipients()

    # create SMTP object, passing in gmail server and port
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

    # establish connection to server
    smtpObj.ehlo()

    # start TLS encryption
    smtpObj.starttls()

    # re-establish connection to server, now encrypted
    smtpObj.ehlo()

    # login
    smtpObj.login(from_addr, email_pw)

    for to_addr in recipients:

        smtpObj.sendmail(
            f"{from_addr}",
            f"{to_addr}",
            "Subject: Honk Honk! STREET SWEEPING TOMORROW\n"
            f"Tomorrow is the first {alert_day} of the month!\n\n"
            "Don't forget to move your car."
        )


def tomorrow():
    """ Return index and string representations of tomorrow """
    tom =  datetime.date.today() + datetime.timedelta(days=1)

    tomorrow_str = tom.strftime('%A')
    tomorrow_day = tom.day

    return tomorrow_str, tomorrow_day


def get_recipients():
    """ Load recipients JSON """
    with open('recipients.json', 'r') as f:

        recip_json = json.load(f)

        return list(recip_json['recipients'])


if __name__ == '__main__':

    run()
