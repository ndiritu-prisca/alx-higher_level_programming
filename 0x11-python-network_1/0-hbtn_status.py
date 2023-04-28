#!/usr/bin/python3
"""
    A script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib import request


if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        res = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(res)))
        print("\t- content: {}".format(res))
        print("\t- utf8 content: {}".format(res.decode(encoding='utf-8')))
