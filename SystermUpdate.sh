#!/bin/bash
echo "start to update systerm automaticly!"
sudo apt update

sudo apt upgrade

sudo apt autoclean

sudo apt autoremove

sudo apt autoclean

echo "Update finished!"

