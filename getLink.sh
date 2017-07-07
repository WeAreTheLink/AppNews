cat $1 | grep -Po '(?<=href=")[^"]*' | awk '$0 !~ /javascript|privacidade/'
