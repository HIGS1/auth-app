from pocketbase import PocketBase
from .user import User


class PB_Manager:
    def Initialize() -> None:
        PB_Manager._pb = PocketBase('https://gato.pockethost.io/')
        PB_Manager.user = None

    def login(username_email, password) -> User | str:
        try:
            PB_Manager._pb.collection('users').auth_with_password(
                username_email, password)
        except:
            return 'Failed to authenticate'

        PB_Manager.user = User(
            id=PB_Manager._pb.auth_store.model.id,
            username=PB_Manager._pb.auth_store.model.username,
            email=PB_Manager._pb.auth_store.model.email,
            verified=PB_Manager._pb.auth_store.model.verified,
            profile_pic_url=PB_Manager._pb.auth_store.model.avatar,
        )

        return PB_Manager.user

    def register(username, email, password) -> None | str:
        try:
            result = PB_Manager._pb.collection('users').create({
                'username': username,
                'email': email,
                'password': password,
                'passwordConfirm': password,
                'emailVisibility': False,
            })
            print(result.__dict__)
        except Exception:
            print('Failed to Sign Up a new account')
            return 'Failed to Sign Up a new account'

        return None

    def verify_user() -> None:
        if PB_Manager.user.verified == True:
            return
        try:
            PB_Manager._pb.collection(
                'users').requestVerification(PB_Manager.user.email)
        except:
            print('Something went wrong while requesting account verification')

        print('Verfication E-mail sent')

    def send_password_reset_email(email: str) -> None | str:
        try:
            PB_Manager._pb.collection('users').requestPasswordReset(email)
        except:
            print('Something went wrong while requesting a password reset.')
            return 'Something went wrong while requesting a password reset.'
