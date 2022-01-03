The code is divided into two modules. The first module: Crawler.py is a very simple implementation of webcrawling.

First of all the code is meant to be run in a python interpreter.

- The code starts by importing the BeautifulSoup library.
- The webCrawler class is then defined, which has a constructor that takes an iterable of URLs to observe and a function called crawl() that downloads the URL from the given url and returns it as text.
- The run() method starts by checking if there are any URLs in the observed_urls list or not.
- If there aren't, it will add them all to observed_urls .
- Then, it calls get_urls() , which gets all links on a page and returns them as strings with their corresponding paths (the path is relative to whatever URL was passed into this function).
- It then uses BeautifulSoup's findAll('a') method to find all links on the page and loops through each one until it finds one with an href attribute starting with '/'.
- This means that we can use urljoin(url) to create a new path for crawling based off of what was passed in as its argument.
- Finally, after looping through every link found on the page, we call crawl() .
- The code creates an instance of the webCrawler class with the url parameter set to ['https://www.stackoverflow.com/'] and then runs it.