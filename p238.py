import hashlib
file_name="img.jpg"
with open(file_name,"rb" )as f:
	file_data=f.read()
	imagehash=hashlib.sha256(file_data).hexdigest()
	print("hash code image: ",imagehash)