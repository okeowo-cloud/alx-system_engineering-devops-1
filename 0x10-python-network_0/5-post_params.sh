#!/usr/bin/env bash
# send a post request
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
