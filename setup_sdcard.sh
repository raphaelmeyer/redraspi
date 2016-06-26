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
  echo "!"
  echo "! '${DEV}' is not a device path of form /dev/sdX"
  echo "!"
  exit 1
fi

DEV_NAME=${BASH_REMATCH[1]}
REMOVABLE=$(cat /sys/block/${DEV_NAME}/removable)

if [[ ${REMOVABLE} -ne 1 ]] ; then
  echo "!"
  echo "! '${DEV}' is not a removable device"
  echo "!"
  exit 1
fi

################################################################

echo "#"
echo "# Partition '${DEV}'"
echo "#"

sudo parted -s ${DEV} -- mklabel msdos
sudo parted -s ${DEV} -- mkpart primary fat32 2048s 100.0MiB
sudo parted -s ${DEV} -- mkpart primary ext2 100.0MiB -1s

BOOT=${DEV}1
ROOT=${DEV}2

################################################################

echo "#"
echo "# Format boot partition '${BOOT}'"
echo "#"

sudo mkfs.vfat ${BOOT}

echo "#"
echo "# Format root partition '${ROOT}'"
echo "#"

sudo mkfs.ext4 -F ${ROOT}

################################################################

FILE=ArchLinuxARM-rpi-2-latest.tar.gz
FOLDER=${DIR}/download

mkdir -p ${FOLDER}

if [[ -e ${FOLDER}/${FILE} ]] ; then
  echo "#"
  echo "# '${FILE}' already downloaded"
  echo "#"
else
  echo "#"
  echo "# Download archlinux ARM for raspberry pi 2"
  echo "#"
  wget http://archlinuxarm.org/os/${FILE} -P ${FOLDER}
fi

################################################################

MOUNT=${DIR}/mount

mkdir -p ${MOUNT}/boot
mkdir -p ${MOUNT}/root

cd ${DIR}

echo "#"
echo "# As root (not sudo) do:"
echo "#"
echo "# \$ cd ${DIR}"
echo "#"
echo "# \$ mount ${BOOT} mount/boot"
echo "# \$ mount ${ROOT} mount/root"
echo "# \$ bsdtar -xpf download/${FILE} -C mount/root"
echo "# \$ sync"
echo "# \$ mv mount/root/boot/* mount/boot"
echo "#"
echo "# \$ cp setup_arch.sh mount/home/alarm/"
echo "# \$ chown alarm mount/home/alarm/setup_arch.sh"
echo "#"
echo "# \$ umount mount/boot"
echo "# \$ umount mount/root"

