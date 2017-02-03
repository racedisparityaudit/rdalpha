#!/bin/bash

#
# This script allows us to very quickly get a common development environment
# set up on our machines.
#
# We're assuming everyone is on Mac.
#
# For example, it allows us to install particular versions of Python
# or data manipulation tooling.
#

# Make script more robust by failing when there are empty variables or
# a particular command fails.
set -o errexit

# Make sure we're at the root of the repo.
prog_dir=$(dirname $0)
cd $prog_dir

# Make sure that we're all using the same versions of common tools.
brew update
brew upgrade

# Install system packages (not using a Brewfile to keep all this setup stuff
# contained within this file).
brew install python3

# Install python packages (again not using requirements.txt to keep general
# dev env setup seperate from the individuals projects in this repo).
pip3 install virtualenv

# Set up a virtualenv to work within.
virtualenv -p python3 venv

# Start up the virtual env.
source venv/bin/activate
