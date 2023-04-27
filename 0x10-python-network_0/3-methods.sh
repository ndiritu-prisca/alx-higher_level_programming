#!/bin/bash
# Script that takes in a URL and displays all HTTP methods a server accepts.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
