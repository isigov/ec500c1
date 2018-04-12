import ffmpeg
import twittermedia
import vision_api
import urllib2
import os
import pymongo

class TwitpicAPI:
	def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret, json_key):
		self.lconsumer_key=consumer_key
		self.lconsumer_secret=consumer_secret
		self.laccess_token_key=access_token_key
		self.laccess_token_secret=access_token_secret
		self.ljson_key=json_key
		self.client = pymongo.MongoClient()

	def Aggregate(self, feed, count, download_location, video_location, ffmpeg_location):
		url_list = self.TwitterGetList(feed, count)
		self.TwitterDownload(url_list, download_location)
		#self.TwitterImage2Video(download_location, video_location, ffmpeg_location)
		return self.TwitterAnalyzeImage(download_location, feed)

	def SaveMongo(self, data, database, collection):
		mongo_db = self.client[database]
		mongo_co = mongo_db[collection]
		result = mongo_co.insert_one(data)

	def outputMongo(self):
		for post in self.client['tweets']['savedTerms'].find().sort('count', -1):
			print str(post['name']) + " " + str(post['count'])

	def TwitterGetList(self, feed, count):
		try:
			tw = twittermedia.TwitterMedia(self.lconsumer_key, self.lconsumer_secret, self.laccess_token_key, self.laccess_token_secret)
			urls = tw.FetchImages(feed, count)
			print "Fetched {0} images from {1}...".format(feed, count)
			return urls
		except:
			raise ValueError("Error connecting to Twitter")
			return

	def TwitterDownload(self, urls, location):
		counter = 0
		for url in urls:
			datatowrite = ""
			try:
				filedata = urllib2.urlopen(url)  
				datatowrite = filedata.read()
			except:
				raise ValueError("Error downloading image from {0}", url)
				continue

			try:
				with open(os.path.join(location, 'image-%04d.jpg' % counter), 'wb') as f:  
					f.write(datatowrite)
			except:
				raise ValueError("Error saving images")
				return
			print "Downloaded from {0} & saved to {1}".format(url, os.path.join(location, 'image-%04d.jpg' % counter))
			counter += 1

	def TwitterImage2Video(self, image_folder, save_file, ffmpeg_location, fps=1):
		ff = ffmpeg.ffmpeg()
		ff.img2vid(image_folder, save_file, fps, ffmpeg_location)
		try:
			if os.path.getsize(save_file) == 0:
				raise ValueError("Error converting images to video")
			print "Converted images from {0} to video file {1}".format(image_folder, save_file)
		except:
			raise ValueError("Error converting images to video")

	def TwitterAnalyzeImage(self, image_folder, feed):
		gg = vision_api.GoogleVisionWrapper(self.ljson_key)
		labels = []
		try:
			for img_name in os.listdir(image_folder):
				if img_name.endswith(".jpg"):
					print "Analyzing {0}...".format(img_name)
					out_labels = gg.AnalyzeImage(os.path.join(image_folder, img_name))
					for s in out_labels:

						post = self.client['tweets']['savedTerms'].find_one({'name': s})
						if post is not None:
							print "{0} exists, adding to count".format(s)
							self.client['tweets']['savedTerms'].update_one({'name': s}, {"$set": {'name': s, 'count': int(post['count']) + 1}})
						proto = {
							'name': s,
							'count' : 1
						}
						print "{0} doesn't exist, creating new".format(s)
						self.SaveMongo(proto, 'tweets', 'savedTerms')
					labels.append(out_labels)
					post_1 = {
						'handle': feed,
						'img_name': img_name,
						'labels': ','.join(out_labels)
					}
					print "Saved image {0} to MongoDB".format(img_name)
					self.SaveMongo(post_1, "tweets", "images")
			return labels
		except:
			raise ValueError("Error accessing image directory")