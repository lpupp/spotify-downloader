import requests
from os.path import exists
import json


class AccessToken:

    access_token = open('spotify_token.txt', 'r').read() if exists('spotify_token.txt') else ''
    dc = open('spotify_dc.txt', 'r').read() if exists('spotify_dc.txt') else ''

    def __init__(self):
        pass

    def access_token(self):
        return open('spotify_token.txt', 'r').read() if exists('spotify_token.txt') else ''

    def refresh(self):
        url = 'https://open.spotify.com/get_access_token'
        params = {
            'reason': 'transport',
            'productType': 'web-player'
        }
        request = requests.get(url, headers={
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en',
            'App-Platform': 'WebPlayer',
            'Connection': 'keep-alive',
            'Cookie': f'sp_dc={self.dc}',
            'Host': 'open.spotify.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Spotify-App-Version': '1.2.33.0-unknown',
            'TE': 'trailers',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0',
            #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
        }, params=params)
        request.raise_for_status()
        json = request.json()
        is_anonymous = json['isAnonymous']
        if is_anonymous:
            print('Error: Please use a valid Spotify "sp_dc" cookie.')
            exit(1)
        token = json['accessToken']

        self.access_token = token

        with open('spotify_token.txt', 'w') as file:
            file.write(token)

        return token
