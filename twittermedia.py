#!/usr/bin/env python

import twitter
import wget

class TwitterMedia:
	def __init__(self):
		self.api = twitter.Api(consumer_key='mCKUIlopQMyMuuXhiHVF6aIHH',
		consumer_secret='vIeyrkwqCEOmqo8MZ0vP9DrmCYqg4lrJUkdPdwSnGKJHYhhyL5',
		access_token_key='2492938182-FC5nBZKdfor74sqdzA4qvqCgH9BQusYO7wy14pX',
		access_token_secret='ync9VcW2xj23HStbntPI3A3S9MXG9SbtkblVTDcUo6arb')

	def FetchImages(self, feed):
		statuses = self.api.GetUserTimeline(screen_name=feed, count=200)
		last_id = statuses[-1].id-1

		while True:
			more_statuses = self.api.GetUserTimeline(screen_name="isigov95", count=200, max_id=last_id)
			if len(more_statuses) < 200:
				statuses = statuses + more_statuses
				break
			elif len(more_statuses) == 200:
				statuses = statuses + more_statuses
				last_id = more_statuses[-1].id-1

		images = []
		for s in statuses:
			if not s.media == None:
				if s.media[0].type == "photo":
					images.append(s.media[0].media_url)

		return images