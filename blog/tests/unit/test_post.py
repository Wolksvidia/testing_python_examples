from unittest import TestCase
from blog.post import Post

class Test_Post(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test content', p.content)
        
    def test_joson(self):
        p = Post('Test', 'Test content')
        expected = {'title': 'Test', 'content': 'Test content'}

        self.assertDictEqual(expected, p.json())
