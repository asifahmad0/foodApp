# foodApp
================================================
File: README.md
================================================
# foodApp

================================================
File: foodProject/build_files.sh
================================================
echo "BUILD START"
 python3.12.6 -m pip install -r requirements.txt
 python3.12.6 manage.py collectstatic --noinput --clear
 echo "BUILD END"

================================================
File: foodProject/manage.py
================================================
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodProject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


================================================
File: foodProject/requirements.txt
================================================
﻿asgiref==3.8.1
Django==5.1.4
djangorestframework==3.15.2
drf-yasg==1.21.8
inflection==0.5.1
packaging==24.2
pillow==11.1.0
pytz==2024.2
PyYAML==6.0.2
sqlparse==0.5.3
tzdata==2024.2
uritemplate==4.1.1
python==3.12.6


================================================
File: foodProject/vercel.json
================================================
{
    "builds": [{
        "src": "foodProject/wsgi.py",
        "use": "@vercel/python",
        "config": { "maxLambdaSize": "15mb", "runtime": "python3.12.6" }
    },
    {
        "src": "build_files.sh",
        "use": "@vercel/static-build",
        "config": { "distDir": "staticfiles_build" }
    }],
    "routes": [
        {
            "src": "/(.*)",
            "dest": "/manage.py"
        },
        {
            "src": "/(.*)",
            "dest": "foodProject/wsgi.py"
 }
]
}



================================================
File: .github/workflows/django.yml
================================================
name: Django CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: [3.7, 3.8, 3.9, 3.12.6]

    steps:
    - uses: actions/checkout@v4
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v3
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run Tests
      run: |
        python manage.py test


