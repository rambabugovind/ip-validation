import sys
#import argparse
import re
import os.path


#parser = argparse.ArgumentParser(description='Argument Parser')



def add(k,v):

	if (re.compile(r'^(\+\d{1,2} ?|\(\d{1,3}\)|1-)?\d{3}-\d{3}-\d{4}$').match(v)):
		sys.stderr.write("Phone number accepted.")
		pbool = True
	elif(re.compile(r'^(\+\d{1,2} ?|\d ?)?\(\d{2,3}\)(\d{3}-\d{4})$').match(v)):
		sys.stderr.write("Phone number accepted.")
		pbool = True
	elif(re.compile(r'^(\d{5,8}|\d{3}-\d{4})$').match(v)):
		sys.stderr.write("Phone number accepted.")
		pbool = True
	elif(re.compile(r'^\d{3} ?\d? \d{3} \d{3} \d{4}$').match(v)):
		sys.stderr.write("Phone number accepted.")
		pbool = True
	elif(re.compile(r'^\d{5}.\d{5}$').match(v)):
		sys.stderr.write("Phone number accepted.")
		pbool = True
	else:
		sys.stderr.write("Phone number NOT accepted.")
		pbool = False
	if (re.compile(r'^[a-zA-Z]{2,} ?(([a-zA-Z]\.)|(, [a-zA-Z]{2,})|([a-zA-Z]\'?[a-zA-Z]+))? ?([a-zA-Z]{2,})? ?(\-[a-zA-Z]{2,})? ?([a-zA-Z]{,2}\.)?$').match(k)):
		sys.stderr.write(" Name accepted.")
		nbool = True
	elif(re.compile(r'^[a-zA-Z]\'?[a-zA-Z]+ ?((, [a-zA-Z]{2,})|(\-[a-zA-Z]{2,},))? ?(((a-zA-Z){2,})|([a-zA-Z]{,2}\.))?$').match(k)):
		sys.stderr.write(" Name accepted.")
		nbool = True
	else:
		sys.stderr.write(" Name NOT accepted.")
		nbool = False
	if (nbool and pbool):
		sys.stderr.write(" Name and Phone num meets reqrd conditions. Stored in file.")
		if(os.path.isfile("output.txt")):
			f = open("output.txt","a")
		else:
			f = open("output.txt","w")
		f.write(""+k+"\t"+v+"\n")
		f.close()
		s = set()
		f = open("output.txt","r")
		lines = f.readlines()
		f.close()
		f = open("output.txt","w")
		for line in lines:
			if line not in s:
				f.write(line)
				s.add(line)
		f.close()
		sys.exit(0)
	else:
		sys.stderr.write(" Name/Phone num DOESNT meet reqrd conditions. NOT Stored in file.")
		sys.exit(1)

def list():
	f = open("output.txt","r")
	print(f.read())
	f.close()
	
def delt(d):
	f = open("output.txt","r")
	lines = f.readlines()
	f.close()
	f = open("output.txt","w")
	for line in lines:
		if d not in line:
			f.write(line)
	f.close()


nbool = False
pbool = False
	

if (len(sys.argv) < 2):
	print("Usage: ")
	print("1. Add: .\secprog.py add \"John Smith\" \"(123)456-7890\"\n2. Delete by name: .\secprog.py del \"John Smith\"\n3. Delete by number: .\secprog.py del \"(123)456-7890\"\n4. List: .\secprog.py list")
	print("Double quotes reqrd wherever used")

elif(sys.argv[1] == 'add' and (len(sys.argv) == 4)):
	p = sys.argv[2]
	t = sys.argv[3]
	#t = ' '.join(sys.argv[3])		
	add(p,t)

elif(sys.argv[1] == 'list'): 
	list()

elif(sys.argv[1] == 'del' and len(sys.argv) ==3): 
	d = sys.argv[2]
	delt(d)

else:
	print("Usage: ")
	print("1. Add: .\secprog.py add \"John Smith\" \"(123)456-7890\"\n2. Delete by name: .\secprog.py del \"John Smith\"\n3. Delete by number: .\secprog.py del \"(123)456-7890\"\n4. List: .\secprog.py list")
	print("Double quotes reqrd wherever used")



#dict = {k:k*k for k in range(1,10) }
#print (dict)
 
 
#input() -- to keep cmd open even after it displays o/p