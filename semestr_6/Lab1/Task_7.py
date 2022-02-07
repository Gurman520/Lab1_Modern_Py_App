import schedule
from datetime import datetime
import time
message = ''
slt = 0


def job():
    if int(slt[0:2]) > int(datetime.now().hour) or int(datetime.now().hour) > int(slt[3:5]):
        for i in range(datetime.now().hour % 12):
            print(message)


schedule.every().hour.at(":00").do(job)
# schedule.every(10).seconds.do(job)

message = input("Сообщение которое должна выводить программа: ")
slt = input("Время сна: ")
while True:
    schedule.run_pending()
    time.sleep(1)
