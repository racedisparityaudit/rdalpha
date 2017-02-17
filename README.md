# rdalpha

Repository for the Race Disparity Unit alpha project

## Links

https://rdalpha.herokuapp.com/

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

## Deployment

First create a new heroku app, we are deploying different sprints to separate
apps in order to be able to show how it has evolved.

Set the remote git branch to match your new app
`heroku git:remote -a [your-heroku-app-name]`


You should then be able to deploy with :

`git push heroku master`
or
`git push heroku [your branch]:master`

After a deployment you'll need to run the migrations
with the relevant taxonomy data in taxonomy.csv which is created by the python app
and create all of the relevant tables.

`heroku run rails db:migrate`

Next open a rails console
`heroku run rails c`

Import the database
`TaxonomyImporter.new.import`

Updating the data
If you want to update the data after deploy then you can run some commands
to delete the current taxonomy and reimport taxonomy.csv

`heroku run rails c`
`TaxonomyImporter.new.import`

There is http basic auth, the credentials for this live in production.rb.

you should now be able to do `heroku open` and visit the application in your browser
