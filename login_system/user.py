from requests import get


class User:
    def __init__(
            self,
            id: str,
            username: str,
            email: str,
            profile_pic_url: str,
            verified: bool
    ) -> None:
        self.id = id
        self.username = username
        self.email = email
        self.verified = verified
        self.profile_pic_url = profile_pic_url

    def get_profile_pic(self) -> bytes:
        try:
            r = get(self.profile_pic_url)

            return r.content
        except Exception as e:
            print(e)
