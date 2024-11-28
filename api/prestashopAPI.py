import logging
from prestapyt import PrestaShopWebServiceDict
from product import BaseProduct, BaseCategory

class PrestaShopAPI:
    def __init__(self, api_url, api_key):
        self.api_url =  api_url
        self.api_key = api_key
        self.api = PrestaShopWebServiceDict(self.api_url, self.api_key)
        self.configure_logging()
        self.categories = {}

    def configure_logging(self):
        logging.basicConfig(level=logging.ERROR)
        self.logger = logging.getLogger("prestashop")
        self.logger.setLevel(logging.ERROR)

    def get_products(self):
        try:
            return self.api.get('products')
        except Exception as e:
            self.logger.error(f'Error getting products: {e}')
            return None
        
    def get_empty_product(self):
        try:
            return self.api.get('products', options={"schema": "blank"})
        except Exception as e:
            self.logger.error(f'Error getting empty product: {e}')
            return None

    def get_product(self, product_id):
        try:
            return self.api.get('products', product_id)
        except Exception as e:
            self.logger.error(f'Error getting product: {e}')
            return None

    def print_product(self, product_id):
        product_data = self.get_product(product_id)
        if product_data is None:
            self.logger.error(f'Error getting product data for product ID: {product_id}')
            return

        product = product_data['product']
        try:
            product_name = product['name']['language']['value']
            product_price = product['price']
            product_quantity = product['quantity']['value']
            category_id = product['id_category_default']
            category_data = self.get_category(category_id)
            category_name = category_data['category']['name']['language']['value']
            print(f'Product ID: {product_id}, Name: {product_name}, Price: {product_price}, Quantity: {product_quantity}, Category: {category_name}')
        except Exception as e:
            self.logger.error(f'Error parsing product data for product ID: {product_id}: {e}')

    def print_products(self):
        products_data = self.get_products()
        if products_data is None:
            self.logger.error('Error getting products')
            return

        products = products_data['products']['product']
        for product in products:
            product_id = product['attrs']['id']
            self.print_product(product_id)

    def get_categories(self):
        try:
            return self.api.get('categories')
        except Exception as e:
            self.logger.error(f'Error getting categories: {e}')
            return None

    def get_category(self, category_id):
        try:
            return self.api.get('categories', category_id)
        except Exception as e:
            self.logger.error(f'Error getting category: {e}')
            return None
        
    def get_empty_category(self):
        try:
            return self.api.get('categories', options={"schema": "blank"})
        except Exception as e:
            self.logger.error(f'Error getting empty category: {e}')
            return None

    def print_categories(self):
        categories_data = self.get_categories()
        if categories_data is None:
            self.logger.error('Error getting categories')
            return

        categories = categories_data['categories']['category']
        for category in categories:
            category_id = category['attrs']['id']
            category_data = self.get_category(category_id)
            if category_data is None:
                self.logger.error(f'Error getting category data for category ID: {category_id}')
                continue

            try:
                category_name = category_data['category']['name']['language'][0]['value']
                print(f'Category ID: {category_id}, Name: {category_name}')
            except Exception as e:
                self.logger.error(f'Error parsing category data for category ID: {category_id}: {e}')

    def add_product(self, product : BaseProduct):
        try:
            return self.api.add('products', product.get_product())
        except Exception as e:
            self.logger.error(f'Error creating product: {e}')
            return None
        
    def add_category(self, main_category : BaseCategory, sub_category : BaseCategory) -> tuple:
        try:
            self.__update_categories()

            main_category_id = self._get_or_create_category(main_category)

            sub_category_id = 0
            if sub_category.get_name() != "":
                sub_category.set_parent_id(int(main_category_id))
                sub_category_id = self._get_or_create_category(sub_category)

            return main_category_id, sub_category_id
        except Exception as e:
            self.logger.error(f'Error creating category: {e}')
            return None

    def update_product(self, product_id, updated_fields):
        try:
            product_data = self.get_product(product_id)
            if product_data is None:
                self.logger.error(f'Product ID {product_id} not found')
                return

            product = product_data['product']
            product.update(updated_fields)

            readonly_fields = ['manufacturer_name', 'quantity', 'position_in_category', 'cache_default_attribute']
            for field in readonly_fields:
                product.pop(field, None)
            
            print(product) # Debugging

            self.api.edit('products', {'product': product})
            print(f'Product ID: {product_id} updated successfully')
        except Exception as e:
            self.logger.error(f'Error updating product: {e}')

    def delete_product(self, product_id):
        try:
            self.api.delete('products', product_id)
            print(f'Product ID: {product_id} deleted successfully')
        except Exception as e:
            self.logger.error(f'Error deleting product: {e}')

    def set_logging_debug(self):
        logging.basicConfig(level=logging.DEBUG)
        self.logger.setLevel(logging.DEBUG)

    def __update_categories(self):
        categories = self.api.get("categories")["categories"]["category"]
    
        categories_dict = {}

        for category in categories:
            category_id = category["attrs"]["id"]
            
            category_details = self.api.get(f"categories/{category_id}")["category"]
            category_name = category_details["name"]["language"]["value"]
            parent_id = category_details["id_parent"]
            
            categories_dict[category_name] = {
                "category_id": int(category_id),
                "parent_id": int(parent_id),
            }

        self.categories = categories_dict

    def _get_or_create_category(self, category: BaseCategory) -> int:
        category_name = category.get_name()
        if category_name in self.categories:
            return self.categories[category_name]["category_id"]
        else:
            response = self.api.add('categories', category.get_category())
            category_id = response['prestashop']['category']['id']
            return category_id