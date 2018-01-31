import io
import os
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account

class GoogleVisionWrapper:

	client = None

	def __init__(self, json_key):
		credentials = service_account.Credentials.from_service_account_file(json_key)
		self.client = vision.ImageAnnotatorClient(credentials=credentials)

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