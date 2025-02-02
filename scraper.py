import re
from urllib.parse import urlparse

def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]



def extract_next_links(url, resp):
    # Maintaining a set to make sure we don't visit same page more than once. 
    # Keeps track of URLS (with the fragment)
    visited_urls = set()

    '''
    # 1. unique_urls:
        - We will need a set to keep track of the number of unique pages that we visit (A page here is considered the url without the fragment). A fragment is there to navigate you to a specific part of the webpage.

    #2. longest_page:
        - We'll also need to keep track of which of these pages is the longest in terms of words.
        - This could just be an object with two fields: url, word count
        - Beautiful Scope makes this really easy for us, especially since this requirement doesn't want us to exclude stop words

    # 3. Top 50 Words:
        - Maintain a hash map that keeps track of the number of occurrences of words other than stop words. After we've read all the pages, use a heap to get the top 50
        words.

    # 4. Need to implement a Tracker for ics.uci.edu domain:
        - We can have a defaultdict(set), so that every url (https://{subdomain}.ics.uci.edu) will map to a set of unique pages within that subdomain. This set will ensure that
        we only consider each unique page once. We will be able to use the Len of the set to get the number of unique pages within the domain:

    '''
    # Implementation required.
    # url: the URL that was used to get the page
    # resp.url: the actual url of the page
    # resp.status: the status code returned by the server. 200 is OK, you got the page. Other numbers mean that there was some kind of problem.
    # resp.error: when status is not 200, you can check the error here, if needed.
    # resp.raw_response: this is where the page actually is. More specifically, the raw_response has two parts:
    #         resp.raw_response.url: the url, again
    #         resp.raw_response.content: the content of the page!
    # Return a list with the hyperlinks (as strings) scrapped from resp.raw_response.content
    return list()

def is_valid(url):
    # Decide whether to crawl this url or not. 
    # If you decide to crawl it, return True; otherwise return False.
    # There are already some conditions that return False.
    try:
        parsed = urlparse(url)
        if (parsed.netloc != "ics.uci.edu" and parsed.netloc != "cs.uci.edu" and parsed.netloc != "informatics.uci.edu" and parsed.netloc != "stat.uci.edu"):
            print("oh no")
            return False
        if parsed.scheme not in set(["http", "https"]):
            return False
        return not re.match(
            r".*\.(css|js|bmp|gif|jpe?g|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print ("TypeError for ", parsed)
        raise
    
    return True
    
    
# if __name__=='__main__':
#     print(is_valid("http://google.com"))
#     print(is_valid("https://ics.uci.edu/happening/news/?filter%5Bunits%5D=19"))


