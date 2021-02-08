import subprocess
from sys import executable as python
import urllib.request
import shutil
import os

# don't judge me
subprocess.run([python, "-m", "pip", "install", "-r", "requirements.txt", "--user"])
subprocess.run([python, "-m", "pip", "install", "libarchive", "--user"])

if not os.path.isfile("ffmpeg.7z"):
    urllib.request.urlretrieve("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z", "ffmpeg.7z")

try:
    shutil.rmtree("ffmpeg")
except FileNotFoundError:
    pass
try:
    shutil.rmtree("ffmpeg-4.3.2-2021-02-02-essentials_build")
except FileNotFoundError:
    pass

import libarchive.public
for entry in libarchive.public.file_pour("ffmpeg.7z"):
    print(entry)

shutil.move("ffmpeg-4.3.2-2021-02-02-essentials_build", "ffmpeg")
