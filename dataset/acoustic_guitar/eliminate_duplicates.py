from hashlib import md5
from os import listdir
from os.path import isfile, join

path = '.'
files = [f for f in listdir(path) if isfile(join(path, f))]

file_and_md5 = {}

# Calculate MD5
def Getmd5(file):
  # get hash of file
  file_bytes = file.encode('utf-8')
  file_hash = md5(file_bytes).hexdigest()
  return file_hash

# Put on a list all files and their respectives md5 sum
for file in files:
	if(file.endswith('.jpeg') or file.endswith('.JPEG') or file.endswith('.xml') or file.endswith('.XML')):
	  file_and_md5[file] = Getmd5(file)

dict_counter = {}
for file, value in file_and_md5.items():
  if(value in dict_counter):
    print(dict_counter[value])
  else: dict_counter[value].value()+=1

for file, value in dict_counter.items():
  if(value!=1):
    print(dict_counter[file])

#test = 'n02676566_8533.xml'
#print (test in file_and_md5)


#if file_path in files:
  