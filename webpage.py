from bs4 import BeautifulSoup
from collections import Counter
import re
import scraper

class Webpage:
    def __init__(self, url, resp):
        self.url = url
        self.resp = resp
        self.tokens = []
        self.word_count = 0
        self.word_frequencies = {}
        
        # call the method to extract word information
        self.__extract_word_information()
        
    def __extract_word_information(self):
        """
        Parsed page and then computes a dictionary with all the words found on the page and their frequency. 
        """
        # create beautiful soup object and get all the text
        parsed_page = BeautifulSoup(self.resp.raw_response.content, "html.parser").get_text()
        
        # create token list 
        self.__tokenize(parsed_page)

        # compute word count
        self.word_count = len(self.tokens)
       
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
                  
    def is_stopword(self, word):
        """
        Returns whether a word/token is a stop word
        """
        stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours\tourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']
        return word in stop_words
    
    def get_combined_frequencies():
        """
        Combines the word frequencies hashmaps from all the webpages
        """
        # combined the frequencies from all the webpages
        combined_frequencies = Counter()
        for webpage in scraper.report.visited_webpages:
            combined_frequencies.update(webpage.word_frequencies)

        # sort the combined frequency map by decreasing frequency 
        sorted_combined_frequencies = sorted(combined_frequencies.items(), key=lambda frequency : (-frequency[1], frequency[0])) 

        return sorted_combined_frequencies

    def get_top_50_words():
        """
        Gets the 50 most common words in the entire set of pages, excluding stop words
        """
        combined_frequencies = self.get_combined_frequencies()
        
        top_50_words = []
        count = 0
        for word, freq in combined_frequencies:
            # add the word to top_50_words if it's not a stopword and count 50 has not been reached
            if (not is_stopword(word)) and count < 50:
                top_50_words.append((word, freq))
                count += 1 
                
        return top_50_words
    
