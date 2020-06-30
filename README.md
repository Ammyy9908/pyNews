<h1>LoremipsumPy</h1>
## This Package Returns Latest and top News Headlines from different sources of News by taking some arguments

## Installation

Run the follwoing to install

$pip install pyNewsApi

## Usage

>>from pyNewsApi import PYNEWS

>>p = PYNEWS()<br/>

## Get News by country codes
>>data = p.get_get_headlines_by_country(countrycode='in') or p.get_headlines_by_country('in')<br/>
>>print(data)<br/>

## Get News by news provider name

>>data = p.get_headline_by_source(source='techradar') or p.p.get_headline_by_source('techradar')<br/>
>>print(data)<br/>

## Get News by category and country name

>>data = p.get_head_by_cat_country(cat='technology',country='in') or p.get_head_by_cat_country('technology','in')<br/>
>>print(data)<br/>

## Get Top headlines by giving query

>>data = p.get_top_headlines_about(query='apple') or p.get_top_headlines_about('apple')<br/>
>>print(data)<br/>


# Get all news from all sources no need to take any arguments

>>data = p.get_from_all_sources()<br/>
>>print(data)<br/>

# Get News by languages

>>data = p.get_by_lang(lang='fr') or p.get_by_lang('fr')<br/>
>>print(data)

# get help for the module
>> p.get_help()

# get all supported languages
>> p.display_langauges()

# get country codes
>>p.display_country()

# get categories 
>>p.display_catcty()
