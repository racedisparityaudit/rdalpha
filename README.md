# rdalpha

Repository for the Race Disparity Unit alpha project.

## Deployment

First create a new heroku app, we are deploying different sprints to separate
apps in order to be able to show how it has evolved.

Set the remote git branch to match your new app
`heroku git:remote -a [your-heroku-app-name]`


You should then be able to deploy with :

`git push heroku master`


After a deployment you'll need to run the migrations, this will seed the database
with the relevant taxonomy data in taxonomy.csv which is created by the python app
and create all of the relevant tables.

`heroku run rails db:migrate`

There is http basic auth, the credentials for this live in production.rb.

you should now be able to do `heroku open` and visit the application in your browser
