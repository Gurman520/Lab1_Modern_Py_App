import schedule
from datetime import datetime
import time


def job():
    for i in range(datetime.now().hour % 12):
        print("Ку ")


schedule.every().hour.at(":00").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
