from datetime import datetime

class Author:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Author: {self.name}"


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.title}\n{self.content}\n{self.author} - {self.timestamp}"


class Blog:
    def __init__(self, name):
        self.name = name
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Added post '{post.title}' to the blog.")

    def display_posts_by_author(self, author):
        author_posts = [post for post in self.posts if post.author == author]
        if not author_posts:
            print(f"No posts found for author {author}.")
        else:
            print(f"Posts by {author}:")
            for post in author_posts:
                print(post)

    def display_latest_posts(self, num_posts=5):
        if not self.posts:
            print("The blog has no posts.")
        else:
            print(f"Latest {num_posts} posts:")
            sorted_posts = sorted(self.posts, key=lambda post: post.timestamp, reverse=True)[:num_posts]
            for post in sorted_posts:
                print(post)

author1 = Author("Alice")
author2 = Author("Bob")

blog = Blog("Tech Blog")

post1 = Post("Introduction to Python", "Python is a versatile programming language.", author1)
post2 = Post("Web Development with Django", "Learn web development with Django framework.", author1)
post3 = Post("Machine Learning Basics", "An overview of machine learning concepts.", author2)
post4 = Post("Tips for Productive Coding", "Improve your coding productivity with these tips.", author1)

blog.add_post(post1)
blog.add_post(post2)
blog.add_post(post3)
blog.add_post(post4)

blog.display_posts_by_author(author1)
blog.display_latest_posts(3)
