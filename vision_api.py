import io
import os
from google.cloud import vision
from google.cloud.vision import types

class GoogleVisionWrapper:

	client = None

	def __init__(self):
		self.client = vision.ImageAnnotatorClient()

	def AnalyzeImage(self, file_path):
		with io.open(file_path, 'rb') as image_file:
			content = image_file.read()

		image = types.Image(content=content)

		response = self.client.label_detection(image=image)
		labels = response.label_annotations

		out = []
		for label in labels:
			out.append(label.description)

		return out