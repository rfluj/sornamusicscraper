
from webbrowser import get
from .req import Req
from .globals import Globals
from .bs import Bs

class SornaMusicScraper:
    def __init__(self):
        self.baseurl = "https://sornamusic.ir/"
        self.req     = Req()
        self.globals = Globals()
        self.bs      = Bs()
    
    # create function for get all artists list
    # input    --->>> None
    # response --->>> result , message, statuscode
    def getAllArtists(self):
        statuscode, response = self.req.sendrequest(self.baseurl, headers=self.globals.HomePageHeader)
        if statuscode == -1 or statuscode == -2:
            return False, "error in send request.", -4
        elif statuscode == 200:
            result = self.bs.getAllHomeArtists(response.text)
            if result:
                if len(result) == 0:
                    return False, "nothing found in page. something wrong.", -1
                else:
                    return result, "successful", 1
            else:
                return False, "error in scrap home page. url : " + self.baseurl, -2
        else:
            return False, "error in load page all artists. Status_Code : " + str(statuscode), -3
    
    # create function for get artist info. like songs and albums
    # input    --->>> artist page url
    # response --->>>
    def getArtistAllInfo(self, url, output=[]):
        statuscode, response = self.req.sendrequest(url, headers=self.globals.HomePageHeader)
        if statuscode == -1 or statuscode == -2:
            return False, "error in send request.", -4
        elif statuscode == 200:
            result, nextpage = self.bs.getArtistAllInfo(response.text)
            if result:
                output      += result
                checkmessage = True
                if nextpage:
                    output, message, statuscode = self.getArtistAllInfo(nextpage, output)
                    checkmessage = False
                if statuscode == 1:
                    message = "successful"
                    checkmessage = False
                if checkmessage:
                    message = 'successful'
                return output, message, statuscode
            else:
                return False, "error in scrap artist page. url : " + url, -2
        else:
            return False, "error in load page artist. Status_Code : " + str(statuscode), -3
            


