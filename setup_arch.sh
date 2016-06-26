#!/bin/bash

################################################################

DEV=/dev/sdg

################################################################

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

################################################################

if [ ! -z $1 ] ; then
  DEV=$1
fi

if [[ ! ${DEV} =~ ^\/dev\/(sd[a-z])$ ]] ; then
  echo "! '${DEV}' is not a device path of form /dev/sdX"
  exit 1
fi

DEV_NAME=${BASH_REMATCH[1]}
REMOVABLE=$(cat /sys/block/${DEV_NAME}/removable)

if [[ ${REMOVABLE} -ne 1 ]] ; then
  echo "! '${DEV}' is not a removable device"
  exit 1
fi

################################################################

echo "# Partition '${DEV}'"

sudo parted -s ${DEV} -- mklabel msdos
sudo parted -s ${DEV} -- mkpart primary fat32 2048s 100.0MiB
sudo parted -s ${DEV} -- mkpart primary ext2 100.0MiB -1s

BOOT=${DEV}1
ROOT=${DEV}2

################################################################

echo "# Format boot partition '${BOOT}'"

sudo mkfs.vfat ${BOOT}

echo "# Format root partition '${ROOT}'"

sudo mkfs.ext4 -F ${ROOT}

################################################################

MOUNT=${DIR}/mount

mkdir -p ${MOUNT}/boot
mkdir -p ${MOUNT}/root

################################################################

mkdir -p ${DIR}/download

FILE=ArchLinuxARM-rpi-2-latest.tar.gz
FOLDER=${DIR}/download

if [[ -e ${FOLDER}/${FILE} ]] ; then
  echo "# '${FILE}' already downloaded"
else
  echo "# Download archlinux ARM for raspberry pi 2"
  wget http://archlinuxarm.org/os/${FILE} -P ${FOLDER}
fi

################################################################

echo "# Extract file system"

sudo mount ${BOOT} ${MOUNT}/boot
sudo mount ${ROOT} ${MOUNT}/root

sudo su -c bsdtar -xpf ${FOLDER}/${FILE} -C ${MOUNT}/root
sudo sync

mv ${MOUNT}/root/* ${MOUNT}/boot

sudo umount ${MOUNT}/boot
sudo umount ${MOUNT}/root

