#!/usr/bin/env python3

from subprocess import run
from time import sleep
from playsound import playsound
from gtts import gTTS
from os import remove
from os.path import exists


def check_status():
    with open("/sys/class/power_supply/BAT0/status") as f:
        state = f.readline().strip()

    if state == "Discharging":
        return True

    return False


def check_capacity():

    with open("/sys/class/power_supply/BAT0/capacity") as f:
        capacity = f.readline().strip()

    if int(capacity) <= 30:
        return True, capacity

    return False


while True:

    if check_capacity() and check_status():
        run(
            f"notify-send 'Battery Critical -> { check_capacity()[1] }'",
            shell=True
        )

        playsound('/home/cafo/lang/python/.hehe.mp3')
    sleep(60)