#!/bin/bash
# takes in a URL and displays all HTTP methods
curl -sI "OPTIONS" "$1" | grep Allow | cut -c 8-
