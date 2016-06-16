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

Python versions
---------------
At the moment, [supported Python runtimes](https://devcenter.heroku.com/articles/python-runtimes#supported-python-runtimes) (specified in runtime.txt) are `python-2.7.11` and `python-3.5.1`.  If you're using aslack, you need to use the latter.

Setting up the heroku CLI
-------------------------
Install the [Heroku Toolbelt](https://toolbelt.heroku.com/).