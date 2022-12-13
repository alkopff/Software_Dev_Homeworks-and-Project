import sys
import time

#function that returns a tuple with the number of time a read aligns to a reference sequence and a list of the indexes where it aligns
def count_n_align(read, reference):
    n=0
    l=[]
    i=0
    
    while True:
      a=reference.find(read,i)
      if a==-1:
        break
      else:
        n+=1
        l+=[a]
        i=a+1
    if n==0:
        l=[-1]
    return n,l


if __name__=="__main__":
    
    if len(sys.argv)<=3:
        print("Usage:")
        print(" $python3 processdata.py <ref_file> <reads_file> <alignment_file>")
        sys.exit(0)

    ref_file=sys.argv[1]
    reads_file=sys.argv[2]
    alignment_file=sys.argv[3]

    #open and read the reference_file
    refFile=open(ref_file,'r')
    reference=refFile.read()

    print('reference length: '+ str(len(reference)))

    #creating a list containing all the reads of the reads_file
    readFile=open(reads_file,'r')
    reads=[x.replace('\n','') for x in readFile.readlines()]
    nreads=len(reads)

    print('number reads: '+ str(len(reads)))

    n0=0
    n1=0
    n2=0

    #counting the number of reads that align once, twice or never
    for read in reads:
        n_align=count_n_align(read,reference)[0]
        if n_align==0:
            n0+=1
        elif n_align==1:
            n1+=1
        elif n_align==2:
            n2+=1

    print('align0: '+ str(n0/nreads))
    print('align1: '+ str(n1/nreads))
    print('align2: '+ str(n2/nreads))

    #lauching time counting

    t0=time.time()
    #writing in the alignment_file 
    with open(alignment_file,'w') as alignFile:
        for i in range(nreads):
            alignFile.write(reads[i])
            for j in count_n_align(reads[i],reference)[1]:
                alignFile.write(" " + str(j))
            alignFile.write("\n")

    t1=time.time()

    print('elapsed time: '+ str(t1-t0))



    

 
 
 


