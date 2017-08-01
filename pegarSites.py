#/usr/bin/env python3

import subprocess

p = subprocess.Popen("./generateSites.sh",stdout=subprocess.PIPE)
for line in p.stdout.readlines():
  k = subprocess.call(["wget","-k","-nc","-r","--no-parent","-A","html",line])



#!/bin/bash

#./generateSites.sh  | xargs -n1 wget -k -nc -r --no-parent -A html
