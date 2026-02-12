from .base import *  # noqa: F403

DEBUG = False
ALLOWED_HOSTS = ["tavcms.example.com"]
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
