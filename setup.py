from setuptools import setup

setup(
    name = "fortniteapi",
    packages = ["fortniteapi"],
    version = "1.0.8",
    description = "A python wrapper for the fortnitetracker.com API",
    long_description = """ 
    For a list of all the variables see the github and look at variables.txt

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
    download_url = "https://github.com/mattp111/fortniteapi/archive/1.0.8.tar.gz",
    keywords = ["fortnite", "api", "tracker", "fortnite tracker"],
    classifiers = [],
)
