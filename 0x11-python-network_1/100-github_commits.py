#!/usr/bin/python3
"""
    A script that takes 2 args to list 10 commits from most recent to oldest
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits"\
          .format(argv[2], argv[1])
    res = requests.get(url)
    json_dict = res.json()
    for i in range(10):
        print("{}: {}".format(json_dict[i].get("sha"),
              json_dict[i].get("commit").get("author").get("name")))
