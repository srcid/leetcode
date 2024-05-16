#!/usr/bin/awk -f

BEGIN {
    i = 0;
    flag = 1;
}

$0 ~ /^$/ {
    flag = 1;
    next;
}

flag {
    flag = 0;
    print "\n"++i;
    next;
}

! flag {
    print $0
}