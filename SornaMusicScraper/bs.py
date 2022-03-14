
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
        soup  = self.BeautifulSoup(response, "html.parser")
        # print(soup.prettify())
        atags = self.querySelector("aside.side-menu|ul|li.cat-item cat-item-2|ul.children|li|a", [soup], [])
        if atags:
            for a in atags:
                obj = {'url' : a['href'], 'artist_name' : a.text}
                print(obj)
            print(len(atags))
        else:
            print('found nothing.')

