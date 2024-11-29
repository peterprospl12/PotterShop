import logging
import os
from prestashopAPI import PrestaShopAPI
from product import BaseProduct, BaseCategory, BaseImage
import json
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_url = os.getenv("API_URL")
    api_key = os.getenv("API_KEY")
    project_path = os.getenv("PROJECT_PATH")

    api = PrestaShopAPI(api_url, api_key)
    api.delete_all_products()
    api.delete_all_categories()

    product_template = api.get_empty_product()
    base_product = BaseProduct(product_template)
    main_category = BaseCategory(api.get_empty_category())
    sub_category = BaseCategory(api.get_empty_category())
    image = BaseImage(f"{project_path}/scraper-results/")

    project_path = os.getenv("PROJECT_PATH")
    with open(f"{project_path}/scraper-results/all_products.json", 'r', encoding='utf-8') as file:
        products = json.load(file)

    for i in range(1, 100):
        product = products[str(i)]
        main_category_name = product["Categories"][0]
        sub_category_name = product["Categories"][1] if len(product["Categories"]) > 1 else None

        main_category.set_default_attributes(main_category_name)
        if sub_category_name is not None:
            sub_category.set_default_attributes(sub_category_name) if sub_category_name is not None else None

        category_id = api.add_category(main_category, sub_category)

        base_product.get_from_json(product)
        base_product.set_category(category_id[0])
        base_product.set_associations(category_id[0], category_id[1])    
        
        product_id = api.add_product(base_product)

        image.set_image(product["Images"])
        api.add_images(product_id, image.get_images())

        print(f"Product {i} added successfully")

if __name__ == '__main__':
    main()