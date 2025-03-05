INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #THIRD PARTY APPS
    'rest_framework',
    'corsheaders',
    'drf_yasg',
    
    #LOCAL APPS
    'apps.accounts',
    'apps.companies',
    'rest_framework_simplejwt',
]