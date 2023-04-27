#!/bin/bash
#Takes in a URL as an argument, sends a GET request to the URL & displays body
curl -s -H "X-School-User-Id: 98" "$1"
