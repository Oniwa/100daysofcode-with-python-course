import datetime as dt
import winsound as ws

import click


def beep():
    frequency = 500
    duration = 1000
    ws.Beep(frequency, duration)


@click.command()
@click.argument('minutes_to_run')
def pomodoro(minutes_to_run):
    start = dt.datetime.now()
    print(f'The timer started at {start}')

    timedelta = dt.timedelta(minutes=int(minutes_to_run))

    finish = start + timedelta

    print(f'The timer will finish at {finish}')

    while dt.datetime.now() < finish:
        pass

    beep()

    print('You have finished one pomodoro')

if __name__ == "__main__":
    pomodoro()