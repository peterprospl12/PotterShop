import time, random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



TIME_SLEEP = 0


website_addr = "https://localhost:8443/"
service = Service(executable_path='/usr/bin/chromedriver')


chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

browser = webdriver.Chrome(service=service, options=chrome_options)




def Z1(website_addr, browser):
    def products_links(url):
        browser.get(url)
        time.sleep(TIME_SLEEP)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'product')))
        products = browser.find_elements(By.CLASS_NAME, 'thumbnail')
        product_links = []
        for i in range(len(products)):
             product_links.append(products[i].get_attribute("href"))
        return product_links
        
        
    def add_to_the_cart(url):
        browser.get(url)
        time.sleep(TIME_SLEEP)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'container')))
        try:
            a = WebDriverWait(browser, 0.1).until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-page-add-to-cart')))
        except TimeoutException:
            return 1
        try:
            WebDriverWait(browser, 0.1).until(EC.presence_of_element_located((By.XPATH, "//span[@data-stock]")))
            dostepne = browser.find_element(By.XPATH, "//span[@data-stock]")
            dostepne = dostepne.get_attribute("data-stock")
        except TimeoutException:
            dostepne = 2
        b = random.randint(1, int(dostepne))
        
        D_ile = browser.find_element(By.NAME, 'qty')
        D_ile.send_keys(Keys.DELETE)
        D_ile.send_keys(b)
        B_dodaj = browser.find_element(By.CLASS_NAME, 'add-to-cart')
        B_dodaj.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cart-products-count')))
        return 2
        
        
    ile = random.randint(1, 10)
    ile2 = [ile, 10-ile]
    Products_links1 = products_links(website_addr + '72-ksiazki')
    Products_links2 = products_links(website_addr + '65-kubki')
    for link in Products_links1:
        if add_to_the_cart(link) == 2: ile2[0]-=1
        if ile2[0] == 0: break
    for link in Products_links2:
        if add_to_the_cart(link) == 2: ile2[1]-=1
        if ile2[1] == 0: break
    time.sleep(TIME_SLEEP)





def Z2(website_addr, browser, name):
    def add_to_the_cart(products):
        browser.get(random.choice(products))
        time.sleep(TIME_SLEEP)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'container')))

        try:
            a = WebDriverWait(browser, 0.1).until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-page-add-to-cart')))
        except TimeoutException:
            add_to_the_cart(products)
            return
        
        B_dodaj = browser.find_element(By.CLASS_NAME, 'add-to-cart')
        B_dodaj.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cart-products-count')))

    browser.get(website_addr)
    I_search = browser.find_element(By.NAME, 's')
    I_search.send_keys(name)
    I_search.send_keys(Keys.RETURN)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'product')))
    time.sleep(TIME_SLEEP)
    
    products = browser.find_elements(By.CLASS_NAME, 'thumbnail')
    dostepne_produkty = []
    for i in range(len(products)):
        dostepne_produkty.append(products[i].get_attribute("href"))
    add_to_the_cart(dostepne_produkty)

            
        


def Z3(website_addr, browser):
    browser.get(website_addr)
    time.sleep(TIME_SLEEP)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'remove-from-cart')))
    products = browser.find_elements(By.CLASS_NAME, 'remove-from-cart')
    product_links = [element.get_attribute("href") for element in products]
    jest = len(product_links)
    if jest <= 3: Z = jest-1
    else: Z = 3
    links = random.sample(product_links, k=Z)
    
    for link in links:
        browser.get(link)
        time.sleep(TIME_SLEEP)





def Z4(website_addr, browser):
    browser.get(website_addr)
    time.sleep(TIME_SLEEP)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control-submit')))
    browser.find_element(By.CSS_SELECTOR, "input[value=\"1\"]").click()
    browser.find_element(By.CSS_SELECTOR, "input[name=\"firstname\"]").send_keys("Name")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"lastname\"]").send_keys("Surname")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"email\"]").send_keys("test" + str(random.randint(0, 99999999)) + "@gmail.com")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"password\"]").send_keys("password")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"customer_privacy\"]").click()
    browser.find_element(By.CSS_SELECTOR, "input[name=\"psgdpr\"]").click()
    time.sleep(TIME_SLEEP)
    browser.find_element(By.CLASS_NAME, 'form-control-submit').click()





def Z5(website_addr, browser):
    browser.get(website_addr)
    time.sleep(TIME_SLEEP)

    browser.find_element(By.ID, 'field-address1').send_keys('ADDRESS')
    browser.find_element(By.ID, 'field-postcode').send_keys('00-000')
    browser.find_element(By.ID, 'field-city').send_keys('CITY')
    time.sleep(TIME_SLEEP)
    browser.find_element(By.NAME, 'confirm-addresses').click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'continue')))

    browser.find_element(By.ID, 'delivery_option_24').click()
    time.sleep(TIME_SLEEP)
    browser.find_element(By.NAME, 'confirmDeliveryOption').click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'payment-confirmation')))

    browser.find_element(By.ID, 'payment-option-2').click()
    time.sleep(TIME_SLEEP)
    browser.find_element(By.ID, 'conditions_to_approve[terms-and-conditions]').click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.center-block")))
    time.sleep(TIME_SLEEP)
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary.center-block").click()





def Z6(website_addr, browser):
    browser.get(website_addr)
        
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'account')))
    time.sleep(TIME_SLEEP)
    browser.find_element(By.CLASS_NAME, 'account').click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'history-link')))
    time.sleep(TIME_SLEEP)
    browser.find_element(By.ID, 'history-link').click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-link-action=\"view-order-details\"]")))
    time.sleep(TIME_SLEEP)
    browser.find_element(By.CSS_SELECTOR, "a[data-link-action=\"view-order-details\"]").click()


    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'order-infos')))
    D_info = browser.find_element(By.ID, 'order-infos')
    li_elements = D_info.find_elements(By.CSS_SELECTOR, '.box > ul > li')
    for element in li_elements:
        try:
            a = element.find_element(By.TAG_NAME, 'a')
            browser.get(a.get_attribute('href'))
            time.sleep(TIME_SLEEP)
            return
        except NoSuchElementException as e:
            continue






start_time = time.time()

print("Dodanie do koszyka 10 produktów (w różnych ilościach) z dwóch różnych kategorii")
Z1(website_addr, browser)


print("Wyszukanie produktu po nazwie i dodanie do koszyka losowego produktu spośród znalezionych")
Z2(website_addr, browser, "Kamień")


print("Usunięcie z koszyka 3 produktów")
Z3(website_addr + 'koszyk', browser)


print("Rejestracja nowego użytkownika")
Z4(website_addr + 'logowanie?create_account=1', browser)


print("Wykonanie zamówienia zawartości koszyka, wybór metody płatności: przy odbiorze, wybór jednego z dwóch przekaźników, zatwierdzenie zamówienia")
Z5(website_addr + 'zamówienie', browser)


print("Sprawdzenie statusu zamówienia, pobranie faktury VAT")
Z6(website_addr, browser)




end_time = time.time()
czas = end_time - start_time

print("Czas wykonania: " + str(czas) + " sekundy")
