INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    'turfbooking',
]

STATIC_URL = '/static/'

# Optional for production
STATICFILES_DIRS = [
    BASE_DIR / "turfbooking/static",
]
