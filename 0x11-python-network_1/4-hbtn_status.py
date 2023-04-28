#!/usr/bin/python3
"""
    A script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    txt = res.text
    print("Body response:")
    print("\t- type: {}".format(type(txt)))
    print("\t- content: {}".format(txt))
