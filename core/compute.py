from secrets import token_urlsafe


def generate_short_url():
    url_id = token_urlsafe(6)
    return url_id
