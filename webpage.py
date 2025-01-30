from bs4 import BeautifulSoup
import re

class Webpage:
    def __init__(self, url, resp):
        self.url = url
        self.resp = resp
        self.tokens = []
        self.word_frequencies = {}
        
        # call the method to extract word information
        self.extract_word_information()
        
    def extract_word_information(self):
        """
        Returns a dictionary with all the words found on the page and their frequency. 
        """
        # create beautiful soup object and get all the text
        parsed_page = BeautifulSoup(self.resp.raw_response.content, "html.parser").get_text()
        
        # create token list 
        self.__tokenize(parsed_page)
       
        # compute frequencies
        self.__compute_word_frequencies(self.tokens)

    def __tokenize(self, parsed_page):
        """
        Tokenizes the input text, keeping only alphanumeric and ' sequences, independent of capitalization.
        """
        self.tokens = [token for token in re.findall(r"[a-zA-Z0-9']+", parsed_page.lower())]         

    def __compute_word_frequencies(self, tokenList):
        """
        Input: tokenList: List<Token>
        Output: Map<Token,Count>
        Counts the number of occurrences of each token in the token list. 
        """    
        for token in self.tokens:
            # get token frequency from map, if it doesn't exist set to 0, then add 1
            self.word_frequencies[token] = self.word_frequencies.get(token, 0) + 1