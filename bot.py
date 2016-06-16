# a demo aslack bot for deployment to Heroku

import logging
import asyncio
from aslack.slack_bot import SlackBot
from collections import OrderedDict
from textwrap import dedent

class SleepyBot(SlackBot):
    """A simple Slack bot

    Arguments:
      id_ (:py:class:`str`): The BOT's Slack ID.
      user (:py:class:`str`): The BOT's friendly name.
      api (:py:class:`SlackApi`): The Slack API wrapper.

    """
    VERSION = 'SleepyBot v0.0.1'
    INSTRUCTIONS = dedent("""
    SleepyBot

    An aSlack bot demo

    For more information, see https://github.com/bensteinberg/demo-slackbot
    """)

    # necessary?
    def __init__(self, id_, user, api):
        super().__init__(id_, user, api)

    # matches
    def message_is_for_me(self, data):
        """If you send me a message"""
        return (self.message_is_to_me(data))

    # dispatchers
    async def say_im_awake(self, data):
        """I will say I'm awake"""
        return dict(channel=data['channel'], text="I'm awake!")
        
    MESSAGE_FILTERS = OrderedDict([
        (message_is_for_me, say_im_awake),
    ])

    

if __name__ == "__main__":
    """Main loop"""
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    logging.info("I'm awake and logging")
    LOOP = asyncio.get_event_loop()
    BOT = LOOP.run_until_complete(SleepyBot.from_api_token())
    LOOP.run_until_complete(BOT.join_rtm())

