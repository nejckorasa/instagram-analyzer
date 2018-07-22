from setuptools import setup

dependencies = ['beautifultable>=0.5.2', 'requests>=2.19.1']

description = 'Analyzes user\'s Instagram location geotags to find most frequent locations, countries, cities'
with open('README.md') as f:
    long_description = f.read()

setup(
    name='instagram-analyzer',
    version='1.0.5',
    author='Nejc Korasa',
    author_email='nejc.korasa@gmail.com',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/nejckorasa/instagram-analyzer',
    download_url='https://github.com/nejckorasa/instagram-analyzer/archive/master.zip',
    packages=['instagram_analyzer'],
    license='Public domain',
    install_requires=dependencies,
    keywords=['instagram', 'location', 'download', 'media', 'photos', 'videos', 'geocoding']
)
