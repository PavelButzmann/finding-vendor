# Program to find vendor, it run in Python3

This is a small program to find the vendor from a list of MAC addresses. This is useful if you have a large list and want to know who the vendor of those devices is.

⚠ Consider creating a file named <ins>macaddress.txt</ins> with your MAC address list, and change <ins>FILE_PATH</ins> variable in the line to the directory where your list will be.

### file = open('FILE_PATH','r').read().splitlines()

for example if your file <ins>macaddress.txt</ins> is on <ins>/temp/programs/</ins> you need to remplace the line for

### file = open('/temp/programs/macaddress.txt','r').read().splitlines()

now please install requirements, if you want to run on virtual environment do the follow

python3 -m venv finding

source finding/bin/activate

### pip install -r /path/to/requirements.txt
