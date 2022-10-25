import json
import os
import secrets
from dotenv import load_dotenv

load_dotenv()


class Config:

    COMPANY_INSTAGRAM = os.getenv("COMPANY_INSTAGRAM", "")
    COMPANY_NAME = os.getenv("COMPANY_NAME", "")
    COMPANY_LOGO = os.getenv("COMPANY_LOGO", "")
    COMPANY_SLOGAN = os.getenv("COMPANY_SLOGAN", "")
    COMPANY_TIKTOK = os.getenv("COMPANY_TIKTOK", "")
    COMPANY_TWITTER = os.getenv("COMPANY_TWITTER", "")
    COMPANY_URL = os.getenv("COMPANY_URL", "")
    DEBUG = True
    GITHUB_SECRET = os.getenv("GITHUB_SECRET")
    JSON_SORT_KEYS = False  # do not alphabetically sort in jsonfiy method.
    MAIL_SERVER = os.getenv("MAIL_SERVER", "")
    MAIL_PORT = os.getenv("MAIL_PORT", "")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", "")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", "")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "")
    MAIL_USE_SSL = os.getenv("MAIL_USE_SSL", "")
    LNBITS_API_KEY = os.getenv("LNBITS_API_KEY")  # wallet address
    LNBITS_VERSION = os.getenv("LNBITS_VERSION")
    LNBITS_WEBHOOK = os.getenv("LNBITS_WEBHOOK")
    SECRET_KEY = secrets.token_urlsafe(32)  # secret key
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_ECHO = False  # what does this do?
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # what does this do?
    TESTING = True
