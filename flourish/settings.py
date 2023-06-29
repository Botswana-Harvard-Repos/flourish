"""
Django settings for flourish project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import configparser
import os
from pathlib import Path
import sys

from django.core.management.color import color_style

style = color_style()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r2+kl0ci5#p_h4(e4edde8zko5ch%pp^jc-3z%rvh@fzmtv%09'

SITE_ID = 40

DEFAULT_STUDY_SITE = 40

REVIEWER_SITE_ID = 1

APP_NAME = 'flourish'

LOGIN_REDIRECT_URL = 'home_url'

INDEX_PAGE = 'flourish.bhp.org.bw'

# AUTO_CREATE_KEYS = True

ETC_DIR = os.path.join('/etc/', APP_NAME)
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# KEY_PATH = os.path.join(BASE_DIR, 'crypto_fields')
# KEY_PATH = os.path.join(ETC_DIR, 'crypto_fields')

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'flourish.bhp.org.bw', '10.113.201.239', '192.168.8.102']

CONFIG_FILE = f'{APP_NAME}.ini'

CONFIG_PATH = os.path.join(ETC_DIR, CONFIG_FILE)
sys.stdout.write(style.SUCCESS(f'  * Reading config from {CONFIG_FILE}\n'))
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crypto_fields.apps.AppConfig',
    'django_q',
    'django_tables2',
    'django_extensions',
    'crispy_forms',
    'multiselectfield',
    'edc_action_item.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_model_admin.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_reference.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'edc_call_manager.apps.AppConfig',
    'edc_metadata_rules.apps.AppConfig',
    # "accounts.apps.AccountsConfig",
    'flourish_export.apps.AppConfig',
    'flourish_dashboard.apps.AppConfig',
    'flourish_prn.apps.AppConfig',
    'flourish_caregiver.apps.AppConfig',
    'flourish_child.apps.AppConfig',
    'flourish_follow.apps.AppConfig',
    'pre_flourish_follow.apps.AppConfig',
    'flourish_reports.apps.AppConfig',
    'flourish_metadata_rules.apps.AppConfig',
    'flourish_labs.apps.AppConfig',
    'flourish_reference.apps.AppConfig',
    'flourish_visit_schedule.apps.AppConfig',
    'flourish.apps.EdcAppointmentAppConfig',
    'flourish.apps.EdcBaseAppConfig',
    'flourish.apps.EdcDataManagerAppConfig',
    'flourish.apps.EdcFacilityAppConfig',
    'flourish.apps.EdcLocatorAppConfig',
    'flourish.apps.EdcMetadataAppConfig',
    'flourish.apps.EdcOdkAppConfig',
    'flourish.apps.EdcProtocolAppConfig',
    'flourish.apps.EdcVisitTrackingAppConfig',
    'flourish.apps.EdcTimepointAppConfig',
    'flourish.apps.EdcSenaiteInterfaceAppConfig',
    'pre_flourish.apps.AppConfig',
    'flourish_calendar.apps.AppConfig',
    'flourish.apps.AppConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'cacheops',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
    
]

ROOT_URLCONF = 'flourish.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'flourish.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
mysql_config = configparser.ConfigParser()
mysql_config.read(os.path.join(ETC_DIR, 'mysql.ini'))

HOST = mysql_config['mysql']['host']
DB_USER = mysql_config['mysql']['user']
DB_PASSWORD = mysql_config['mysql']['password']
DB_NAME = mysql_config['mysql']['database']
PORT = mysql_config['mysql']['port']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': HOST,  # Or an IP Address that your DB is hosted on
        'PORT': PORT,
    }
}

# DATABASES = {
# 'default': {
# 'ENGINE': 'django.db.backends.sqlite3',
# 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
# }
# }

ODK_SERVER_TYPE = 'central'
ODK_CONFIGURATION = {
    'OPTIONS': {
        'read_default_file': '/etc/odk/odk.cnf',
    },
}

SENAITE_CONFIGURATION = {
    'OPTIONS': {
        'read_default_file': '/etc/edc_senaite_interface/senaite.conf',
    },
}

# Email configurations
EMAIL_BACKEND = config['email_conf'].get('email_backend')
EMAIL_HOST = config['email_conf'].get('email_host')
EMAIL_USE_TLS = config['email_conf'].get('email_use_tls')
EMAIL_PORT = config['email_conf'].get('email_port')
DEFAULT_FROM_EMAIL = config['email_conf'].get('email_from')
EMAIL_HOST_USER = config['email_conf'].get('email_host_user')
EMAIL_HOST_PASSWORD = config['email_conf'].get('email_host_pwd')

# Celery configurations
CELERY_TIMEZONE = 'Africa/Gaborone'
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_INCLUDE = ['flourish_child.utils', 'edc_odk.tasks', ]
# CELERY_RESULT_BACKEND = 'file:///etc/celery/results'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

BASE_FORMAT = 'https://%(host)s/v1/projects/2/forms/%(form_id)s/%(api)s'

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
    ('tn', 'Setswana'),
    ('en', 'English'))

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DEVICE_ID = config['edc_device'].get('device_id', '99')
DEVICE_ROLE = config['edc_device'].get('role')

CELLPHONE_REGEX = '^[7]{1}[12345678]{1}[0-9]{6}$'
TELEPHONE_REGEX = '^[2-8]{1}[0-9]{6}$'

DASHBOARD_URL_NAMES = {
    'child_dashboard_url': 'flourish_dashboard:child_dashboard_url',
    'child_listboard_url': 'flourish_dashboard:child_listboard_url',
    'child_screening_listboard_url': 'flourish_dashboard:child_screening_listboard_url',
    'subject_listboard_url': 'flourish_dashboard:subject_listboard_url',
    'data_manager_listboard_url': 'edc_data_manager:data_manager_listboard_url',
    'maternal_screening_listboard_url': 'flourish_dashboard:maternal_screening_listboard_url',
    'maternal_dataset_listboard_url': 'flourish_dashboard:maternal_dataset_listboard_url',
    'pre_flourish_caregiver_locator_listboard_url': 'pre_flourish:pre_flourish_caregiver_locator_listboard_url',
    'flourish_follow_listboard_url': 'flourish_follow:flourish_follow_listboard_url',
    'flourish_follow_appt_listboard_url': 'flourish_follow:flourish_follow_appt_listboard_url',
    'flourish_follow_booking_listboard_url': 'flourish_follow:flourish_follow_booking_listboard_url',
    'flourish_follow_book_listboard_url': 'flourish_follow:flourish_follow_book_listboard_url',
    'subject_dashboard_url': 'flourish_dashboard:subject_dashboard_url',
    'odk_listboard_url': 'edc_odk:odk_listboard_url',
    'export_listboard_url': 'flourish_export:export_listboard_url',
    'flourish_calendar_url': 'flourish_calendar:calendar',
    # pre flourish urls
    'pre_flourish_screening_listboard_url': 'pre_flourish:pre_flourish_screening_listboard_url',
    'pre_flourish_consent_listboard_url': 'pre_flourish:pre_flourish_consent_listboard_url',
    'pre_flourish_child_listboard_url': 'pre_flourish:pre_flourish_child_listboard_url',
    'pre_flourish_subject_dashboard_url': 'pre_flourish:pre_flourish_subject_dashboard_url',
    'pre_flourish_maternal_dataset_listboard_url': 'pre_flourish:pre_flourish_maternal_dataset_listboard_url',
    'pre_flourish_child_dashboard_url': 'pre_flourish:pre_flourish_child_dashboard_url',
    'pre_flourish_follow_listboard_url': 'pre_flourish_follow:pre_flourish_follow_listboard_url',
    'pre_flourish_follow_appt_listboard_url': 'pre_flourish_follow:pre_flourish_follow_appt_listboard_url',
    'pre_flourish_follow_booking_listboard_url': 'pre_flourish_follow:pre_flourish_follow_booking_listboard_url',
    'pre_flourish_follow_book_listboard_url': 'pre_flourish_follow:pre_flourish_follow_book_listboard_url',
    # Senaite Interface URLs
    # Use caregiver result listboard as default/entry listboard.
    'senaite_result_listboard_url': 'flourish_dashboard:caregiver_result_listboard_url',
    'child_result_listboard_url': 'flourish_dashboard:child_result_listboard_url',
     'missing_crf_report_url': 'flourish_reports:missing_crf_report_url',
}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'flourish/base.html',
    'dashboard_base_template': 'flourish/base.html',
    'child_subject_dashboard_template': 'flourish_dashboard/child_subject/dashboard.html',
    'child_listboard_template': 'flourish_dashboard/child_subject/listboard.html',
    'subject_listboard_template': 'flourish_dashboard/maternal_subject/listboard.html',
    'subject_dashboard_template': 'flourish_dashboard/maternal_subject/dashboard.html',
    'data_manager_listboard_template': 'edc_data_manager/listboard.html',
    'maternal_screening_listboard_template': 'flourish_dashboard/screening/maternal_listboard.html',
    'maternal_dataset_listboard_template': 'flourish_dashboard/maternal_dataset/maternal_listboard.html',
    'pre_flourish_caragiver_locator_listboard_template': 'pre_flourish/caregiver_locator_listboard.html',
    'flourish_follow_listboard_template': 'flourish_follow/follow_listboard.html',
    'flourish_follow_appt_listboard_template': 'flourish_follow/appointments_windows_listboards.html',
    'flourish_follow_booking_listboard_template': 'flourish_follow/bookings_listboard.html',
    'flourish_follow_book_listboard_template': 'flourish_follow/book_listboard.html',
    'pre_flourish_child_listboard_template': 'pre_flourish/child/child_listboard.html',
    'pre_flourish_subject_dashboard_template': 'pre_flourish/caregiver/dashboard.html',
    'pre_flourish_child_dashboard_template': 'pre_flourish/child/dashboard.html',
    'pre_flourish_screening_listboard_template': 'pre_flourish/caregiver/listboard.html',
    'pre_flourish_subject_listboard_template': 'pre_flourish/caregiver/subject_listboard.html',
    'child_screening_listboard_template': 'flourish_dashboard/child_subject/screening_listboard.html',
    'odk_listboard_template': 'edc_odk/odk_forms/listboard.html',
    'export_listboard_template': 'flourish_export/listboard.html',
    # Preflourish_follow_templates
    'pre_flourish_follow_listboard_template': 'pre_flourish_follow/follow_listboard.html',
    'pre_flourish_follow_appt_listboard_template': 'pre_flourish_follow/appointments_windows_listboards.html',
    'pre_flourish_follow_booking_listboard_template': 'pre_flourish_follow/bookings_listboard.html',
    'pre_flourish_follow_book_listboard_template': 'pre_flourish_follow/book_listboard.html',
    # Override senaite result template
    'senaite_result_listboard_template': 'flourish_dashboard/result_listboard.html',
    'missing_crf_report_template': 'flourish_reports/missing_crfs/missing_crf_report.html',
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'flourish', 'static')

HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')
COUNTRY = 'botswana'

PARENT_REFERENCE_MODEL1 = ''
PARENT_REFERENCE_MODEL2 = ''

# Date and time format
SHORT_DATE_FORMAT = 'Y-m-d'
SHORT_DATETIME_FORMAT = 'Y-m-d h:m'
DATE_FORMAT = 'Y-m-d'

CACHEOPS_REDIS = "redis://localhost:6379/1"


CACHEOPS = {
    'flourish_caregiver.*': {'ops': 'all', 'timeout': 60*60*24},
    'flourish_child.*': {'ops': 'all', 'timeout': 60*60*24},
    'flourish_prn.*': {'ops': 'all', 'timeout': 60*60*24},
    'flourish_follow.*': {'ops': 'all', 'timeout': 60*60*24},
    'flourish_calendar.*': {'ops': 'all', 'timeout': 60*60*24},
    'flourish_child.models.child_appointment.Appointment': None,
    'edc_appointments.*': None,
    '*.*': {'timeout': 60*60},
}

if 'test' in sys.argv:
    class DisableMigrations:

        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None


    MIGRATION_MODULES = DisableMigrations()
    PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)
    DEFAULT_FILE_STORAGE = 'inmemorystorage.InMemoryStorage'
