# Imports
import moviepy.editor
from pathlib import Path

# Variables
video_file = Path('video.mp4')

video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio

# Code
audio.write_audiofile(f'{video_file.stem}.mp3')
