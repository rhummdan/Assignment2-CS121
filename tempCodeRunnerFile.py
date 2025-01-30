from scraper import visited_webpages, test_scraper
from collections import Counter


html1 = """
<div>
    <p>apple Hello, banana <b>world</b> my name is lana it's!</p>
    <p> apple 00</p>
</div>
"""

html2 = """
<div>
    <p>APPLE</p>
</div>
"""

html3 = """
<div>
    <p>banana blueberry bananas i'm banana 1 2 3 4 5 6 7 8 9 0 1 2 2345 apple apple apple</p>
</div>
"""

test_scraper(html1)
test_scraper(html2)
test_scraper(html3)

def is_stopword(word):
    stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours\tourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves']
    
    return word in stop_words

def make_report():
    report = open("report.md", "w")
    report.write("# CS 121 Assignment 2 Report: \n")
    
    top_50_words = get_top_50_words(report)
    for num, word in enumerate(top_50_words):
        report.write(f"{num}. {word[0]}\n")
        
    report.close()
    

def get_top_50_words(report):
    report.write("## Top 50 Words:")
    
    combined_frequencies = get_combined_frequencies()
    
    top_50_words = []
    
    count = 0
    print(combined_frequencies)
    for word in combined_frequencies:
        if (not is_stopword(word)) and count < 50:
            top_50_words.append(word)
            count += 1 
            
    print(top_50_words)
    return top_50_words
    
def get_combined_frequencies():
    # combined the frequencies from all the webpages
    combined_frequencies = Counter()
    for webpage in visited_webpages:
        combined_frequencies.update(webpage.word_frequencies)
    
    # sort the combined frequency map by decreasing frequency 
    sorted_combined_frequencies = sorted(combined_frequencies.items(), key=lambda frequency : (-frequency[1], frequency[0])) 
    
    return sorted_combined_frequencies
        
        
make_report()

