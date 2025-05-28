#!/usr/bin/bash
# Read from the file file.txt and output all valid phone numbers to stdout.

## File content sample
# 987-123-4567
# 123 456 7890
# (123) 456-7890

cat file.txt | while read -r phone; do if [[ $phone =~ ^([[:digit:]]{3}-[[:digit:]]{3}-[[:digit:]]{4}|\([[:digit:]]{3}\) [[:digit:]]{3}-[[:digit:]]{4})$ ]]; then echo $phone; fi done

while read -r phone; do if [[ $phone =~ ^([[:digit:]]{3}-[[:digit:]]{3}-[[:digit:]]{4}|\([[:digit:]]{3}\) [[:digit:]]{3}-[[:digit:]]{4})$ ]]; then echo $phone; fi done < file.txt

grep -oE '^([[:digit:]]{3}-[[:digit:]]{3}-[[:digit:]]{4}|\([[:digit:]]{3}\) [[:digit:]]{3}-[[:digit:]]{4})$' file.txt

grep -oP '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt

awk '$0 ~ /^([[:digit:]]{3}-|\([[:digit:]]{3}\) )[[:digit:]]{3}-[[:digit:]]{4}$/ { print $0 }' file.txt