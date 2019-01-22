from unittest import TestCase
from blog.blog import Blog
from blog.post import Post


class TestBlog(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Author')
        b.create_post('Test', 'Test content')
        p = Post('Test', 'Test content')

        self.assertEqual(p.title, b.posts[0].title)
        self.assertEqual(p.content, b.posts[0].content)
        self.assertEqual(1,len(b.posts))

    def test_json_no_posts(self):
        b = Blog('Test', 'Author')
        d = {
            'title': 'Test',
            'author': 'Author',
            'posts': [],
        }

        self.assertDictEqual(d, b.json())

    def test_json(self):
        b = Blog('Test', 'Author')
        b.create_post('Test Post', 'Test content')
        d = {
            'title': 'Test',
            'author': 'Author',
            'posts': [
                {'title': 'Test Post','content': 'Test content',},
            ],
        }

        self.assertDictEqual(d, b.json())