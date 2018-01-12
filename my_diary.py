import datetime
import sys
import os
from collections import OrderedDict

from peewee import *

getdb = SqliteDatabase('diary.db')

def initial():
    getdb.connect()
    getdb.create_tables([Diary], safe=True)


class Diary(Model):
    content = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = getdb

def main():
    clear()
    initial()
    show_menu()

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_menu():
    """ your main menu """
    choice = None

    while choice != 'y':
        print("Enter 'q' to quit.")
        for key,value in user_menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Choose your letter: ').lower().strip()

        if choice in user_menu:
            user_menu[choice]()

def show_posts(s=None):
    """ Show your posts """
    posts = Diary.select().order_by(Diary.created_date.desc())

    if s:
        posts = posts.select().where(Diary.content.contains(s))

    for post in posts:
        print('\nYour post diary nr {}:'.format(str(post.id)))
        print('\n'+post.content+'\n\nPosted on date: '+post.created_date.strftime('%A %B %d, %Y %I:%M%p'))
        print('\n\n**************************\n\n')

def search_posts():
    """ Serch in posts"""
    s = input('what are you looking for? ')
    show_posts(s)

def delete_post():
    """ Delete post """
    d = input('Give number of one post you whant to delete')
    post  = Diary.get(Diary.id == int(d))
    post.delete_instance()

def insert_posts():
    """ Insert new post """
    print("Enter post content. Press ctrl+d when finished.")
    data = sys.stdin.read().strip()

    if data:
        if input('Save entry? [Yn] ').lower() != 'n':
            Diary.create(content=data)
            print("Saved successfully!")

user_menu = OrderedDict([
    ('a', insert_posts),
    ('s', show_posts),
    ('h', search_posts),
    ('d', delete_post),
])


if __name__ == '__main__':
    main()
