# redraspi

Red Ras Pi

[![Build Status](https://travis-ci.org/raphaelmeyer/redraspi.svg?branch=master)](https://travis-ci.org/raphaelmeyer/redraspi)


## Setup

- Pepare the sd card:

        host$ ./setup_sdcard.sh [/dev/sdX]

  See https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-3 for reference

- Start the raspberry pi
- SSH to raspberry pi with user _alarm_ and password _alarm_
- Change to root. The root password is root:

        alarmpi$ su

- Execute the setup script:

        alarmpi$ /root/setup_arch.sh

