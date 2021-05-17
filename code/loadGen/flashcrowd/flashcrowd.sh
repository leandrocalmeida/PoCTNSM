python3 /vagrant/code/loadGen/flashcrowd/flashcrowd.py -f 2,12,4 100 8 -l http://192.168.50.50/top10youtube/playlist.xspf 

#usage: flashcrowd.py [-h] [-V] [-v] [-f Rnorm,S,n] -l PLAYLIST
#                     duration flash_events
#
#positional arguments:
#  duration              set the duration of the experiment in minutes
#  flash_events          set the number of flash events in the experiment
#
#optional arguments:
#  -h, --help            show this help message and exit
#  -V, --version         show program's version number and exit
#  -v, --verbose         set verbosity level [default: None]
#  -f Rnorm,S,n, --flashcrowd Rnorm,S,n
#                        set the flashcrowd behavior, that varies with Rnorm
#                        (normal load), S (shock_level) and n (constant used in
#                        rampdown)
#  -l PLAYLIST, --playlist PLAYLIST
#                        Set the playlist for the clients