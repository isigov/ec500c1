# TwitpicAPI

Library to fetch images URLs from Twitter feed, downloaded images, compile into video using ffmpeg, and return labels from Google Vision.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* [Python](http://www.python.org) - Main language
* [ffmpeg](https://www.ffmpeg.org/) - Image/video conversion
* [Google Vision API](https://cloud.google.com/vision/) - Used to create labels from images

## Using the library

Initalize the TwitpicAPI class with Twitter & Google API keys

```python
import twitpicapi

consumer_key=''
consumer_secret=''
access_token_key=''
access_token_secret=''
json_key = '/path/to/google.json'

t = twitpicapi.TwitpicAPI(consumer_key, consumer_secret, access_token_key, access_token_secret, json_key)
t.Aggregate("handle", -1, "/path/to/Images/", "/path/to/mov.mp4", "ffmpeg")
```

Call Aggregate function with arguments: 
feed=name of twitter account to fetch images from
count=number of images to fetch, set to -1 for infinity
download_location=full path to folder where to save images
video_location=full path to video file

Returns list of lists containing name of image as first element and phrases contained in image for the rest of elements
