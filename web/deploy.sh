#!/bin/bash

#
# Deploy the app.
#
# Break this out into a script to document the process for someone new
# to heroku and so we can bring in extra tasks in the future. E.g.
# data processing, publishing to many different release channels
# so that user researchers can use a stable version whilst devs work on
# a dev version.
#

# Make script more robust by failing when there are empty variables or
# a particular command fails.
set -o nounset
set -o errexit

# Make sure we're at the root of the repo.
prog_dir=$(dirname $0)
cd $prog_dir/..

# Normally you use "git push heroku master" in heroku.
# We're likely going to be building all sorts in this repo so
# we use the following to put our app into a sub directory.
#git subtree push --prefix web heroku master
git push heroku `git subtree split --prefix web master`:master --force

heroku run python manage.py migrate