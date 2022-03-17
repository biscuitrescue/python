#!/usr/bin/env python3
from subprocess import Popen
from subprocess import PIPE
from subprocess import run
from time import sleep

maxmem=2
l=Popen("lsblk -f | awk '/swap/ {printf $1}'", shell=True, stdout=PIPE)
x=l.communicate()[0].decode().strip()
swapdisk=''
for s in x:
    if s.isalpha() or s.isdigit():
        swapdisk+=s

while True:
    check=Popen("lsblk | awk '/SWAP/ {printf $1}'",shell=True,stdout=PIPE)
    outo=check.communicate()[0].decode().strip()
    disk=''
    for k in outo:
        if k.isalpha() or k.isdigit():
            disk+=k
    check=Popen("free -h | awk '/Mem/ {printf $3}'", shell=True, stdout=PIPE)
    out=check.communicate()[0].decode().strip()
    mem=''
    for k in out:
        if not (k.isalpha()):
            mem+=k
    if len(disk)==0 and float(mem)>=maxmem:
        cmd='sudo swapon /dev/'+swapdisk
        run(cmd, shell=True)
    if len(disk)>0 and float(mem)<maxmem:
        cmd='sudo swapoff /dev/'+swapdisk
        run(cmd, shell=True)
    sleep(1)
