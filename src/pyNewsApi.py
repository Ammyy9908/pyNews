import requests

class PYNEWS:
    '''This Class Generates
    News about topics,country and from
    different sources'''
    def __init__(self):
        self.url = ""
        self.country_codes = "ae ar at au be bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp kr lt lv ma mx my ng nl no nz ph pl pt ro rs ru sa se sg si sk th tr tw ua us ve za".split(" ")
        self.secret_key = '77fcc3b8e0e44caa9df1f04080fb1fdf'
        self.sources = ['abc-news','google-news-in',
        'bbc-news','bbc-sport','buzzfeed','cbc-news',
        'cnn','espn','fox-news','google-news','hacker-news'
        ,'national-geographic','techcrunch','techradar','the-times-of-india',
         'time','usa-today','wired']
        self.cat = ['business','entertainment', 'general', 'health', 'science', 'sports', 'technology']
        self.lang = 'ar de en es fr he it nl no pt ru se ud zh'.split(' ')

    def display_country_codes(self):
        '''returns a list of country codes'''
        codes = self.country_codes.split(" ")
        return codes

    def display_sources(self):
        '''returns list of sources'''
        return self.sources

    def get_headlines_by_country(self,countrycode='in'):
        ''' This method gives
        headlines by country code name as a argument
        and return a json response'''
        if countrycode in self.country_codes:
            self.url = 'https://newsapi.org/v2/top-headlines?country='+countrycode+'&apiKey='+self.secret_key
            try:
                response = requests.get(self.url).json()
                headlines = response["articles"]
                return headlines
            except:
                print("Internet Required!")
        else:
            return "Invalid country code. See all country codes by calling display_country_codes()"


    def get_headline_by_source(self,source='bbc-news'):
        '''This method gives
        headlines by source name as a argument
        and returns a json response'''
        if source in self.sources:
            self.url = 'https://newsapi.org/v2/top-headlines?sources='+source+'&apiKey='+self.secret_key
            try:
                response = requests.get(self.url).json()
                headlines = response["articles"]
                return headlines
            except:
                print("Internet Required!")
        else:
            print("Invalid source name. See All source names by calling display_sources()")
            return 

    def get_head_by_cat_country(self,cat='technology',country='in'):
        '''This method gives
        headlines by category and country  name as a argument
        and returns a json response'''
        print(cat,country)
        if cat in self.sources or country in self.country_codes:
            self.url = 'https://newsapi.org/v2/top-headlines?country='+country+'&category='+cat+'&apiKey='+self.secret_key
            try:
                response = requests.get(self.url).json()
                headlines = response["articles"]
                return headlines
            except:
                print("Internet Required!")
        else:
            print("Invalid category and country name. See All categories and country  names by calling display_catcty()")
            return 

    def get_top_headlines_about(self,query='Modi'):
        '''This method gives
        top headlines by some query
        as a argument and return a json response'''
        self.url='https://newsapi.org/v2/top-headlines?q='+query+'&apiKey='+self.secret_key
        try:
            response = requests.get(self.url).json()
            headlines = response["articles"]
            if len(headlines) > 1:
                return headlines
            else:
                print("No result found for ",query)

        except:
            print("Internet Required!")

    def get_every_about(self,query='india'):
        '''This methods gives
        everything about some topic by giving topic
        as a argument'''
        self.url = 'https://newsapi.org/v2/everything?q='+query+'&apiKey='+self.secret_key
        try:
            response = requests.get(self.url).json()
            headlines = response["articles"]
            if len(headlines) > 1:
                return headlines
            else:
                print("No result found for ",query)

        except:
            print("Internet Required!")


    def get_from_all_sources(self):
        '''This methods gives
        everything from all sources without ang aruguments'''
        self.url = 'https://newsapi.org/v2/sources?apiKey='+self.secret_key
        try:
            response = requests.get(self.url).json()
            news = response["sources"]
            return news
        except:
            print("Internet Required!")

    def get_by_lang(self,lang='en'):
        '''This methods gives
        everything from all sources by taking one argument for language and returns json response'''
        if lang not in self.lang:
            print("The news in language you provide is not found! See All Avialable Language We support by calling display_languages()")
        else:
            self.url='https://newsapi.org/v2/sources?language='+lang+'&apiKey='+self.secret_key
            try:
                response = requests.get(self.url).json()
                news = response["sources"]
                return news
            except:
                print("Internet Required!")

    def display_catcty(self):
        '''This method returns the list of categories and country codes'''
        return (self.cat,self.country_codes)

    def display_langauges(self):
        '''This method returns the list of supported languages'''
        return self.lang

    def get_help(self):
        '''returns docstring for the Class'''
        print(help(PYNEWS))



p = PYNEWS()

