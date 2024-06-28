#!/bin/bash
set -e
#
# Ubuntu 22.04 LTS minimal
# Scrtip for setting Django apps
# Update from install_ubuntu_minimal_20.04.sh
# 28/06/2024
#

# Remove old packages and make cleaning of the system.
sudo apt-get update
sudo apt-get autoremove
sudo apt-get autoclean

# Install network tools
sudo apt-get -y install net-tools
sudo apt-get -y install git
sudo apt-get -y install curl
sudo apt-get -y install nano

# Install Python development tools
sudo apt-get -y install python3
sudo apt-get -y install python3-dev
sudo apt-get -y install python3-venv
sudo apt-get -y install python3-pip


# -------------------------



sudo ubuntu-drivers autoinstall

sudo apt-get install -y openssh-server
sudo systemctl enable ssh --now
sudo systemctl start ssh
#sudo apt-get install -y wireshark-qt
#sudo apt-get install -y hping3
#sudo apt-get install -y fping

# Install common apps
sudo apt-get install -y mlocate
sudo apt-get install -y locate
sudo apt -y install -y git
sudo apt-get install -y ffmpeg
sudo apt-get install -y dialog

# Install essential tools that are not part of package.
sudo apt-get install -y build-essential
sudo apt-get install -y cmake
sudo apt-get install -y libgtk2.0-dev
sudo apt-get install -y libusb-1.0
sudo apt install -y libssl-dev
sudo apt install -y libffi-dev

# C/C++
sudo apt install -y gcc

# Python environments
sudo apt-get install -y python3-dev
sudo apt-get install -y python3-venv
sudo apt-get install -y python3-pip
sudo apt-get install -y python-tk

