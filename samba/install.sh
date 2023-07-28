#!/bin/bash

echo "Installing Samba..."

sudo apt-get install samba samba-common-bin -y

mkdir /home/mainframe/shared
sudo nano /etc/samba/smb.conf

# create a user for mainframe
sudo smbpasswd -a mainframe

# restart smbd
sudo systemctl restart smbd