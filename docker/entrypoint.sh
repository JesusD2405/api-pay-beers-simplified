#!/bin/bash

set -e
echo "***--------------------------- Install Dependencies ---------------------------***"
pip3 install -r requirements.txt

echo "***--------------------------- Run Tests ---------------------------***"
python manage.py test tests.stock.stockTest

echo "***--------------------------- Run Server ---------------------------***"
if  [[ $RUN_MODE == "PROD" ]]; then
  gunicorn payBeersSimplified.wsgi:application -w $GUNICORN_WORKERS -b :8000;
else
  python manage.py runserver 0.0.0.0:8000;
fi
