import requests
from bs4 import BeautifulSoup
import time 
import random
import re

def extract_links(url, depth, visited):
    user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1",
    ]
    try:
        #Random user-agent
        headers = {"User-Agent": random.choice(user_agents)}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        for link in links:
            try:
                href = link.get('href')
                if href is not None and href.startswith('/'):
                    # The link is truncated, so we need to follow it
                    full_url = f'{url}{href}'
                else:
                    full_url = href

                visited.add(full_url)
            except requests.exceptions.RequestException:
                # Skip the subdomain if there is a request exception
                pass
        if depth < 5:
            for link in links:
                href = link.get('href')
                #time.sleep(1)
                if href is not None and href.startswith('/'):
                    full_url = f'{url}{href}'
                else:
                    full_url = href
                if full_url not in visited:
                    
                    extract_links(full_url, depth + 1, visited)
    except requests.exceptions.RequestException:
    # Skip the subdomain if there is a request exception
        pass
visited = set()
the_final_urls=[]
#extract_links('https://atalaysblog.wordpress.com', 0, visited)

with open("domains.txt") as the_file:  #Domains & subdomain that will be searched. HTTPS must be included. 
    the_file=the_file.read().splitlines() 
    for i in the_file:
        #time.sleep(1)
        time.sleep(random.choice([3,7,5,8,13,1,2,4,11,1,2,3,4,5,6,7,8,9])) #Will be uncommented at the final

        extract_links(i, 0, visited)
    
    for  i in range (len(the_file)):
        for url in visited:
            if url is not None and url.startswith('http') and the_file[i] in url:
                the_final_urls.append(url)
                #print(url)
            else:
                pass
    
#print()
#print('----------*****------')
#for i in the_final_urls:
#    print(i)
#print('----------LOOOOOOOL------')

the_final_urls = list(dict.fromkeys(the_final_urls))  #Removed the duplicated values
for i in the_final_urls:
    print(i)


def run_the_regex_rules():
    patterns = [
        re.compile(r'4[0-9]{12}(?:[0-9]{3})?'), #Visa
        re.compile(r'5[1-5][0-9]{14}'),         #MasterCard
        re.compile(r'3[47][0-9]{13}'),          #AMEX
        ]
    for url in the_final_urls:
        response = requests.get(url)
        text = response.text
        time.sleep(random.choice([3,7,5,8,13,1,2,4,11,1,2,3,4,5,6,7,8,9]))

        for i,pattern in enumerate(patterns):
            matches = pattern.finditer(text)
            for match in matches:
                print(f'Regular expression {i+1}: {match.group()} : {response.url}')
                
print(run_the_regex_rules())
