from pocketbase import PocketBase
from getpass import getpass

pb = PocketBase('https://tito.pockethost.io/')

username_email = input('Username or Email: ')
password = getpass('Password: ')

pb.collection('users').auth_with_password(
    username_email,
    password
)

if pb.auth_store.token == None:
    print('Failed to Login')
else:
    print(f'Welcome back, {pb.auth_store.base_model.username}')

