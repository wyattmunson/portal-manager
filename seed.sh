#!/bin/bash

echo "######## ######## ##    ##       ## #### "
echo "   ##    ##       ###   ##       ##  ##  "
echo "   ##    ##       ####  ##       ##  ##  "
echo "   ##    ######   ## ## ##       ##  ##  "
echo "   ##    ##       ##  #### ##    ##  ##  "
echo "   ##    ##       ##   ### ##    ##  ##  "
echo "   ##    ######## ##    ##  ######  #### "

echo //////////////////////////////////
echo // Installing tenji seed script //
echo //////////////////////////////////

echo "Moving to home directory"
cd ~

echo "Tenji will install the required dependencies. Enter your password when promted."

sudo apt update
sudo apt install python -y
sudo apt install git -y

# install ansible
sudo apt install software-properties-common
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install ansible

git clone https://github.com/wyattmunson/portal-manager