import ffmpeg
import twittermedia
import vision_api
import urllib2
import os

class TwitpicAPI:
	def Aggregate(self, feed, count, download_location, video_location):
		#url_list = self.TwitterGetList(feed, count)
		#self.TwitterDownload(url_list, download_location)
		#self.TwitterImage2Video(download_location, video_location)
		self.TwitterAnalyzeImage(download_location)

	def TwitterGetList(self, feed, count):
		try:
			tw = twittermedia.TwitterMedia()
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
		gg = vision_api.GoogleVisionWrapper()
		#try:
		for img_name in os.listdir(image_folder):
			print gg.AnalyzeImage(os.path.join(image_folder, img_name))
		#except:
		#	raise ValueError("Error accessing image directory")

t = TwitpicAPI()
t.Aggregate("isigov95", -1, "/Users/illyasigov/Documents/GitHub/ec500c1/images/", "/Users/illyasigov/Documents/GitHub/ec500c1/mov.mp4")