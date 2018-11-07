blogs = dict() #blog_name : blog object

def menu():
    print_blogs()

def print_blogs():
    for key, blog in blogs:
        print(key)
        print(blog)
