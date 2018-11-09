from unittest import TestCase
from unittest.mock import patch
from blog import app
from blog.blog import Blog
from blog.post import Post

class TestApp(TestCase):
    def setUp(self):
        """"El metodo es llamado antes de correr los test, por lo que se puede utilizar para 
        inicializacion de datos utiles para los tests a ejecutar"""
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('blog.app.create_blog') as mocked_create_blog:
                mocked_input.side_effect = ['c', 'q']
                app.menu()
                mocked_create_blog.assert_called()

    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_MSG)

    def test_menu_calls_print_blogs(self):
        with patch('blog.app.print_blogs') as mocked_print_blog:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('l', 'q')
                app.menu()
                mocked_print_blog.assert_called()

    def test_print_blog(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Blog(title=Test, author=Test Author)')

    def test_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author') #retorna los valores pasados incrementalmente cuando el input es llamado
            app.create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))

    def test_read_blog(self):
        with patch('builtins.input', return_value='Test'):
            with patch('blog.app.print_posts') as mocked_print_posts:
                app.read_blog()
                mocked_print_posts.assert_called_with(app.blogs['Test'])
    
    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Test Post', 'Test Content')
        with patch('blog.app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])
            
    def test_print_post(self):
        post = Post('Test Post', 'Test Content')
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with('- Test Post -- Test Content')

    def test_creat_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Post', 'Test Content')
            app.create_post()
            self.assertEqual(app.blogs['Test'].posts[0].title, 'Test Post')
            self.assertEqual(app.blogs['Test'].posts[0].content, 'Test Content')

