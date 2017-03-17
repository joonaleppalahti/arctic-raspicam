#!/bin/bash
#SHELL=/bin/bash
#PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/arctic/img
#cd /home/arctic/img
DATE=$(date '+%Y-%m-%d_%H:%M:%S');
ffmpeg -r 2 -f image2 -s 1280x720 -pattern_type glob -i '*.png' -vcodec libx264 -crf 25 -pix_fmt yuv420p file:$DATE.mp4

sudo mv $DATE.mp4 /var/www/html/ArcticWeb/img
rm *.png
