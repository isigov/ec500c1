import ffmpeg
import twittermedia
import urllib2
import os

def main():
	try:
		tw = twittermedia.TwitterMedia()
		urls = tw.FetchImages("isigov95")
	except:
		print("Error connecting to Twitter\n")
		return

	counter = 0
	for url in urls:
		datatowrite = ""
		try:
			filedata = urllib2.urlopen(url)  
			datatowrite = filedata.read()
		except:
			print("Error downloading image from {0}\n", url)
			continue

		with open('images/image-%04d.jpg' % counter, 'wb') as f:  
			f.write(datatowrite)

		counter += 1
	ff = ffmpeg.ffmpeg()
	ff.img2vid(os.getcwd() + "/images", "mov.mp4")


if __name__ == '__main__':
	main()
