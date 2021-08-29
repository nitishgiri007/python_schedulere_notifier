from logging import NullHandler
import schedule
import time
import winsound
from plyer import notification


def sleep():
    print("time to sleep ....")
    winsound.PlaySound('TF001.WAV', winsound.SND_ASYNC)

    while True:
        notification.notify(
            title="SLEEP",
            message="Time to SLEEP ",
            timeout=15
        )
        time.sleep(10)

    # winsound.PlaySound('TF001.WAV', winsound.SND_ASYNC)


def wake():
    print("time to wake up....")
    winsound.PlaySound('TF002.WAV', winsound.SND_ASYNC)
    while True:
        notification.notify(
            title="Wake",
            message="Time to WAKE_UP ",
            timeout=15
        )
        time.sleep(10)


def code():
    print("time to coding....")
    winsound.PlaySound('TF003.WAV', winsound.SND_ASYNC)
    while True:
        notification.notify(
            title="COADING",
            message="Time to COADING ",
            timeout=15
        )
        time.sleep(10)


def game():
    print("time to play games....")
    winsound.PlaySound('TF004.WAV', winsound.SND_ASYNC)
    while True:
        notification.notify(
            title="GAME",
            message="Time to play GAME ",
            timeout=15
        )
        time.sleep(10)


schedule.every().day.at("00:21").do(sleep)
schedule.every().day.at("05:00").do(wake)
schedule.every().day.at("00:28").do(code)
schedule.every().day.at("14:00").do(game)

while True:
    schedule.run_pending()
    time.sleep(1)
