import ffmpeg
import twittermedia
import vision_api
import urllib2
import os

class TwitpicAPI:
	def __init__(self, consumer_key, consumer_secret, access_token_key, access_token_secret, json_key):
		self.lconsumer_key=consumer_key
		self.lconsumer_secret=consumer_secret
		self.laccess_token_key=access_token_key
		self.laccess_token_secret=access_token_secret
		self.ljson_key=json_key

	def Aggregate(self, feed, count, download_location, video_location):
		url_list = self.TwitterGetList(feed, count)
		self.TwitterDownload(url_list, download_location)
		self.TwitterImage2Video(download_location, video_location)
		return self.TwitterAnalyzeImage(download_location)

	def TwitterGetList(self, feed, count):
		try:
			tw = twittermedia.TwitterMedia(self.lconsumer_key, self.lconsumer_secret, self.laccess_token_key, self.laccess_token_secret)
			urls = tw.FetchImages(feed)
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
				with open(location + '/image-%04d.jpg' % counter, 'wb') as f:  
					f.write(datatowrite)
			except:
				raise ValueError("Error saving images")
				return

			counter += 1

	def TwitterImage2Video(self, image_folder, save_file, fps=1):
		ff = ffmpeg.ffmpeg()
		ff.img2vid(image_folder, save_file, fps)
		try:
			if os.path.getsize(save_file) == 0:
				raise ValueError("Error converting images to video")
		except:
			raise ValueError("Error converting images to video")

	def TwitterAnalyzeImage(self, image_folder):
		gg = vision_api.GoogleVisionWrapper(self.ljson_key)
		labels = []
		try:
			for img_name in os.listdir(image_folder):
				if img_name.endswith(".jpg"):
					labels.append([img_name, gg.AnalyzeImage(os.path.join(image_folder, img_name))])
			return labels
		except:
			raise ValueError("Error accessing image directory")