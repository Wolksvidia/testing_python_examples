from unittest import TestCase
from blog.blog import Blog


class Test_Blog(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Author')

        self.assertEqual('Test', b.title)
        self.assertEqual('Author', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Test', 'Author')

        self.assertEqual(b.__repr__(), 'Blog(title=Test, author=Author)')
