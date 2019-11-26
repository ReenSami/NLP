__author__ = 'sumreen.azam'
from bs4 import BeautifulSoup
import re
import json

def analyzeLog(textSample):
    ipAddress = []
    urls_list = []
    email_address = []
    image_urls = []
    file_urls = []
    files_list = []
    date_list = []
    hash_tags = []
    simple_text = []
    soup = BeautifulSoup(textSample, "html.parser")
    soup_string = str(soup).replace('~', '').replace('|', ' ').replace(',', ' ').replace('"', ' ').replace('{', ' ').replace('}', ' ').replace('(', ' ').replace(')', ' ').replace(';', ' ').replace('[',' ').replace(']',' ')
    txtString = soup_string.split(' ')
    txtString = filter(None, txtString)
    for t in txtString:
        if(re.search("(?P<url>https?://[^\s]+)", t)):
            if (re.search('([-\w]+\.(?:jpg|gif|png))', t)):
                image_urls.append(t)
            elif (re.search('([-\w]+\.(?:pdf|csv|docx|ppt))', t)):
                file_urls.append(t)
            else:
                urls_list.append(t)
        elif(re.search(r'\d{4}-\d{2}-\d{2}', t)):
            date_list.append(t)
        elif(re.search(r'[0-9]+(?:\.[0-9]+){3}', t)):
            ipAddress.append(t)
        elif(re.search(r"[^@]+@[^@]+\.[^@]+", t)):
            email_address.append(t)
        elif (re.search(r"(\S+(?:dll|exe|docx|pdf|ppt|csv|bash|batch|libs|png|gif|jpg))", t)):
            files_list.append(t)
        elif (re.search(r'(?i)\#\w+', t)):
            hash_tags.append(t)
        else:
            simple_text.append(t)

    response = {
        'urls_list':urls_list,
        'image_urls_list':image_urls,
        'file_urls_list': file_urls,
        'date_list': date_list,
        'IP_address_list':ipAddress,
        'emails_list':email_address,
        'file_names_list':files_list,
        'hash_tags_list':hash_tags,
        'simple_text_list':simple_text,
    }
    return json.dumps(response)


class Test():

    fileName = 'sample.txt'
    txt = open(fileName, "r")
    result= analyzeLog(txt)
    print result


    #print image_urls




Test()