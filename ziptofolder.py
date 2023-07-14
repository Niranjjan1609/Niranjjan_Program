import os
import zipfile

path = os.getcwd()

def extract_zip():
	print(path)
	for file in os.listdir(path):
		if file.endswith('.zip'):
			zipfile = path +'\\'+file
			with zipfile.ZipFile(zipfile, 'r') as zip_ref:
				zip_ref.extractall(path)


extract_zip()