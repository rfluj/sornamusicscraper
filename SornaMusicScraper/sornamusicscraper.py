
from .req import Req
from .globals import Globals
from .bs import Bs

class SornaMusicScraper:
    def __init__(self):
        self.baseurl = "https://sornamusic.ir/"
        self.req     = Req()
        self.globals = Globals()
        self.bs      = Bs()
    
    def getAllArtists(self):
        statuscode, response = self.req.sendrequest(self.baseurl, headers=self.globals.HomePageHeader)
        print(statuscode)
        if statuscode == 200:
            self.bs.getAllHomeArtists(response.text)


