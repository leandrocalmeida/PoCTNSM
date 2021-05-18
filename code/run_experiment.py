#!/usr/bin/env python3
'''
Created on May 17, 2021
@authors: leandro almeida (leandro.almeida@ifpb.edu.br) 
'''

__version__ = 0.1
__updated__ = '2021-05-17'
DEBUG = 0

import argparse
import datetime
import time
import random
import subprocess
import os
import threading
import math

def run(args):

    duration = int(args.duration)
    flash_events = int(args.flash_events)
    sleep_flash = (duration / flash_events) * 60

    # set the boundaries
    start = now = datetime.datetime.now()
    end   = now + datetime.timedelta(minutes=args.duration)

    # start video_client
    cmd = "nohup vagrant ssh clientVlc -c 'export DISPLAY=:1 && timeout 6000 /vagrant/host-setup/clientVlc/client.sh' > /dev/null &"
    os.system(cmd)

    # Define loadGen commands
    loadGen1 = "nohup vagrant ssh loadGen1 -c 'export DISPLAY=:1 && timeout 6000 /vagrant/code/loadGen/flashcrowd/flashcrowd.sh' > /dev/null &"
    loadGen2 = "nohup vagrant ssh loadGen2 -c 'export DISPLAY=:1 && timeout 6000 /vagrant/code/loadGen/flashcrowd/flashcrowd.sh' > /dev/null &"
    loadGen3 = "nohup vagrant ssh loadGen3 -c 'export DISPLAY=:1 && timeout 6000 /vagrant/code/loadGen/flashcrowd/flashcrowd.sh' > /dev/null &"

    while (now < end):

        # start loadGen's flashcrowd
        os.system(loadGen1)
        os.system(loadGen2)
        os.system(loadGen3)

        # sleep (random) for a new flash_event
        time.sleep(random.uniform(0,sleep_flash))

        # refresh the timer
        now = datetime.datetime.now()


def main():

    parser = argparse.ArgumentParser()
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)

    parser.add_argument('-V', '--version', action='version', version='%%(prog)s %s (%s)' % (program_version, program_build_date))
    parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
    
    # positional arguments (duration, flash_events)
    parser.add_argument("duration", type=float, help="set the duration of the experiment in minutes")    
    parser.add_argument("flash_events", type=float, help="set the number of flash events in the experiment")
    
    args = parser.parse_args()
     
    run(args)

# hook for the main function 
if __name__ == '__main__':
    main()