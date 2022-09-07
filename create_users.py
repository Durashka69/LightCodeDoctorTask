import requests

from random import choice

from string import ascii_letters

from faker import Faker


MAX_USERS = 2

fake = Faker()


"""

I wrote this script because i didn't want to create new user all the time by myself

"""


def generate_username():
    nickname = []

    for i in range(10):
        nickname.append(choice(ascii_letters))

    username = ''.join(nickname)

    return username


url = 'http://localhost:8000/api/users/'


for i in range(MAX_USERS):
    data = {
        'username': generate_username(),
        'email': fake.email(),
        'password': 'testpassword',
        'r_password': 'testpassword'
    }

    requests.post(url, data)
    print(data.get('username'))
