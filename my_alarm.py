
import sys
import numpy as np
from time import sleep
import datetime
now = datetime.datetime.now()
i = 0
print("Press Ctrl-C to terminate the alarm clock early.")
hr, min = map(int,input("Give input in 24 hr min format: ").split())
minutes=int(hr-now.hour)*60+int(min-now.minute)

if minutes < 0:
    print("Invalid value for minutes, should be >= 0")
    sys.exit(1)

seconds = minutes * 60

if minutes == 1:
    unit_word = " minute"
else:
    unit_word = " minutes"

try:
    if minutes > 0:
        print("Sleeping for " + str(minutes) + unit_word)
        sleep(seconds)
    print("Wake up")
    for i in range(5):
        print(chr(7),
        sleep(1))
except KeyboardInterrupt:
    print("Interrupted by user")
    sys.exit(1)