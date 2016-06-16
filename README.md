demo-slackbot
=============

This is a simple Slack bot using
[aslack](http://pythonhosted.org/aslack/), intended to show how to
write a bot in Python and deploy it to Heroku.  The basic idea is that
you add appropriately edited versions of Procfile, app.json,
requirements.txt, and runtime.txt to your repo, make a bot
integration, invite your bot to a channel, and then:

    heroku create

To run locally:

    export SLACK_API_TOKEN=yourtokenhere
    heroku local

To run on Heroku:

    heroku config:set SLACK_API_TOKEN=yourtokenhere
    git push heroku master
    heroku ps:scale worker=1

To turn it off:

    heroku ps:scale worker=0
