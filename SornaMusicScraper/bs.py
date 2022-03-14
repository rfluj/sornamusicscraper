
from unittest import result
from bs4 import BeautifulSoup

class Bs:
    def __init__(self):
        self.BeautifulSoup = BeautifulSoup

    def querySelector(self, query, soup, output):
        try:
            nodes = soup
            selectors = query.split('|')
            for node in nodes:
                if node:
                    selector = selectors[0]
                    if '.' in selector:
                        results = node.find_all(selector.split('.')[0], { 'class': ' '.join(selector.split('.')[1:]) })
                    elif '#' in selector:
                        results = node.find_all(selector.split('#')[0], { 'id': ' '.join(selector.split('#')[1:]) })
                    else:
                        results = node.find_all(selector)
                    if len(selectors) == 1:
                        for res in results:
                            output.append(res)
                            # return results
                    else:
                        self.querySelector('|'.join(selectors[1:]), results, output)
            return output
        except Exception as e:
            print(e)
            print('querySelector')
            return False

    def getAllHomeArtists(self, response):
        try:
            soup  = self.BeautifulSoup(response, "html.parser")
            # print(soup.prettify())
            atags = self.querySelector("aside.side-menu|ul|li.cat-item cat-item-2|ul.children|li|a", [soup], [])
            if atags:
                result = []
                for a in atags:
                    obj = {'url' : a['href'], 'artist_name' : a.text}
                    result.append(obj)
                return result
            else:
                return []
        except:
            return False
    
    # response --->>> result(array) and next page url if exist
    def getArtistAllInfo(self, response):
        try:
            soup  = self.BeautifulSoup(response, "html.parser")
            atags = self.querySelector("div.mycontent|article|header.clearfix|h2|a", [soup], [])
            if atags:
                result = []
                for a in atags:
                    url  = a['href']
                    text = a.text
                    if 'دانلود آلبوم' in text:
                        type = 'album'
                        name = text.split('دانلود آلبوم')[1]
                    elif 'دانلود آهنگ' in text:
                        type = 'song'
                        name = text.split('دانلود آهنگ')[1]
                    else:
                        type = 'song'
                        name = text
                    obj = {
                        'url' : url,
                        'name' : name,
                        'type' : type
                    }
                    result.append(obj)
                nextpagetag = self.querySelector("div.navigation|ul|li|a", [soup], [])
                nextpageurl = False  
                if nextpagetag:
                    for a in nextpagetag:
                        if 'برگهٔ بعد »' in a.text:
                            nextpageurl = a['href']
                            break
                return result, nextpageurl
            else:
                return False, False
        except Exception as e:
            return False, False

