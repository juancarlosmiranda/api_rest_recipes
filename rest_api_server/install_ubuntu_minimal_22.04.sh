#!/bin/bash
set -e
#
# Ubuntu 22.04 LTS minimal
# Script for setting Django apps
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
