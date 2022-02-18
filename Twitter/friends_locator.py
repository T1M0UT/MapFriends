from functools import lru_cache

import geopy.exc
import folium
from geopy import Nominatim

geo_locator = Nominatim(user_agent='my_request')


def get_location(location_str):
    return geo_locator.geocode(location_str)

import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py
@lru_cache(maxsize=256)
def search(user: str):
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    acct = user
    if len(acct) < 1:
        raise ValueError("username length is 0")
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '200'})
    print('Retrieving', url)
    try:
        connection = urllib.request.urlopen(url, context=ctx)
        data = connection.read().decode()
    except Exception as e:
        if str(e) == 'HTTP Error 429: Too Many Requests':
            raise e
        return False

    dump_data = json.loads(data)
    with open("friends.json", 'w') as file:
        json.dump(dump_data, file, indent=6)

    data = dump_data['users']
    friends = []
    for item in data[:20]:
        try:
            location = get_location(item['location'])
            if location:
                friends.append((item["screen_name"], location.latitude, location.longitude))
                print(location)
        except geopy.exc.GeocoderUnavailable:
            continue

    map = folium.Map(location=[0, 0], zoom_start=3, tiles="Open street map")
    fg = folium.FeatureGroup(name="Friends")
    for name, lat, long in friends:
        fg.add_child(folium.Marker(location=[lat, long],
                                         popup=name,
                                         color="grey",
                                         fill_opacity=0.5))
    map.add_child(fg)
    map.save('templates/MapFriends.html')
    return True


if __name__ == "__main__":
    search(input("Enter user name: "))
