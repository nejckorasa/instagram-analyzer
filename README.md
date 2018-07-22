<img src="https://raw.githubusercontent.com/nejckorasa/instagram-analyzer/master/presentation/instagram-logo.png?raw=true" align="right">

Instagram Analyzer
=================

[![PyPI](https://img.shields.io/pypi/v/instagram-analyzer.svg)](https://pypi.org/project/instagram-analyzer/) ![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
 [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Analyze%20Instagram%20location%20tags%20to%20se%20what%20cities%2C%20countries%20you%20visited&url=https://github.com/nejckorasa/instagram-analyzer&via=github&hashtags=python,instagram,location,geocoding,github,geotagging,developers)

instagram-analyzer is an application written in Python that analyzes geotags using reverse geocoding in user's Instagram photos and videos. 

It provides the data of specific locations, countries and cities you've visited so far, as well as how many times and which Instagram posts match the location.

Use responsibly.

What it does
-------

### :round_pushpin: Store all instagram media data :camera:

Application loads all user's instagram media and saves it in JSON format to `insta_media_data.json`. This data includes all media metadata, including likes, location, tagged users, comments, image url-s ...

### :round_pushpin: Store all instagram location data :bar_chart:

Analyzes geotags and saves locations in JSON format to `insta_locations_data.json`. This data includes occurrence for each location as well as image and instagram media url-s ...

### :round_pushpin: Store all instagram countries and cities location data :open_file_folder:

Countries and cities are additionally analyzed using reverse geocoding with [LocationIQ API](https://locationiq.com). Data is saved in `insta_countires_data.json` and `insta_cities_data.json` files.

### :round_pushpin: Prints occurrences for location, country and city :airplane:

````
You have visited 99 different locations
You have visited 7  different countries
You have visited 32 different cities
````

### :round_pushpin: Print table view of most visited location, countries and cities :earth_africa:

For example, when executed for [nejckorasa](https://www.instagram.com/nejckorasa) print for countries looks like this:

````
Countries: 

+------+-----------------+-------------+
| rank | country         | occurrences |
+------+-----------------+-------------+
|  1   | Slovenia        |     51      |
+------+-----------------+-------------+
|  2   | The Netherlands |     12      |
+------+-----------------+-------------+
|  3   | Spain           |      8      |
+------+-----------------+-------------+
|  4   | Poland          |      8      |
+------+-----------------+-------------+
|  5   | Russia          |      7      |
+------+-----------------+-------------+
|  6   | Croatia         |      7      |
+------+-----------------+-------------+
|  7   | Hungary         |      6      |
+------+-----------------+-------------+

````

Similar tables are printed for specific locations and cities.


Install
-------

To install instagram-analyzer:
```bash
$ pip install instagram-analyzer
```

To update instagram-analyzer:
```bash
$ pip install instagram-analyzer --upgrade
```

Usage
-------

Once installed, import it, configure it and run it:

```Python
from instagram_analyzer import InstaAnalyzer

InstaAnalyzer(
    insta_token='<INSTAGRAM_TOKEN_HERE>',
    location_iq_token='<LOCATION_IQ_TOKEN_HERE>').run()
```


Before you run it, see [Configuration & Options](https://github.com/nejckorasa/instagram-analyzer/blob/master/README.md#configuration--options)


Configuration & Options
-------

### Acquire Tokens

##### Acquire Instagram Access Token

Go to [Pixelunion](http://instagram.pixelunion.net/), generate token, don't forget the token!

##### Acquire Location IQ Access Token

Go to [Location IQ](https://locationiq.com/), sign up, get the token, don't forget the token!

### Configure and run

Create `InstaAnalyzer` instance with token values.

```Python
analyzer = InstaAnalyzer(
    insta_token='<INSTAGRAM_TOKEN_HERE>',
    location_iq_token='<LOCATION_IQ_TOKEN_HERE>')
analyzer.read_media_from_file = False
analyzer.run()
```

> Once instagram media data is stored in JSON, you can read it from there, instead of loading it again via Instagram API (API is limited to 200 request per hour). Set `analyzer.read_media_from_file = True`


### Options

- `location_iq_token` is optional. If not set only basic location analysis will be run and saved to file.
- Once `InstaAnalyzer` has been run all data is available to access:

```Python
# Configure InstaAnalyzer
analyzer = InstaAnalyzer(
    insta_token='<INSTAGRAM_TOKEN_HERE>',
    location_iq_token='<LOCATION_IQ_TOKEN_HERE>')
    
# Run InstaAnalyzer    
analyzer.run()

# Access cities, countries and location data
cities = analyzer.cities
countires = analyzer.countires
locations = analyzer.locations

# Access instagram media data
instagram_media = analyzer.insta_media_data

# Print locations later
analyzer.print_locations()
```
    


Stored data examples
-------

When executed for [nejckorasa](https://www.instagram.com/nejckorasa) data for one country item (Spain) looks like this:

```Json
"Spain": {
    "count": 8,
    "media_items": [
      [
        {
          "id": "<post_id>",
          "image": "https://scontent.cdninstagram.com/vp/e7705068da5e289f5e44c0c396c08f74/5BD54C95/t51.2885-15/sh0.08/e35/p640x640/36149213_609452269436842_8766778259800064000_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
          "link": "https://www.instagram.com/p/Bkh3-KfgxL9/"
        }
      ],
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/2b239894a363f6bbe93d604ab2cdfa8a/5BE953CD/t51.2885-15/sh0.08/e35/p640x640/33941046_171665143683479_8766885676932136960_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/Bj7Uj56gxBs/"
      },
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/9d7003f674af9ca05accf9961df893a6/5BE28FDA/t51.2885-15/sh0.08/e35/p640x640/33120615_197967877520708_8731075699906969600_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/Bjmp-6bAYus/"
      },
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/1e7ca79fc44823ff3ef8b24e6dd55e61/5BD1E8C3/t51.2885-15/sh0.08/e35/p640x640/33608474_597094857325212_724188974242856960_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/BjR_9lpAqpc/"
      },
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/1b046c05b1cbe9708f57f5e591b68d1c/5BD8E039/t51.2885-15/sh0.08/e35/p640x640/32947036_172314443452529_4611639929133334528_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/BjNEIwiA6Py/"
      },
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/5ac0e05fb60700cba4c41d6d1216eb5b/5BC8A9DB/t51.2885-15/e15/10802615_318814311644936_1896556761_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/vdWuHBkwuY/"
      },
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/40620d8f5e7e01a546e2b958d18bd42a/5BE9E99F/t51.2885-15/e15/10784835_319487204924131_388050040_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/vYybQyEwiA/"
      },
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/b733c0bdf312ee5c21bb3fd6148e6221/5BE263EA/t51.2885-15/e15/10802986_691193854310946_2042620114_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/vc9ZFakwrq/"
      },
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/875bff08c310444273eae90a67e525dd/5BC8F29F/t51.2885-15/e15/928044_671144066338855_1666493611_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/vaWbQLEwqX/"
      }
    ]
  }
```
Of course, `<post_id>` will be an actual post ID.

Data for cities is almost the same. For specific location one location item looks like this:

````Json
"236678869": {
    "latitude": 45.7925,
    "longitude": 15.1647,
    "name": "Novo Mesto",
    "id": 236678869,
    "count": 4,
    "media_items": [
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/6941d16b164ec488dd3a303004344f78/5BE40DE8/t51.2885-15/sh0.08/e35/p640x640/31270267_1592482480868234_8257495365851283456_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/Bij24yzAdHB/"
      },
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/3189c0f2e5931f47b4506046ff26afff/5BDB6109/t51.2885-15/e15/10724200_1496985983889525_746072573_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/uDDPHekwtW/"
      },
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/fbf31b5c410c9036ce43862012249d02/5BEC3F36/t51.2885-15/e15/10488704_250740985124191_1862853011_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/q94LWMkwlk/"
      },
      {
        "id": "<post_id>",
        "image": "https://scontent.cdninstagram.com/vp/27c6681709c7b71fc86d8477c11d2b88/5BCAD041/t51.2885-15/e15/10013254_641464529259998_1091484863_n.jpg?efg=eyJ1cmxnZW4iOiJ1cmxnZW5fZnJvbV9pZyJ9",
        "link": "https://www.instagram.com/p/mKDvsikwsC/"
      }
    ],
    "city": "Novo mesto",
    "additional_data": {
      "place_id": "113385772",
      "licence": "\u00a9 LocationIQ.org CC BY 4.0, Data \u00a9 OpenStreetMap contributors, ODbL 1.0",
      "osm_type": "way",
      "osm_id": "167321715",
      "lat": "45.7897769",
      "lon": "15.1680662",
      "display_name": "Krka, Novo mesto, Jugovzhodna Slovenija, 8000, Slovenia",
      "address": {
        "suburb": "Krka",
        "town": "Novo mesto",
        "state_district": "Jugovzhodna Slovenija",
        "postcode": "8000",
        "country": "Slovenia",
        "country_code": "si"
      },
      "boundingbox": [
        "45.7858017",
        "45.7927137",
        "15.1640388",
        "15.1725268"
      ]
    }
  }
````

Notice `additional_data` field, this data is populated using [Location IQ API](https://locationiq.com)


FAQ
-------

#### Why does it take so long to load additional location data?

For reverse geocoding, Location IQ API is used. Free version of that API si rate limited to 1 request per second. That is why additional data loading takes `<different_location_count>` seconds.


Contributing
-------

Pull requests are welcome, [Show your ❤ with a ★](https://github.com/nejckorasa/instagram-analyzer/stargazers)