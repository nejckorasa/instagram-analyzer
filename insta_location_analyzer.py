import requests
import json
import os.path
import time
from beautifultable import BeautifulTable

# Insta constans

INSTA_TOKEN: str = None
INSTA_MEDIA_URI: str = 'https://api.instagram.com/v1/users/self/media/recent'

INSTA_MEDIA_JSON_FILE_NAME = './insta_media_data.json'
INSTA_LOCATIONS_JSON_FILE_NAME = './insta_locations_data.json'
INSTA_COUNTIRES_JSON_FILE_NAME = './insta_countires_data.json'
INSTA_CITIES_JSON_FILE_NAME = './insta_cities_data.json'

# Geo constans

LOCATION_IQ_TOKEN: str = None
LOCATION_IQ_URI: str = 'https://us1.locationiq.org/v1/reverse.php'

# Other constants

ANALYZE_COUNTRIES = False

# Data

insta_media_data: dict = {}

def load_insta_media():

    print('Loading Instagram media [', end='', flush=True)

    next_max_id: str = None
    next_page: bool = True

    while next_page:
        media = get_recent_media(next_max_id=next_max_id)
        next_max_id = media['next_max_id']
        next_page = media['next_page']
        print("#", end="", flush=True)

    print ('] [DONE] - Media items size: ', len(insta_media_data))


def read_insta_media():

    global insta_media_data

    if not os.path.isfile(INSTA_MEDIA_JSON_FILE_NAME):
        raise ValueError("Media has not yet been loaded, file: " + INSTA_MEDIA_JSON_FILE_NAME + " does not exist") 

    with open(INSTA_MEDIA_JSON_FILE_NAME) as f:
        insta_media_data = json.loads(f.read())


def store_insta_media():

    print('Saving media data to file ', end='', flush=True)
    with open(INSTA_MEDIA_JSON_FILE_NAME, "wb") as f:
        f.write(json.dumps(insta_media_data).encode("utf-8"))
    print ('[DONE]')


def get_recent_media(next_max_id: str = None):

    # set count to 2000 to get max data per request    
    payload: dict = {
        'access_token': INSTA_TOKEN, 
        'max_id': next_max_id,
        'count': 2000
        }

    response: dict = requests.get(INSTA_MEDIA_URI, params=payload).json()

    if 'code' in response and response['code'] != 200:
        raise ValueError("Error while calling Instagram API, error_type: " 
            + response['error_type'] + ", message: " 
            + response['error_message'])

    for item in response['data']:
        insta_media_data[item['id']] = item
        
    next_max_id = response['pagination'].get('next_max_id', None)
    
    return {'next_max_id' : next_max_id,  'next_page' : next_max_id is not None}


def analyze_locations():

    print('Analyzing locations ...')
    
    locations: dict = {}
    countries: dict = {}
    cities: dict = {}

    for key in insta_media_data.keys():
        media_item = insta_media_data[key]
        location = media_item['location']

        if location is not None:
            location_id = location['id']
            if location_id in locations:
                locations[location_id]['count'] += 1
                locations[location_id]['media_items'].append(
                    {
                        'id': media_item['id'], 
                        'image': media_item['images']['standard_resolution']['url'], 
                        'link': media_item['link']
                    }
                )
            else:
                location['count'] = 1
                location['media_items'] = [
                    {
                        'id': media_item['id'], 
                        'image': media_item['images']['standard_resolution']['url'], 
                        'link': media_item['link']
                    }
                ]
                locations[location_id] = location

    if ANALYZE_COUNTRIES:
        
        print('Loading country data (should take about', len(locations) , 'seconds) [', end='', flush=True)
        for key in locations:

            location = locations[key]
            media_items = location['media_items']

            # Load additional data
            country_data = load_country_data(location)

            # Extract additional data
            country = country_data['address']['country']
            city: str = None
            if 'city' in country_data['address']:
                city = country_data['address']['city']
            elif 'town' in country_data['address']:
                city = country_data['address']['town']
            elif 'village' in country_data['address']:
                city = country_data['address']['village']
            else:
                city = 'Other'
            
            location['city'] = city
            location['additional_data'] = country_data

            # Fill countries
            if country in countries:
                countries[country]['count'] += 1
                countries[country]['media_items'] += media_items
            else:
                countries[country] = {
                    'count': 1,
                    'media_items': [media_items]
                }
            
            # Fill cities
            if city in cities:
                cities[city]['count'] += 1
                cities[city]['media_items'] += media_items
            else:
                cities[city] = {
                    'count': 1,
                    'media_items': [media_items]
                }
            
            # Location IQ rate limit (1 request per second)
            print("#", end="", flush=True)
            time.sleep(1)
        
        print('] [DONE]')

    # Store & print location data
    store_locations_data(locations, countries, cities)
    print_locations_data(locations, countries, cities)


def store_locations_data(locations, countries, cities):
    
    with open(INSTA_LOCATIONS_JSON_FILE_NAME, "wb") as f:
        f.write(json.dumps(locations).encode("utf-8"))

    with open(INSTA_COUNTIRES_JSON_FILE_NAME, "wb") as f:
        f.write(json.dumps(countries).encode("utf-8"))

    with open(INSTA_CITIES_JSON_FILE_NAME, "wb") as f:
        f.write(json.dumps(cities).encode("utf-8"))


def print_locations_data(locations, countries, cities):
    
    rank: int = 1

    # Sort by occurrences
    sorted_locations = sorted(locations.items(), key=lambda i: i[1]['count'], reverse=True)
    sorted_countries = sorted(countries.items(), key=lambda i: i[1]['count'], reverse=True)
    sorted_cities = sorted(cities.items(), key=lambda i: i[1]['count'], reverse=True)

    print('You have visited', len(locations), 'different locations')
    print('You have visited', len(countries), 'different countries')
    print('You have visited', len(cities), 'different cities')

    # Pretty print locations
    print('Locations: \n')
    locations_table = BeautifulTable()
    locations_table.column_headers = ['rank', 'location', 'occurrences']
    locations_table.column_alignments['location'] = BeautifulTable.ALIGN_LEFT
    
    rank = 1
    for location in sorted_locations:
        locations_table.append_row([rank, location[1]['name'], location[1]['count']])
        rank += 1

    print(locations_table)

    # Pretty print countries
    print('Countries: \n')
    countries_table = BeautifulTable()
    countries_table.column_headers = ['rank', 'country', 'occurrences']
    countries_table.column_alignments['country'] = BeautifulTable.ALIGN_LEFT
    
    rank = 1
    for country in sorted_countries:
        countries_table.append_row([rank, country[0], country[1]['count']])
        rank += 1

    print(countries_table)

    # Pretty print cities
    print('Cities: \n')
    cities_table = BeautifulTable()
    cities_table.column_headers = ['rank', 'city', 'occurrences']
    cities_table.column_alignments['city'] = BeautifulTable.ALIGN_LEFT
    
    rank = 1
    for city in sorted_cities:
        cities_table.append_row([rank, city[0], city[1]['count']])
        rank += 1

    print(cities_table)


def load_country_data(location):

    payload: dict = {
        'key': LOCATION_IQ_TOKEN, 
        'lat': location['latitude'],
        'lon': location['longitude'],
        'format': 'json'
        }

    return requests.get(LOCATION_IQ_URI, params=payload).json()


def analyze(insta_token, location_iq_token, read_media_from_file=False, analyze=True, countries=False):

    # Set tokens

    if insta_token is None:
       raise ValueError("Insta token must be present, set insta_token parameter")  

    global INSTA_TOKEN
    INSTA_TOKEN = insta_token

    if countries and location_iq_token is None:
        raise ValueError("Location iq token must be present, set location_iq_token parameter")  

    global LOCATION_IQ_TOKEN
    LOCATION_IQ_TOKEN = location_iq_token

    # Prepare data

    if read_media_from_file:
        read_insta_media()
    else:
        load_insta_media()
        store_insta_media()

    # Analyze

    global ANALYZE_COUNTRIES
    ANALYZE_COUNTRIES = countries

    if analyze:
        analyze_locations()

def main():

    analyze(
        insta_token='<INSTA_TOKEN_HERE>', 
        location_iq_token='<LOCATION_ID_TOKEN_HERE>', 
        read_media_from_file=False, 
        countries=True)


if __name__ == '__main__':
    main()
