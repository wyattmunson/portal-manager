#!/bin/bash


echo ""
echo "========================================="
echo "   ___ _    "
echo "  / __| |     SEED PROVISIONER"
echo " | (_ | |__       Debian"
echo "  \___|____|"
echo "Grayrock Labs"
echo "========================================="
echo ""



cd ~
sudo apt update
sudo apt install ansible -y
sudo apt install git -y
git clone https://github.com/wyattmunson/portal-manager 