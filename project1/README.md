# TwitpicAPI
<br/>
Library to fetch images URLs from Twitter feed, downloaded images, compile into video using ffmpeg, and return labels from Google Vision
<br/>
<br/>
Import twitpicapi.py into project
<br/>
Initalize the TwitpicAPI class with Twitter & Google API keys
<br/>
Call Aggregate function with arguments: feed=name of twitter account to fetch images from
<br/>
count=number of images to fetch, set to -1 for infinity
<br/>
download_location=full path to folder where to save images
<br/>
video_location=full path to video file
<br/>
<br/>
Returns list of lists containing name of image as first element and phrases contained in image for the rest of elements


