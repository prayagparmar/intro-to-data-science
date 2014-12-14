__author__ = 'prayagparmar'
import json

import requests


def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.

    data = requests.get(url).text
    data = json.loads(data)

    # <topartists country="Spain">
    # <artist rank="1">
    # <name>Coldplay</name>
    # <playcount>3199</playcount>
    #     <mbid>cc197bad-dc9c-440d-a5b5-d52ba2e14234</mbid>
    #     <url>http://www.last.fm/music/Coldplay</url>
    #     <streamable>1</streamable>
    #     <image size="small">...</image>
    #     <image size="medium">...</image>
    #     <image size="large">...</image>
    #   </artist>
    #     ...
    # </topartists>

    # return the top artist in Spain
    return data['topartists']['artist'][0]['name']


if __name__ == "__main__":
    url = 'Get your own API key from http://www.last.fm/api/show/geo.getTopArtists'
    print api_get_request(url)


