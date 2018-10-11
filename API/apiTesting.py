__author__ = 'Singhhakam'

import requests
import json

class ApiTest:

    def getcall(self,url):
        resp= requests.get(url)
        return resp

    def verifyResponse(self,resp):
        if (resp.status_code==200):
            print("API executed successfully")
        else:
            print("API not executed properly")

    def printdata(self,resp):
        print(json.dumps(resp.json(), indent=4))

if __name__ == '__main__':
    #You can change url here .
    BASEURL = "https://api.github.com/"


    ap =ApiTest()
    response = ap.getcall(BASEURL)
    ap.verifyResponse(response)
    ap.printdata(response)