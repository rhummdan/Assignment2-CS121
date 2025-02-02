
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

# TODO: Implement a class that keeps track of the longest page
class LongestPage:

      def __init__(self):
            self.longest_page = None