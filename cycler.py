#!/usr/bin/env python3

import subprocess
import os
import random
from time import sleep

a=subprocess.Popen(
    'echo $HOME',
    shell=True,
    stdout=subprocess.PIPE
)
HOME=a.communicate()[0].decode().strip()+'/'
directory=HOME+'Pictures/Wallpapers/'
pictures=os.listdir(directory)

def cycle():
    global pictures
    random.shuffle(pictures)
    for i in pictures:
        cmd='feh --bg-scale '+directory+i
        subprocess.run(
            cmd,
            shell=True,
        )
        sleep(900)

while True:
    cycle()
