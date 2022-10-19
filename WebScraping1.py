from bs4 import BeautifulSoup
import requests
import subprocess

url="https://www.interviewbit.com/python-mcq/"
headers = {"User-Agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
           "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

source=requests.get(url,headers=headers)
#print(page)
soup1=BeautifulSoup(source.content,"html.parser")
#print(soup)
soup2=BeautifulSoup(soup1.prettify(),"html.parser")
#print(soup1)
qus=soup2.findAll('section',class_="ibpage-mcq-problems__item")
file=open("WepScraping.txt",'w')
#print(len(qus))
for i in qus:
    #print(i)
    span=i.find('span').text.strip()
    p = i.find('p').text.strip()
    p1=i.findAll('p')[1].text.strip()
    p2=i.findAll('p')[2].text.strip()
    p3=i.findAll('p')[3].text.strip()
    p4=i.findAll('p')[4].text.strip()
    p5=i.findAll('p')[5].text.strip()

    print(span+p)
    print('a.',p1)
    print('b.',p2)
    print('c.',p3)
    print('d.',p4)
    print('Answer:',p5)
    print(' ')

    file.write('\n'+span+ p)
    file.write('\n' + p1)
    file.write('\n' + p2)
    file.write('\n' + p3)
    file.write('\n' + p3)
    file.write('\n' + p4)
    file.write('\nAnswer:' + p5)
    file.write('\n' + ' ')

file.close()
subprocess.Popen('notepad WepScraping.txt')













