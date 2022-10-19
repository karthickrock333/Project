from bs4 import BeautifulSoup
import requests
import subprocess

url="https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

headers = {"User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
           "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page=requests.get(url,headers=headers)
soup1= BeautifulSoup(page.content,"html.parser")
#print(soup1)
soup2=BeautifulSoup(soup1.prettify(),"html.parser")
list = soup2.findAll('div',class_="_2kHMtA")
#print(list)
file=open('Flipkarts.txt','w',encoding='utf-8')
for x in list:
    a=x.find('div' ,class_="_4rR01T").text.strip()
    b=x.find('div' ,class_="_30jeq3 _1_WHN1").text.strip()
    c=x.find('div' ,class_="_3LWZlK").text.strip()

    #print(a,'\n','Rating:',c,'  Price:',b,'\n',' ')
    print(f"Laptop:\t{a}\nRating:{c} \nPrice:{b}\n ")

    #file.write(a+'\n'+'Rating:'+c+'  Price:'+b+'\n')
    file.write(f"{a}\nRating:{c} \nPrice:{b}\n \n")
file.close()
subprocess.Popen('notepad Flipkarts.txt')





