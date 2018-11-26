#!/bin/sh

xwd -name $1 | convert - tmp.jpg
#xwd -name AssaultCube -out tmp.xwd
#convert tmp.xwd tmp.jpg
