import logging
import os
from prestashopAPI import PrestaShopAPI
from product import BaseProduct, BaseCategory, BaseImage
import json
from dotenv import load_dotenv
import time

def load_environment_variables():
    load_dotenv()
    return os.getenv("API_URL"), os.getenv("API_KEY"), os.getenv("PROJECT_PATH")

def initialize_api(api_url, api_key):
    api = PrestaShopAPI(api_url, api_key)
    api.delete_all_products()
    api.delete_all_categories()
    return api

def load_products(project_path):
    with open(f"{project_path}/scraper-results/all_products.json", 'r', encoding='utf-8') as file:
        return json.load(file)

def process_product(api, base_product, main_category, sub_category, image, product):
    main_category_name = product["Categories"][0]
    sub_category_name = product["Categories"][1] if len(product["Categories"]) > 1 else None

    main_category.set_default_attributes(main_category_name)
    if sub_category_name is not None:
        sub_category.set_default_attributes(sub_category_name)
    else:
        sub_category = BaseCategory(api.get_empty_category())

    category_id = api.add_category(main_category, sub_category)

    base_product.get_from_json(product)
    base_product.set_category(category_id[0])
    base_product.set_associations(category_id[0], category_id[1])

    product_id = api.add_product(base_product)
    api.set_product_stock(product_id)

    image.set_image(product["Images"])
    api.add_images(product_id, image.get_images())

def main():
    api_url, api_key, project_path = load_environment_variables()
    api = initialize_api(api_url, api_key)
    products = load_products(project_path)

    logging.basicConfig(level=logging.ERROR)

    base_product = BaseProduct(api.get_empty_product())
    main_category = BaseCategory(api.get_empty_category())
    sub_category = BaseCategory(api.get_empty_category())
    image = BaseImage(f"{project_path}/scraper-results/")

    start_time = time.time()

    for i in range(1, len(products) + 1):
        product = products[str(i)]
        process_product(api, base_product, main_category, sub_category, image, product)

    end_time = time.time()
    print(f'Total time taken to add all products: {end_time - start_time} seconds')

if __name__ == "__main__":
    main()