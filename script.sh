sudo sh -c 'echo 1 >  /proc/sys/vm/drop_caches'
sudo sh -c 'echo 2 >  /proc/sys/vm/drop_caches'
sudo sh -c 'echo 3 >  /proc/sys/vm/drop_caches'
sudo swapoff -a
sudo swapon -a
echo " echo 3 >  /proc/sys/vm/drop_caches"
free -m
free -h
sudo ls -al
du -sch ~/.bashrc /tmp $XDG_RUNTIME_DIR 
sleep 30
clear
