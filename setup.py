from setuptools import setup

setup(
    name='instagram-analyzer',
    version='1.0.1',
    author='Nejc Korasa',
    author_email='nejc.korasa@gmail.com',
    description='Analyzes user\'s Instagram location geotags to find most frequent locations, countries, cities',
    long_desription='instagram-analyzer is an application written in Python that analyzes geotags using reverse '
                    'geocoding in user\'s Instagram photos and videos. It provides the data of specific locations, '
                    'countries and cities you\'ve visited so far, as well as how many times and which Instagram posts '
                    'match the location.',
    url='https://github.com/nejckorasa/instagram-analyzer',
    download_url='https://github.com/nejckorasa/instagram-analyzer/archive/master.zip',
    packages=['instagram_analyzer'],
    license='Public domain',
    install_requires=[
        'beautifultable>=0.5.2',
        'requests>=2.19.1'
    ],
    keywords=['instagram', 'location', 'download', 'media', 'photos', 'videos', 'geocoding']
)
