#!/bin/bash

./generateSites.sh  | xargs -n1 wget -k -nc -r --no-parent -A html
