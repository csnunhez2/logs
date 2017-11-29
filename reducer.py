#!/usr/bin/env python

import sys

max_jpg_user = ""
max_count_jpg = 0
max_url = ""
max_count_url = 0

current_user = None
current_user_count = 0

current_url = None
current_url_count = 0

for line in sys.stdin:
    line = line.strip()
    datas = line.split()
    text = datas[0]
    count = int(datas[1])
    if text.startswith("c"):
        if current_user == text:
            current_user_count += count
        else:
            if current_user:
                if current_user_count > max_count_jpg:
                    max_jpg_user = current_user
                    max_count_jpg = current_user_count
            else:
                max_jpg_user = text
                max_count_jpg = count
            current_user = text
            current_user_count = count
    else:
        if current_url == text:
            current_url_count += count
        else:
            if current_url:
                if current_url_count > max_count_url:
                    max_url = current_url
                    max_count_url = current_url_count
            else:
                max_url = text
                max_count_url = count
            current_url = text
            current_url_count = count

if current_user_count > max_count_jpg:
    max_jpg_user = current_user
    max_count_jpg = current_user_count

if current_url_count > max_count_url:
    max_url = current_url
    max_count_url = current_url_count

print 'El usuario que accedio a mas archivos jpg fue: %s\tcon: %s accesos' % (max_jpg_user, max_count_jpg)
print 'La url mas visitada fue: %s\t con %s visitas' % (max_url, max_count_url)
