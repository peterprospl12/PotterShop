import io
import logging
import random
from utils import convert_price
from prestashopAPI import PrestaShopAPI
import requests
from requests.auth import HTTPBasicAuth
from product import BaseProduct
import json

def upload_image(api_url, api_key, product_id, image_path):
    url = f'{api_url}/images/products/1/'
    with open(image_path, 'rb') as image_file:
        files = {'image': (image_path, image_file, 'image/jpeg')}
        response = requests.post(url, files=files, auth=HTTPBasicAuth(api_key, ''))
        
    if response.status_code == 200:
        print('Product image was successfully created.')
    else:
        print(f'Failed to upload image. Status code: {response.status_code}, Response: {response.text}')


def main():
    api_url = 'http://localhost:8080/api'
    api_key = 'leak'
    api = PrestaShopAPI(api_url, api_key)

    # # Print products
    # api.print_products()

    # # Print categories
    # api.print_categories()
    logging.basicConfig(level=logging.NOTSET)
    #api.print_products()
    #upload_image(api_url, api_key, 1, '/home/peter/VsCodeProjects/PotterShop/api/1024.jpg')

    # product_id = 2
    # updated_fields = {
    #     'name': 'Updated Product',
    #     'price': '111111.11',
    #     'description': 'This is an updated product',
    #     'description_short': "jakies gowno",
    #     'id_default_image': 1
    # }
    # product = api.get_product(product_id)
    # print(product)
    # api.print_product(product_id)

    # #api.update_product(product_id, updated_fields)
    # api.print_product(product_id)

    product_template = api.get_empty_product()
    base_product = BaseProduct(product_template)

    with open("/home/peter/VsCodeProjects/PotterShop/scraper-results/all_products.json", 'r', encoding='utf-8') as file:
        products = json.load(file)

    product = products['1']
    base_product.set_name(product["Name"])
    base_product.set_price(convert_price(product["Price"]))
    base_product.set_meta_title(product["Name"])
    base_product.set_link_name(product["Name"])
    base_product.set_description_short("test123")
    base_product.set_description(product["Description"])
    base_product.set_category("1")
    
    categories_list = [{'id': 2}, {'id': 1}, {'id': 1}]
    
    product_template["product"]["associations"]["categories"] = {"category": categories_list}
    
    
    api.api.add('products', base_product.get_product())

if __name__ == '__main__':
    main()