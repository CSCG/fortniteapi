from setuptools import setup

setup(
    name = "fortniteapi",
    packages = ["fortniteapi"],
    version = "1.0.5",
    description = "A python wrapper for the fortnitetracker.com API",
    long_description = """ 
    A python wrapper for the fortnitetracker.com API. I will add a list on github of all the variables soon

    Usage:


    	import fortniteapi

    	tracker = fortniteapi.tracker("<your api key>, <user>, <platform>")

    	wins = tracker.SOLO_WINS
    	print(wins)

    """,
    long_description_content_type='text/markdown',
    author = "Matt P",
    author_email = "pap0046@nhs.vic.edu.au",
    url = "https://github.com/mattp111/fortniteapi",
    download_url = "https://github.com/mattp111/fortniteapi/archive/1.0.0.tar.gz",
    keywords = ["fortnite", "api", "tracker", "fortnite tracker"],
    classifiers = [],
)
