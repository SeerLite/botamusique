import subprocess
from sys import executable as python

# don't judge me
subprocess.run([python, "-m", "pip", "install", "-r", "requirements.txt", "--user"])
