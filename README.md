# rdalpha

Repository for the Racial Disparity Unit alpha project

## Links

https://rdalpha.herokuapp.com/

## Working with the govuk styling

The styling in this project is built on top of the [govuk elements](https://github.com/alphagov/govuk_elements) which
has been included as a submodule. The elements project
itself is built on top the [govuk frontend toolkit](https://github.com/alphagov/govuk_frontend_toolkit/)
project which provides basic building blocks for govuk styling.

### Usage


Edit the files in web/app/static/scss and use the command
`sass --watch "/path/to/scss/source/folder":"/path/to/css/target/folder"`.

This will automatically recompile changes made in the scss files to static css files
which can then be used as normal css files. Beware any changes made directly to the css
files will be overwritten by changes made to the relevant scss file.


## Infrastructure

In this section we can add quick notes about infrastructure as we go. The aim is to capture all the details and then clean up / restructure later.

By capturing it in here rather than in other mediums we reduce risk of this info being lost going forward. Also by documenting as we go we make sure something is captured vs trying to remember steps later.

Heroku Account
- Set up heroku account.
- calum.eadie@methodsdigital.co.uk
- Strong password stored in KeePassX.
- Set up two factor authentication (Google Authenticator).

Heroku App
- rdalpha
- europe

