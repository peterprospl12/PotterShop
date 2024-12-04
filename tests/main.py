import time, random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


website_addr = "http://localhost:8080/"
service = Service(executable_path='/usr/bin/chromedriver')
browser = webdriver.Chrome(service=service, options=Options())




def Z1(website_addr, browser):
    def products_links(url, ile):
        browser.get(url)
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product'))
        )
        products = browser.find_elements(By.CLASS_NAME, 'thumbnail')
        product_links = []
        for i in range(len(products)):
             product_links.append(products[i].get_attribute("href"))
        return random.sample(product_links, k=ile)
        
        
    def add_to_the_cart(url):
        browser.get(url)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'container')))
        try:
            a = WebDriverWait(browser, 0.1).until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-to-cart')))
        except TimeoutException:
            return
        try:
            WebDriverWait(browser, 0.1).until(EC.presence_of_element_located((By.XPATH, "//span[@data-stock]")))
            dostepne = browser.find_element(By.XPATH, "//span[@data-stock]")
            dostepne = dostepne.get_attribute("data-stock")
        except TimeoutException:
            dostepne = 10
        b = random.randint(1, int(dostepne))
        
        D_ile = browser.find_element(By.NAME, 'qty')
        D_ile.send_keys(Keys.DELETE)
        D_ile.send_keys(b)
        B_dodaj = browser.find_element(By.CLASS_NAME, 'add-to-cart')
        B_dodaj.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cart-products-count')))
        
        
    ile = random.randint(1, 10)
    ile2 = [ile, 10-ile]
    Products_links1 = products_links(website_addr + '25-ksiazki', ile2[0])
    Products_links2 = products_links(website_addr + '18-kubki', ile2[1])
    for link in Products_links1:
        add_to_the_cart(link)
    for link in Products_links2:
        add_to_the_cart(link)





def Z2(website_addr, browser, name):
    def get_products(name):
        I_search = browser.find_element(By.NAME, 's')
        I_search.send_keys(name)
        I_search.send_keys(Keys.RETURN)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'product')))
        
        products = browser.find_elements(By.CLASS_NAME, 'thumbnail')
        dostepne_produkty = []
        for idx in range(len(products)):
             dostepne_produkty.append(products[idx])
        return dostepne_produkty


    def add_to_the_cart(products):
        product = random.choice(products)
        product.click()
        B_dodaj = browser.find_element(By.CLASS_NAME, 'add-to-cart')
        B_dodaj.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'cart-products-count')))


    browser.get(website_addr)
    products = get_products(name)        
    add_to_the_cart(products)

            
        


def Z3(website_addr, browser):
    def links_to_delete():
        browser.get(website_addr)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'remove-from-cart')))
        products = browser.find_elements(By.CLASS_NAME, 'remove-from-cart')
        product_links = [element.get_attribute("href") for element in products]
        return random.sample(product_links, k=3)

    links = links_to_delete()
    for link in links:
        browser.get(link)





def Z4(website_addr, browser):
    browser.get(website_addr)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'form-control-submit')))
    browser.find_element(By.CSS_SELECTOR, "input[value=\"1\"]").click()
    browser.find_element(By.CSS_SELECTOR, "input[name=\"firstname\"]").send_keys("Name")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"lastname\"]").send_keys("Surname")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"email\"]").send_keys("test" + str(random.randint(0, 999)) + "@gmail.com")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"password\"]").send_keys("password")
    browser.find_element(By.CSS_SELECTOR, "input[name=\"customer_privacy\"]").click()
    browser.find_element(By.CSS_SELECTOR, "input[name=\"psgdpr\"]").click()
    browser.find_element(By.CLASS_NAME, 'form-control-submit').click()





def Z5(website_addr, browser):
    browser.get(website_addr)

    browser.find_element(By.ID, 'field-address1').send_keys('ADDRESS')
    browser.find_element(By.ID, 'field-postcode').send_keys('00-000')
    browser.find_element(By.ID, 'field-city').send_keys('CITY')    
    browser.find_element(By.NAME, 'confirm-addresses').click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'continue')))

    browser.find_element(By.ID, 'delivery_option_24').click()
    browser.find_element(By.NAME, 'confirmDeliveryOption').click()
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'payment-confirmation')))

    browser.find_element(By.ID, 'payment-option-2').click()
    browser.find_element(By.ID, 'conditions_to_approve[terms-and-conditions]').click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-primary.center-block")))
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary.center-block").click()





def Z6(website_addr, browser):
    browser.get(website_addr)
        
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'account')))
    browser.find_element(By.CLASS_NAME, 'account').click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'history-link')))
    browser.find_element(By.ID, 'history-link').click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-link-action=\"view-order-details\"]")))
    browser.find_element(By.CSS_SELECTOR, "a[data-link-action=\"view-order-details\"]").click()


    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'order-infos')))
    D_info = browser.find_element(By.ID, 'order-infos')
    li_elements = D_info.find_elements(By.CSS_SELECTOR, '.box > ul > li')
    for element in li_elements:
        try:
            a = element.find_element(By.TAG_NAME, 'a')
            browser.get(a.get_attribute('href'))
            return
        except NoSuchElementException as e:
            continue
        #print("Brak faktury.")






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
