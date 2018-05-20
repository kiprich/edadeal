from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime

import csv

def get_html(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    browser = webdriver.Chrome(chrome_options=options)

    browser.get(url)

    html = browser.page_source
    browser.quit()
    return html

def write_txt(filename,data):
    
    with open(filename, mode='w') as f: #, encoding='utf8' , encoding="utf_8_sig"
        f.write(data)



def read_txt(filename):
    
    with open(filename, mode='rb') as f: #, encoding=""
        html=f.read()
#        result = chardet.detect(html)
#        print(result)
#        charenc = result['encoding']
#        print(charenc)
    return html


def write_csv(data):
    with open('edadeal.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['title'],
                         data['price'],
                         # data['metro'],
                         # data['url']
                         ))
 
 
def get_page_data(html):
 
    print(type(html))
#    print(html.encode('ascii', errors='xmlcharrefreplace'))
    soup = BeautifulSoup(html, 'lxml')
#    print(type(soup))
    offers = soup.find_all('div', class_="b-offer__root")#.encode('utf-8')
#    print(len(offers))
    i=0
    for offer in offers:
        i+=1
        try:
            #<div title="" class="b-offer__description">Игровой набор MY MINI MIXIQE’S Мини-комната, в&nbsp;ассортименте</div>
            desc = offer.find('div', class_="b-offer__product-info").find('div', class_="b-offer__description").text
        except:
            desc = ''
        print(i)
        print(desc)
        print(desc.encode('utf_8').decode('cp1251','ignore'))

        #    .decode('utf8'))
    #     try:
    #         quantity = offer.find('div', class_='b-b-offer__quantity').text.strip()
    #     except:
    #         quantity = ''    
        # try:
        #     div = ad.find('div', class_='description').find('h3')
        #     url = "https://avito.ru" + div.find('a').get('href')
        # except:
        #     url = ''
        # try:
        #     price = ad.find('div', class_='about').text.strip()
        # except:
        #     price = ''
        # try:
        #     div = ad.find('div', class_='data')
        #     metro = div.find_all('p')[-1].text.strip()
        # except:
        #     metro = ''
        #data = {'desc':desc
        #         'quantity':quantity,
        #         # 'metro':metro,
        #         # 'url':url
        #        }

        # write_csv(data)
    #print(len(data))

def main():
#    print('start: ' + str(datetime.now()))
#    html=get_html('https://edadeal.ru/moskva/offers')
#    write_txt('edadeal.html', html)
    html=read_txt('edadeal.html')
    text=get_page_data(html)
  

#    print('end: ' + str(datetime.now()))

if __name__ == '__main__':
    main()