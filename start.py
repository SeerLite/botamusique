import sys
import subprocess

if sys.platform == "win32":
    import os
    os.environ["PATH"] += ";ffmpeg\\bin\\"

subprocess.run([sys.executable, "mumbleBot.py"])
