"""Settings for emencia.django.newsletter"""
import string
from django.conf import settings

USE_WORKGROUPS = getattr(settings, 'NEWSLETTER_USE_WORKGROUPS', False)
USE_UTM_TAGS = getattr(settings, 'NEWSLETTER_USE_UTM_TAGS', True)

MAILER_HARD_LIMIT = getattr(settings, 'NEWSLETTER_MAILER_HARD_LIMIT', 10000)

INCLUDE_UNSUBSCRIPTION = getattr(settings, 'NEWSLETTER_INCLUDE_UNSUBSCRIPTION', True)

UNIQUE_KEY_LENGTH = getattr(settings, 'NEWSLETTER_UNIQUE_KEY_LENGTH', 8)
UNIQUE_KEY_CHAR_SET = getattr(settings, 'NEWSLETTER_UNIQUE_KEY_CHAR_SET', string.ascii_uppercase + string.digits)

DEFAULT_HEADER_REPLY = getattr(settings, 'NEWSLETTER_DEFAULT_HEADER_REPLY', 'Emencia Newsletter<noreply@emencia.com>')
DEFAULT_HEADER_SENDER = getattr(settings, 'NEWSLETTER_DEFAULT_HEADER_SENDER', 'Emencia Newsletter<noreply@emencia.com>')

TRACKING_LINKS = getattr(settings, 'NEWSLETTER_TRACKING_LINKS', True)

# you may use gif with 
# 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='
TRACKING_IMAGE_FORMAT = getattr(settings, 'NEWSLETTER_TRACKING_IMAGE_FORMAT',
                                'png')
TRACKING_IMAGE = getattr(settings, 'NEWSLETTER_TRACKING_IMAGE',
                 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAAZiS0dEAP8A\n/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB9sDDwgsKd5+jrAAAAAZdEVYdENv\nbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAADUlEQVQI12NgYGBgAAAABQABXvMqOgAAAABJ\nRU5ErkJggg==')

MEDIA_URL = getattr(settings, 'NEWSLETTER_MEDIA_URL', '/edn/')

NEWSLETTER_BASE_PATH = getattr(settings, 'NEWSLETTER_BASE_PATH', 'uploads/newsletter')
