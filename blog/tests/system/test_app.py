from unittest import TestCase
from unittest.mock import patch
from blog import app
from blog.blog import Blog

class TestApp(TestCase):

    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_MSG)

    def test_menu_calls_print_blogs(self):
        with patch('blog.app.print_blogs') as mocked_print_blog:
            with patch('builtins.input', return_value='l'):
                app.menu()
                mocked_print_blog.assert_called()

    def test_print_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Blog(title=Test, author=Test Author)')

    def test_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author') #retorna los valores pasados incrementalmente cuando el input es llamado
            app.create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))
