from pygame import mixer
import schedule
import time

mixer.init()
mixer.music.load('bell.mp3')

def notify():
    mixer.music.play()

schedule.every().monday.  at('08:25').do(notify)
schedule.every().tuesday. at('08:25').do(notify)
schedule.every().thursday.at('08:25').do(notify)

schedule.every().monday.  at('08:58').do(notify)
schedule.every().tuesday. at('08:58').do(notify)
schedule.every().thursday.at('08:58').do(notify)

schedule.every().monday.  at('09:58').do(notify)
schedule.every().tuesday. at('09:58').do(notify)
schedule.every().thursday.at('09:58').do(notify)

schedule.every().monday.  at('10:58').do(notify)
schedule.every().tuesday. at('10:58').do(notify)
schedule.every().thursday.at('10:58').do(notify)

schedule.every().monday.  at('12:58').do(notify)
schedule.every().tuesday. at('12:58').do(notify)
schedule.every().thursday.at('12:58').do(notify)

schedule.every().wednesday.at('08:55').do(notify)
schedule.every().wednesday.at('09:28').do(notify)
schedule.every().wednesday.at('10:33').do(notify)
schedule.every().wednesday.at('11:37').do(notify)
schedule.every().wednesday.at('13:13').do(notify)

schedule.every().friday.at('08:25').do(notify)
schedule.every().friday.at('12:58').do(notify)

while True:
    schedule.run_pending()
    time.sleep(1)