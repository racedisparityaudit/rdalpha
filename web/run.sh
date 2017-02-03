#!/bin/bash

#
# Run the app locally.
#

# Make script more robust by failing when a particular command fails.
set -o errexit

# Make sure we're at the root of the repo.
prog_dir=$(dirname $0)
cd $prog_dir/..

# Make sure we're in the virtualenv and have installed dependancies.
# We have to ignore our robustness code above to get this to work.
source venv/bin/activate

cd web
# automatically compile scss to css
sass --watch app/static/scss/:app/static/css &

pip install -r requirements.txt

# Run!
python manage.py runserver

