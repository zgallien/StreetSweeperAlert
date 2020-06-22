# StreetSweeperAlert
No more street sweeping tickets! Send an email to recipients the day before street sweeping.

Built with Python 3 using native modules.

Set up to run daily on my Raspberry-Pi via crontab:

crontab -l:

20 16 * * * \\
cd /home/pi/python_projects/street_sweeper && \\
. /home/pi/python_projects/street_sweeper/run.sh >> /home/pi/python_projects/street_sweeper/log.txt 2>&1

Notes:
Currently designed for my street sweeping rules (first Mon and Tues of the month). Need to expand as recipients grow.
