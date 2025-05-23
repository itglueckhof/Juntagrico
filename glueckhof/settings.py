"""
Django settings for glueckhof project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'False')=='True'

ALLOWED_HOSTS = ['glueckhof.juntagrico.science', 'localhost', 'mein.glueck-hof.ch']

ADMINS = (
    ('Admin', os.environ.get('JUNTAGRICO_ADMIN_EMAIL')),
)
MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'glueckhof',
    'juntagrico',
    'fontawesomefree',
    'import_export',
    'impersonate',
    'crispy_forms',
    'adminsortable2',
    'polymorphic',
]

IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'view'

ROOT_URLCONF = 'glueckhof.urls'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','glueckhof.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'), #''junatagrico', # The following settings are not used with sqlite3:
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'), #''junatagrico',
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'), #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False), #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'juntagrico.context_processors.vocabulary',
            ],
            'debug': DEBUG
        },
    },
]

WSGI_APPLICATION = 'glueckhof.wsgi.application'


LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

USE_TZ = True
TIME_ZONE = 'Europe/Zurich'

DATE_INPUT_FORMATS =['%d.%m.%Y',]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
    
]

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

WHITELIST_EMAILS = []

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)
            


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

LOGIN_REDIRECT_URL = "/"

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = 'media'

"""
     Crispy Settings
"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'

"""
     juntagrico Settings
"""
ORGANISATION_NAME = "Glück-Hof"
ORGANISATION_LONG_NAME = "Glück-Hof"
ORGANISATION_ADDRESS = {"name":"Glück-Hof", 
            "street" : "Baldegg",
            "number" : "5",
            "zip" : "5400",
            "city" : "Baden",
            "extra" : ""}
ORGANISATION_BANK_CONNECTION = {"PC" : "-",
            "IBAN" : "CH3000769010951601158",
            "BIC" : "FRGGCHB1XXX",
            "NAME" : "Freie Gemeinschaftsbank Genossenschaft",
            "ESR" : ""}
SHARE_PRICE = "250"

REQUIRED_SHARES = 0

ALLOW_JOB_UNSUBSCRIBE = True

DEFAULT_FROM_EMAIL = "solawi@glueck-hof.ch"
CONTACTS = {
    "general": "solawi@glueck-hof.ch"
}
ORGANISATION_WEBSITE = {
    'name': "www.glueck-hof.ch",
    'url': "https://www.glueck-hof.ch"
}
STYLES = {'static': ['glueckhof/css/customize.css']}

# Anpassung Geschäftsjahr = Startdatum
BUSINESS_YEAR_START = {"day":1, "month":5}

# Depoliste Generierung
DEPOT_LIST_GENERATION_DAYS = [0]

# Anpassung der Begriffe.
VOCABULARY = {
    'subscription' : 'Ernte-Anteil',
    'subscription_pl' : 'Ernte-Anteile',
    'co_member' : 'Mitabonnent',
    'co_member_pl' : 'Mitabonnenten',
}

# Abrechnung der Einsätze nach Stunden.
ASSIGNMENT_UNIT = "HOURS"

# Anpassung der Böhnli Bilder:
IMAGES = {'status_100': '/static/glueckhof/img/Kleeblatt_100.png',
    'status_75': '/static/glueckhof/img/Kleeblatt_75.png',
    'status_50': '/static/glueckhof/img/Kleeblatt_50.png',
    'status_25': '/static/glueckhof/img/Kleeblatt_25.png',
    'status_0': '/static/glueckhof/img/Kleeblatt_0.png',
    'single_full': '/static/glueckhof/img/Kleeblatt_full.png',
    'single_empty': '/static/glueckhof/img/Kleeblatt_empty.png',
    'single_core': '/static/glueckhof/img/Kleeblatt_core.png',
    'core': '/static/glueckhof/img/Kleeblatt_core.png',}


# Anpassung der Emails
EMAILS = {
    'welcome': 'mails/member_welcome.txt',
    'co_welcome': 'mails/co_member_welcome.txt',
    's_created': 'mails/share_created.txt',
}

# Statuten / Betriebsreglement
BYLAWS = "https://drive.google.com/file/d/1XotlJ92YfoiXHtUlsvJXFzA4tgShKTD-/view?usp=sharing"

