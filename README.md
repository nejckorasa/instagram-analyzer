<img src="https://github.com/nejckorasa/instagram-analyzer/blob/master/instagram-logo.png?raw=true" align="right">

Instagram Analyzer
=================

instagram-analyzer is a script (application) written in Python that analyzes geotags using reverse geocoding in user's instagram photos and videos. Use responsibly.


What it does
-------

### Store all instagram media data

Script loads all user's instagram media and saves it in JSON format to `insta_media_data.json`. This data includes all media metadata, including likes, location, tagged users, comments, image url-s ...

### Store all instagram location data

Script analyzes geotags and saves locations in JSON format to `insta_locations_data.json`. This data includes occurrence for each location as well as image and instagram media url-s ...

### Store all instagram countries and cities location data

Countries and cities are additionally analyzed using reverse geocoding with [Location IQ API]. Data is saved in `insta_countires_data.json` and `insta_cities_data.json` files.

### Prints occurrences for location, country and city

````
You have visited 99 different locations
You have visited 7  different countries
You have visited 32 different cities
````

### Print table view of most visited location, countries and cities

For example, when script is executed for [nejckorasa](https://www.instagram.com/nejckorasa) print for countries looks like this:

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

Script prints similar table for specific locations and cities.


Install & Usage
-------

As of now installation is not very user friendly, you need to download `insta_location_analyzer.py` and run it as:

````
$ python insta_location_analyzer.py
````


Configuration & Options
-------

#### Acquire Instagram Access Token

Go to [Pixelunion](http://instagram.pixelunion.net/), don't forget the token!

#### Acquire Location IQ Access Token

Go to [Location IQ](https://locationiq.com/), don't forget the token!

#### Paste tokens inside main method 

See the `main()` method:

```Pyhton
def main():

    analyze(
        insta_token='<INSTA_TOKEN_HERE>', 
        location_iq_token='<LOCATION_IQ_TOKEN_HERE>', 
        read_media_from_file=False, 
        countries=True)
```

> Once instagram media data is stored in JSON, you can read it from there, instead of loading it again via Instagram API (API is limited to 200 request per hour). Set `read_media_from_file=True`


FAQ
-------

#### Why does it take so long to load additional location data?

For reverse geocoding, Location IQ API is used. Free version of that API si rate limited to 1 request per second. That is why additional data loading takes '<different_location_count>' seconds.
