
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r"C:\Users\DELL\Downloads\icon2.ico",
        timeout=5
    )

def getdata(url):
    r=requests.get(url)
    return r.text

if __name__=="__main__":
    while(True):
        myhtmldata=getdata('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(myhtmldata, 'html.parser')
        
        mydatastr = ""


        for tr in soup.find_all('tbody')[7].find_all('tr'):
            mydatastr += tr.get_text()

        mydatastr=mydatastr[1:]
        itemlist= mydatastr.split("\n\n")
        
        states=['Delhi','Maharashtra', 'Bihar']


        for item in itemlist[0:25]:
            datalist=item.split('\n')
            if datalist[1] in states:
                print(datalist)
                ntitle="Cases of Covid-19"
                ntext=f"State: {datalist[1]} \nIndian:{datalist[2]} Foreign:{datalist[3]} \nCured:{datalist[4]} \nDeaths:{datalist[5]}"
                notifyMe(ntitle,ntext)
                time.sleep(5)
