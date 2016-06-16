demo-slackbot
=============

This is a simple Slack bot using
[aslack](http://pythonhosted.org/aslack/), intended to show how to
write a bot in Python and deploy it to Heroku.  The basic idea is that
you add appropriately edited versions of Procfile, app.json,
requirements.txt, and runtime.txt to your repo, make a bot
integration, invite your bot to a channel, and then:

    heroku create
    heroku config:set SLACK_API_TOKEN=yourtokenhere
    heroku config:get SLACK_API_TOKEN -s >> .env

To run locally:

    heroku local

To run on Heroku:

    git push heroku master
    heroku ps:scale worker=1

To turn it off:

    heroku ps:scale worker=0
