import scraper 
from collections import Counter

from webpage import Webpage

class Report():
    def __init__(self):
        # keeps track of the visited pages
        self.visited_url = set()
        self.visited_webpages = []
        
    def add_site(self, url):
        # add the url to set
        self.visited_url.add(url)
        
    def add_webpage(self, url, resp):
        webpage = Webpage(url, resp)
        visited_webpages.append(webpage)
        
    def visited_site(self, url):
       return url in self.visited_url

    def make_report(self):
        """
        Makes the report
        """
        report = open("report.md", "w")
        report.write("# CS 121 Assignment 2 Report: \n")
        
        # top 50 words section
        report.write("## Top 50 Words:\n")
        top_50_words = Webpage.get_top_50_words()
        for num, word in enumerate(top_50_words):
            report.write(f"{num + 1}. {word[0]}\n")
            
        report.close()