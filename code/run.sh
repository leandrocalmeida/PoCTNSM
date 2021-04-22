#start INT collector in sinkServer
#nohup vagrant ssh sinkServer -c 'timeout 600 sudo /vagrant/code/receive_int.py' > /dev/null &

#Start INT Traffic in dashServer
#nohup vagrant ssh dashServer -c 'timeout 600 sudo /vagrant/code/send_int.py 192.168.50.52' > /dev/null &

#Start clientVlc
nohup vagrant ssh clientVlc -c 'export DISPLAY=:1 && timeout 6000 /vagrant/host-setup/clientVlc/client.sh' > /dev/null &

#Start loadGens
nohup vagrant ssh loadGen1 -c 'export DISPLAY=:1 && timeout 6000 /vagrant/code/loadGen/loadGen1/mix_periodic_dash1.sh' > /dev/null &
nohup vagrant ssh loadGen2 -c 'export DISPLAY=:1 && timeout 6000 /vagrant/code/loadGen/loadGen2/mix_periodic_dash2.sh' > /dev/null &
nohup vagrant ssh loadGen3 -c 'export DISPLAY=:1 && timeout 6000 /vagrant/code/loadGen/loadGen3/mix_periodic_dash3.sh' > /dev/null &