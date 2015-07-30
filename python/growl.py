#!/usr/bin/python
# use standard Python logging
import logging
import gntp.notifier
import sys
logging.basicConfig(level=logging.INFO)

if len(sys.argv) > 3:
    hostname = sys.argv[1]
    password = sys.argv[2]
    title = sys.argv[3]
    description = sys.argv[4]

    growl = gntp.notifier.GrowlNotifier(
        applicationName=sys.argv[2],
        notifications=["New Updates", "New Messages"],
        defaultNotifications=["New Messages"],
        hostname=hostname,  # Here enter your IP address
        password=password  # Here enter your growl password
    )
    growl.register()
    # Send one message
    # image = open('/var/www/tmp/image.jpg', 'rb').read()
    growl.notify(
        noteType="New Messages",
        title=title,
        description=description,
        # icon = image, #you can optionally define an image icon to appear with the notification
        sticky=True,
        priority=1,
    )
else:
    print "You didn't provide enough argument"
    print "-----------------------------------------------"
    print "Usage: growl.py IP PASSWORD Title Description"
    print "-----------------------------------------------"
