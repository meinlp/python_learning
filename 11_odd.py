from datetime import datetime
from random import randint
import time
 
odds = list(range(1, 60, 2))

for i in range(5):
    right_this_minute = datetime.today().minute
    time_all = datetime.today()
    if right_this_minute in odds:
        print("this minute seems a little odd.")
    else:
        print("not an odd minute")
    sleep_time = randint(1, 10)
    print("sleep time=", sleep_time)
    time.sleep(sleep_time)
