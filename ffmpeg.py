import os
import sys
import tempfile
import argparse
import subprocess

class ffmpeg:
	def img2vid(self, directory, output):
		ffmpeg_options = {
		'-framerate': '1',
		'-i': os.path.join(directory, 'image-%04d.jpg'),
		'-vf': 'scale=720:480'
		}

		command = ['ffmpeg']
		for key, value in ffmpeg_options.iteritems():
			command.extend((key, str(value)))
		command.append('-y')  # overwrite outputs
		command.append(output)

		print ' '.join(command)
		subprocess.call(command)
