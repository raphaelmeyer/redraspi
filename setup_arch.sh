#!/bin/bash

DEV=/dev/sdg

if [ ! -z $1 ] ; then
  DEV=$1
fi

if [[ ! ${DEV} =~ ^\/dev\/(sd[a-z])$ ]] ; then
  echo "'${DEV}' is not a device path of form /dev/sdX"
  exit 1
fi

DEV_NAME=${BASH_REMATCH[1]}
REMOVABLE=$(cat /sys/block/${DEV_NAME}/removable)

if [[ ${REMOVABLE} -ne 1 ]] ; then
  echo "'${DEV}' is not a removable device"
  exit 1
fi

echo "Partitioning '${DEV}'"


