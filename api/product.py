import os
import random
from utils import convert_price
import io
from bs4 import BeautifulSoup
from PIL import Image

class BaseProduct:
    def __init__(self, product):
        self.product = product
        self.product["product"]["active"] = 1
        self.product["product"]["state"] = 1
        self.product["product"]["available_for_order"] = 1
        self.product["product"]["weight"] = round(random.uniform(0.05, 0.6), 2)
        self.product["product"]["minimal_quantity"] = 1
        self.product["product"]["show_price"] = 1
        self.product["product"]["id_tax_rules_group"] = 1
        del self.product["product"]["associations"]["combinations"]
        del self.product["product"]["position_in_category"]

    def set_name(self, name):
        self.product["product"]["name"]["language"]["value"] = name

    def set_category(self, category_id):
        self.product["product"]["id_category_default"] = category_id

    def set_price(self, price):
        self.product["product"]["price"] = round(price / 1.23, 2)

    def set_meta_title(self, meta_title):
        self.product["product"]["meta_title"]["language"]["value"] = meta_title

    def set_link_name(self, link_name):
        self.product["product"]["link_rewrite"]["language"]["value"] = link_name.replace(" ", "-").lower()

    def set_description_short(self, description_short):
        self.product["product"]["description_short"]["language"]["value"] = description_short

    def set_description(self, description):
        self.product["product"]["description"]["language"]["value"] = description

    def set_associations(self, category_id : int, subcategory_id : int):
        if subcategory_id == 0:
            self.product["product"]["associations"]["categories"] = {"category": [{'id': 2}, {'id': category_id}]}
            pass
        self.product["product"]["associations"]["categories"] = {"category": [{'id': 2}, {'id': category_id}, {'id': subcategory_id}]}

    def get_product(self):
        return self.product
    
    def get_from_json(self, product):
        self.set_name(product["Name"])
        self.set_price(convert_price(product["Price"]))
        self.set_meta_title(product["Name"])
        self.set_link_name(product["Name"])
        self.set_description_short("test123")
        description = self.__remove_src_tags(product["Description"])
        self.set_description(description)

    
    def __remove_src_tags(self, html_content : str):
        soup = BeautifulSoup(html_content, 'html.parser')
        for tag in soup.find_all(src=True):
            parent = tag.find_parent()
            if parent:
                parent.decompose()
        return str(soup)
    

class BaseCategory:
    def __init__(self, category):
        self.category = category
        self.category["category"]["active"] = "1"
        self.category["category"]["is_shop_default"] = "1"
        self.category["category"]["id_parent"] = "2"

    def set_default_attributes(self, name : str):
        self.category["category"]["name"]["language"]["value"] = name
        self.category["category"]["description"] = {'language': [{'attrs': {'id': '1'}, 'value': f'Description for {name}'}]}
        self.category["category"]["link_rewrite"] = {'language': [{'attrs': {'id': '1'}, 'value': name.lower().replace(" ", "-")}]}

    def set_parent_id(self, parent_id):
        self.category["category"]["id_parent"] = parent_id

    def get_name(self) -> str:
        return self.category["category"]["name"]["language"]["value"]

    def get_category(self):
        return self.category


class BaseImage:
    def __init__(self, path_to_images: str):
        self.absolute_path = path_to_images
        self.image_paths = []
        self.images = []

    def set_image(self, image_paths: list):
        self.image_paths = image_paths
        self.__process_image()

    def get_images(self):
        images = self.images
        self.images = []
        return images
    
    def __process_image(self):
        for image_path in self.image_paths:
            image_name, image_path = self.__convert_image_path(image_path)
            with open(image_path, 'rb') as file:
                image = Image.open(file)
                with io.BytesIO() as output:
                    image.convert("RGB").save(output, format="JPEG")
                    content = output.getvalue()

            self.images.append([image_name, content])

    def __convert_image_path(self, image_path : str):
        parts = image_path.split('/')
        return f"{parts[1]}-{parts[2]}", os.path.join(self.absolute_path, f"{parts[0]}/{parts[1]}/{parts[2]}")
