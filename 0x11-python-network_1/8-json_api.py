#!/usr/bin/python3
"""
    A script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    values = {'q': ""}

    if len(sys.argv) == 2:
        letter = sys.argv[1]
        values['q'] = letter
        res = requests.post(url, data=values)
    else:
        res = requests.post(url, data=values)
    try:
        json_dict = res.json()
        if json_dict:
            print('[{}] {}'.format(json_dict.get('id'), json_dict.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
