#!/usr/bin/env python

import twitter
import wget

class TwitterMedia:
	def __init__(self):
		self.api = twitter.Api()

	def FetchImages(self, feed, amt=-1):
		statuses = self.api.GetUserTimeline(screen_name=feed, count=200)
		last_id = statuses[-1].id-1

		while True:
			more_statuses = self.api.GetUserTimeline(screen_name=feed, count=200, max_id=last_id)
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
					if amt > 0:
						amt -= 1
						if amt == 0:
							break
		return images