from unittest import TestCase
from models.item import ItemModel


class TestItemModel(TestCase):
    def test_create_item(self):
        item = ItemModel('Test',10)
        self.assertIsInstance(item, ItemModel)
        self.assertEqual(item.name, 'Test')
        self.assertEqual(item.price, 10)
    
    def test_json(self):
        item = ItemModel('Test',10)
        self.assertEqual(item.json(), {'name': 'Test', 'price': 10})

