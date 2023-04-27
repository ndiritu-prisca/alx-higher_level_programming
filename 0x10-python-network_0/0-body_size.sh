#!/bin/bash
# A script that displays the size of the body of the response
curl -so /dev/null -w '%{size_download}\n' "$1"
