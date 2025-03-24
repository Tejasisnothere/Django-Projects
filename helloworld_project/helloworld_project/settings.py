import os
from pathlib import Path
import dj_database_url

# ✅ Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Secret Key (Use Environment Variable)
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 's3cr3t-k3y-8yH&!9x@4A#rTtY')

# ✅ Debug Mode (Keep False in Production)
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# ✅ Allowed Hosts (Include Railway domain & localhost)
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost,django-projects-production-0299.up.railway.app').split(',')

# ✅ Installed Apps
INSTALLED_APPS = [
    "pages.apps.PagesConfig",  # Custom App
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",  # Whitenoise for Static Files
]

# ✅ Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # Whitenoise for Static Files
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ✅ Root URLs
ROOT_URLCONF = "helloworld_project.urls"

# ✅ Templates (Fixed Directory Name)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],  # ✅ Fixed Typo
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ✅ WSGI Application
WSGI_APPLICATION = "helloworld_project.wsgi.application"

# ✅ Database (Using Railway PostgreSQL)
DATABASES = {
    "default": dj_database_url.config(default=os.getenv("DATABASE_URL", "sqlite:///db.sqlite3"))
}

# ✅ Static Files (For Production)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# ✅ Default Primary Key Type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
