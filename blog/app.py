from blog import Blog
from post import Post

MENU_MSG = 'Enter "c" to create a blob, "l" to list blogs, "r" to read a blog, "p" to create a post, or "q" to quit.'
blogs = dict() #blog_name : blog object

def menu():
    
    selection = input(MENU_MSG)
    while selection != 'q':
        if selection == 'c':
            create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            read_blog()
        elif selection == 'p':
            create_post()
        selection = input(MENU_MSG)

def create_blog():
    title = input('Ingrese el titulo del blog.')
    author = input('Ingrese el nombre del autor.')
    blogs[title] = Blog(title,author)

def create_post():
    title = input('Ingrese el titulo del blog.')
    title_post = input('Ingrese el titulo del post.')
    content = input('Ingrese el contenido del post.')
    
    blogs[title].create_post(title_post,content)

def read_blog():
    title = input('Ingrese el titulo del blog.')
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(f'- {post.title} -- {post.content}')

def print_blogs():
    for key, blog in blogs.items():
        #print(f'- {key}')
        print(f'- {blog}')

if __name__ == "__main__":
    menu()