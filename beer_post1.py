# -*- coding: utf-8 -*-

from slacker import Slacker
import slackbot_settings

if __name__ == '__main__':
	slack = Slacker(slackbot_settings.API_TOKEN)
	slack.chat.post_message(
	'general',
	'今まで嘘ついてごめんなさい。',
	username='ふみ',
	icon_emoji='simple_smile:',
	)
