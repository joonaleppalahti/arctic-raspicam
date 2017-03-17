#!/bin/bash
sudo find /var/www/html/ArcticWeb/img/ -maxdepth 1 -mmin +5 -type f -exec mv "{}" /var/www/html/ArcticWeb/img/old/ \;
