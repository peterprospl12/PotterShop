import unittest
from unittest.mock import patch, MagicMock
from product import BaseProduct, BaseCategory, BaseImage    

class TestBaseProduct(unittest.TestCase):

    def setUp(self):
        self.product_data = {
            "product": {
                "name": {"language": {"value": ""}},
                "associations": {"combinations": [], "categories": []},
                "position_in_category": [],
                "description_short": {"language": {"value": ""}},
                "description": {"language": {"value": ""}},
                "link_rewrite": {"language": {"value": ""}},
                "meta_title": {"language": {"value": ""}}
            }
        }
        self.product = BaseProduct(self.product_data)

    def test_set_name(self):
        self.product.set_name("Test Product")
        self.assertEqual(self.product_data["product"]["name"]["language"]["value"], "Test Product")

    def test_set_category(self):
        self.product.set_category(5)
        self.assertEqual(self.product_data["product"]["id_category_default"], 5)

    def test_set_price(self):
        with patch('utils.convert_price', return_value=100):
            self.product.set_price(123)
            self.assertEqual(self.product_data["product"]["price"], round(123 / 1.23, 2))

    def test_set_meta_title(self):
        self.product.set_meta_title("Test Meta Title")
        self.assertEqual(self.product_data["product"]["meta_title"]["language"]["value"], "Test Meta Title")

    def test_set_link_name(self):
        self.product.set_link_name("Test Link Name")
        self.assertEqual(self.product_data["product"]["link_rewrite"]["language"]["value"], "test-link-name")

    def test_set_description_short(self):
        self.product.set_description_short("Short Description")
        self.assertEqual(self.product_data["product"]["description_short"]["language"]["value"], "Short Description")

    def test_set_description(self):
        self.product.set_description("Full Description")
        self.assertEqual(self.product_data["product"]["description"]["language"]["value"], "Full Description")

    def test_set_associations(self):
        self.product.set_associations(3, 0)
        self.assertEqual(self.product_data["product"]["associations"]["categories"], 
                         {"category": [{'id': 2}, {'id': 3}, {'id': 0}]})
        self.product.set_associations(3, 4)
        self.assertEqual(self.product_data["product"]["associations"]["categories"], 
                         {"category": [{'id': 2}, {'id': 3}, {'id': 4}]})

    def test_get_product(self):
        self.assertEqual(self.product.get_product(), self.product_data)

    def test_get_from_json(self):
        product_json = {
            "Name": "Test Product",
            "Price": "123,00 zł",
            "Description": "<p>Test Description</p>"
        }
        with patch('utils.convert_price', return_value=100):
            self.product.get_from_json(product_json)
            self.assertEqual(self.product_data["product"]["name"]["language"]["value"], "Test Product")
            self.assertEqual(self.product_data["product"]["price"], 100)
            self.assertEqual(self.product_data["product"]["meta_title"]["language"]["value"], "Test Product")
            self.assertEqual(self.product_data["product"]["link_rewrite"]["language"]["value"], "test-product")
            self.assertEqual(self.product_data["product"]["description_short"]["language"]["value"], "test123")
            self.assertEqual(self.product_data["product"]["description"]["language"]["value"], "<p>Test Description</p>")

class TestBaseCategory(unittest.TestCase):

    def setUp(self):
        self.category_data = {
            "category": {
                "name": {"language": {"value": ""}},
                "description": {"language": {"value": ""}},
                "link_rewrite": {"language": {"value": ""}}
            }
        }
        self.category = BaseCategory(self.category_data)

    def test_set_default_attributes(self):
        self.category.set_default_attributes("Test Category")
        self.assertEqual(self.category_data["category"]["name"]["language"]["value"], "Test Category")
        self.assertEqual(self.category_data["category"]["description"]["language"][0]["value"], "Description for Test Category")
        self.assertEqual(self.category_data["category"]["link_rewrite"]["language"][0]["value"], "test-category")

    def test_set_parent_id(self):
        self.category.set_parent_id(10)
        self.assertEqual(self.category_data["category"]["id_parent"], 10)

    def test_get_name(self):
        self.category.set_default_attributes("Test Category")
        self.assertEqual(self.category.get_name(), "Test Category")

    def test_get_category(self):
        self.assertEqual(self.category.get_category(), self.category_data)

class TestBaseImage(unittest.TestCase):

    def setUp(self):
        self.image = BaseImage("/path/to/images")

    @patch("builtins.open", new_callable=MagicMock)
    @patch("product.Image.open")
    def test_set_image(self, mock_image_open, mock_open):
        mock_image = MagicMock()
        mock_image.convert.return_value = mock_image
        mock_image_open.return_value = mock_image

        self.image.set_image(["folder1/1/image1.jpg", "folder2/1/image2.jpg"])
        images = self.image.get_images()

        self.assertEqual(len(images), 2)
        self.assertEqual(images[0][0], "1-image1.jpg")
        self.assertEqual(images[1][0], "1-image2.jpg")

if __name__ == "__main__":
    unittest.main()