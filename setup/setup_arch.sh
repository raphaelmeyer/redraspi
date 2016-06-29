#!/bin/bash

if [[ $(uname -n) != "alarmpi" ]] ; then
  echo "This is not an archlinux ARM on a raspberry pi"
  exit 1
fi

if [[ ! $(uname -m) =~ ^arm.*$ ]] ; then
  echo "This is not an archlinux ARM on a raspberry pi"
  exit 1
fi

if [[ $EUID -ne 0 ]] ; then
  echo "Run this script as root"
  exit 1
fi

pacman -Syu --noconfirm
pacman -Sy --noconfirm sudo \
  cmake \
  fakeroot \
  gcc \
  git \
  make \
  pwgen \
  python \
  python-pip \
  python-pyserial \
  python-setuptools \
  wget

################################################################
cat >> /boot/config.txt <<EOF

device_tree_param=spi=on
dtparam=i2c_arm=on

start_file=start_x.elf
fixup_file=fixup_x.dat

EOF
################################################################
cat >> /etc/modules-load.d/raspberrypi.conf <<EOF

i2c-dev
i2c-bcm2708

EOF
################################################################
cat > /etc/sudoers.d/wheel <<EOF
# allow members of group wheel to execute any command
%wheel ALL=(ALL) ALL

EOF
################################################################

useradd -m -G wheel -s /bin/bash pi

echo "#"
echo "# Set password for user 'pi'"
echo "#"
passwd pi

echo root:`pwgen -y -s 32 1` | chpasswd
echo alarm:`pwgen -y -s 32 1` | chpasswd

gpasswd -d alarm wheel

wget -P /tmp https://aur.archlinux.org/cgit/aur.git/snapshot/python-raspberry-gpio.tar.gz
(
  cd /tmp
  tar zxf python-raspberry-gpio.tar.gz
  chown pi:pi -R python-raspberry-gpio
  cd python-raspberry-gpio
  su -c makepkg pi
  pacman -U --noconfirm python-raspberry-gpio-*.pkg.tar.xz
)

pip install python-twitter

rm -- "$0"

shutdown -r now

