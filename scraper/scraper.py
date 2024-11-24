import requests, json, os
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_fixed


images_limit = 2

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_soup(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup

def get_number_of_pages(url):
    try:
        soup = get_soup(url)
        stick_elements = soup.find_all('li', class_='stick')
        if stick_elements:
            last_stick = stick_elements[-1]
            link = last_stick.find_next('a')
            if link and link.get_text(strip=True).isdigit():
                return int(link.get_text(strip=True))
        return "ERROR: Number of pages not found."
    except requests.RequestException as e: return f"ERROR: {e}"
    except Exception as e: return f"ERROR: {e}"


def get_links(url):
    try:
        soup = get_soup(url)
        product_elements = soup.select("a.f-row")
        product_links = ['https://pottermania.pl'+element.get('href') for element in product_elements if element.get('href')]
        return product_links
    except requests.exceptions.HTTPError as e: print(f"ERROR: {e}")


def get_product(url, number):
    try:
        soup = get_soup(url)
        name = soup.find('h1', itemprop='name').get_text(strip=True)
        price = soup.find('em', class_="main-price").get_text(strip=True)
        availability = soup.find('div', class_='row availability').find('span', class_='second').get_text(strip=True)

        finished_categories = False
        category_num = 2
        categories = []
        while (finished_categories == False):
            li_elements = soup.find_all('li', class_='bred-'+str(category_num))
            category_num+=1
            category = []
            for li in li_elements:
                category_name = li.find('span', itemprop='name')
                if category_name:
                    category.append(category_name.get_text(strip=True))
            if category==[]: finished_categories = True
            else: categories.append(category[0])

        description = soup.find('div', itemprop = "description")
        p_tags = description.find_all('p')
        if p_tags:
            last_p = p_tags[-1]
            last_p.decompose()
        for tag in description.find_all(True):
            if 'style' in tag.attrs: del tag['style']
            if 'itemprop' in tag.attrs: del tag['itemprop']
        description = str(description).replace('\n', '').replace('\r', '')

        img_tags = soup.find_all('a', class_=['gallery', 'js__gallery-anchor-image'])
        img_urls = ['https://pottermania.pl' + img_tag.get('href') for img_tag in img_tags if img_tag.get('href')]
        images_path = []
        number_of_image = 1
        for i in img_urls:
            if images_limit < number_of_image: break
            response = requests.get(i)
            if response.status_code == 200:
                if not os.path.exists('img/'+str(number)): os.mkdir('img/'+str(number))

                if not os.path.exists('img/'+str(number)+'/'+str(number_of_image)+'.jpg'):
                    with open('img/'+str(number)+'/'+str(number_of_image)+'.jpg', 'wb') as file:
                        file.write(response.content)
                    print('[' + str(number_of_image) + '/' + str(len(img_urls)) + '] DOWNLOADING: img/'+str(number)+'/'+str(number_of_image)+'.jpg')
                else:
                    print('[' + str(number_of_image) + '/' + str(len(img_urls)) + '] FILE EXISTS: img/'+str(number)+'/'+str(number_of_image)+'.jpg')

                images_path.append('img/'+str(number)+'/'+str(number_of_image)+'.jpg')

            else: print('ERROR:', response.status_code)
            number_of_image+=1

        data = {
            "Name": name,
            "Price": price,
            "Availability": availability,
            "Categories": categories,
            "Images": images_path,
            "Description": description
        }

        return data
    except requests.RequestException as e: return f"ERROR: {e}"
    except Exception as e: return f"ERROR: {e}"


url = "https://pottermania.pl/harry-potter-wszystkie-produkty/"
number_of_pages = get_number_of_pages(url)
print("FOUND "+str(number_of_pages)+ " PAGES")


titles = []
for i in range(1, number_of_pages+1):
    titles = titles + get_links(url+str(i))
    print("SCRAPPED URLS FROM " + str(i) + " PAGES")
titles = list(dict.fromkeys(titles))
print("FOUND "+str(len((titles))) +" PRODUCTS")

if not os.path.exists('img'): os.mkdir('img')
number = 1
jsonD={}
for url in titles:
    print("-----------------["+str(number)+'/'+str(len(titles))+"]-----------------")
    print("SCRAPPING "+url)
    result = get_product(url, number)
    jsonD[str(number)] = result
    number += 1

    json_data = json.dumps(jsonD, indent=4, ensure_ascii=False)
    with open("all_products.json", "w", encoding="utf-8") as file:
        file.write(json_data)

    print("SCRAPPED " + url)

json_data = json.dumps(jsonD, indent=4, ensure_ascii=False)
with open("all_products.json", "w", encoding="utf-8") as file:
    file.write(json_data)
print("SAVED")
