from playsound import playsound
import time
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def alarm(secounds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < secounds:
        time.sleep(1)
        time_elapsed += 1

        time_left = secounds - time_elapsed
        minutes_left = time_left // 60
        secounds_left = time_left % 60

        print(f"Alarm will sound in : {CLEAR_AND_RETURN}{minutes_left:02d}:{secounds_left:02d}")

    playsound("alarm.mp3")

minutes = int(input("How many minutes to wait: "))
secounds = int(input("How many secounds to wait: "))
alarm(minutes*60+secounds)