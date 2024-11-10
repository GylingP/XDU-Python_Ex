import argparse
import chardet
import codecs

parser=argparse.ArgumentParser(description="Conver file to UTF-8")
parser.add_argument("filename")
parser.add_argument("-e","--encoding")

args=parser.parse_args()

filename=args.filename
encoding=args.encoding

if not encoding:
    with open(filename,'rb') as f:
        encoding=chardet.detect(f.read())['encoding']
        print(encoding)

with codecs.open(filename,'r',encoding) as f:
    data=f.read()
    with codecs.open(filename+".utf8",'w',"utf-8") as futf8:
        futf8.write(data)