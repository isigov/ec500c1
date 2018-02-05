import os
import sys
import tempfile
import argparse
import subprocess

class ffmpeg:
	def img2vid(self, directory, output, fps, ffmpeg_location):
		ffmpeg_options = {
		'-framerate': fps,
		'-i': os.path.join(directory, 'image-%04d.jpg'),
		'-vf': 'scale=720:480'
		}

		command = [ffmpeg_location]
		for key, value in ffmpeg_options.iteritems():
			command.extend((key, str(value)))
		command.append('-y')  # overwrite outputs
		command.append(output)

		print ' '.join(command)
		subprocess.call(command)
