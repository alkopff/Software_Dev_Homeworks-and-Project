import sys
import random 

#function to generate a random DNA sequence of size n 
def generate_seq(n):
	dict={'0':'A','1':'C','2':'G','3':'T'}
	seq=''
	for i in range(n):
		seq+=dict[str(random.randint(0,3))]
	return seq

#function to generate a reference sequence of size n, using the generate_seq function
def generate_ref(n):
	size1=int(0.75*(n)) #generate 75% of the reference randomly
	a=generate_seq(size1)
	size2=n-size1
	b=a[(size1-size2):] #copy the last 25% to complete the sequence
	return a+b

#function to generate N reads of size read_length so that 75% of the reads align once to the reference, 10% twice and 15% never
#returns three lists containing each kind of reads (align0 in L0, align1 in L1 and align3 in L3)
def generate_reads(N,read_length,reference):
	n=len(reference)
	L0=[]
	L1=[]
	L2=[]
	for i in range(N):
		a=random.random()
		if a<=0.75:
			#choosing a random position in the first 50% of the sequence and generating a read starting at this position
			random_position=random.randint(0,n//2-read_length)
			L1+=[reference[random_position:random_position+read_length]]

		elif a>0.75 and a<=0.9:
			read=reference[:read_length]
			#generate reads until one doesn't align to the reference sequence
			while reference.find(read)!=-1:
				read=generate_seq(read_length)
			L0+=[read]
			
		elif a>0.9:
			#choosing a random position in the last 25% of the reference sequence and generating a read starting at this position
			random_position=random.randint(3*(n//4)+1,n-read_length)
			read=reference[random_position:random_position+read_length]
			L2+=[read]
	return L0, L1, L2

if __name__ =="__main__":
	# if len(sys.argv)<7:
	# 	print("Usage:")
    # 	print(" $python3 processdata.py <ref_len> <nreads> <read_len> <ref_file> <reads_file>")
    # 	sys.exit(0)

	ref_len=int(sys.argv[1])
	nreads=int(sys.argv[2])
	read_len=int(sys.argv[3])
	ref_file=sys.argv[4]
	reads_file=sys.argv[5]

	#generate our data set with the reference and the corresponding reads
	reference=generate_ref(ref_len)
	reads=generate_reads(nreads,read_len,reference)

	refFile=open(ref_file, 'w')
	refFile.write(reference)
	refFile.close()

	readFile=open(reads_file,'w')
	for read in reads:
		for line in read:
			readFile.write(line + "\n")
		
	readFile.close()

	print('reference length:'+str(ref_len))
	print('number of reads: '+str(nreads))
	print('read length: '+str(read_len))
	print('align0:'+str((len(reads[0])/nreads)))
	print('align1:'+str((len(reads[1])/nreads)))
	print('align2:'+ str((len(reads[2])/nreads)))
		
