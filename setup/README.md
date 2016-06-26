# redraspi setup

## SD card setup

- Pepare the sd card:

        host$ ./setup_sdcard.sh [/dev/sdX]

  See https://archlinuxarm.org/platforms/armv8/broadcom/raspberry-pi-3 for reference

- Finalize the sd card setup as root

## Raspberry PI configuration

- Start the raspberry pi
- SSH to raspberry pi with user _alarm_ and password _alarm_
- Change to root. The root password is root:

        alarmpi$ su

- Execute the setup script:

        alarmpi$ /root/setup_arch.sh

