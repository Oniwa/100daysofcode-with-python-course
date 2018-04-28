import datetime as dt
import winsound as ws


def beep():
    frequency = 500
    duration = 1000
    ws.Beep(frequency, duration)


start = dt.datetime.now()
print(f'The timer started at {start}')

timedelta = dt.timedelta(minutes=25)

finish = start + timedelta

print(f'The timer will finish at {finish}')

while dt.datetime.now() < finish:
    pass

beep()

print('You have finished one pomodoro')