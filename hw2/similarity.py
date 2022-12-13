import math
import numpy as np
import random 
import sys
import time

if __name__=="__main__":

    if len(sys.argv)<=3:
        print("Usage:")
        print(" $python3 similarity.py <data_file> <output file> [user_thresh (default = 5)]")
        sys.exit(0)
        

    data_file=sys.argv[1]
    output_file=sys.argv[2]
    min_com_users=int(sys.argv[3])

    print("Input MovieLens file: " + data_file)
    print("Output file for similarity data: " + output_file)
    print("Minimum number of common users: " + str(min_com_users))



    f=open(data_file,'r')
        
    #create a dictionnary L with all the data. Each key of L is a movie_id. 
    # The value associated is a dictionnary where each key is a user 
    # and each value is the rating he gave to the movie
    L={}
    users=set()
    n_lines=0
    n_movies=0
    n_users=0

    for line in f:

        if line=="":
            continue
        n_lines+=1

        user=line.split()[0]
        movie=line.split()[1]
        r=line.split()[2]
        rating=r.replace('\n',"")

        if user not in users:
            users.add(user)
            n_users+=1

        if movie in L:
            L[movie][user]=int(rating)
        else:
            L[movie]={user:int(rating)}
            n_movies+=1  

    

    print('Read '+str(n_lines)+' lines with total of '
    +str(n_movies)+' movies and '+str(n_users)+' users')


    #create a dictionnary dic_means where each key is a movie id 
    # and each value is the mean of all the ratings for this movie
    dic_means={}
    for movie in L:
        list_ratings=[L[movie][users] for users in L[movie]]
        dic_means[movie]=np.mean(list_ratings)
    # print(dic_means)

    #function that returns a set containing 
    # all the common_user that rated movie1 and movie2
    def common_users(movie1,movie2,L):
        a=set(L[movie1].keys())
        b=set(L[movie2].keys())
        return a.intersection(b)
    # print(common_users('2','3',L))

    #crete a dictionnary where each key is a tuple (movie1,movie2) 
    # and each value is the set of common_users between movie1 and movie2    
    common_data={}
    for movie1 in L:
        for movie2 in L:
            if movie1!=movie2:
                common_data[(movie1, movie2)]=common_users(movie1,movie2,L)


    #function that compute the similarity between a and b 
    # using the dictionnary L and the dictionnary of common data
    def similarity(a,b,L):
        ra=dic_means[a]
        rb=dic_means[b]
        n=len(common_data[(a,b)])
        L1=[]
        L2=[]
        result=0
        
        if n>=min_com_users:
            
            for common_user in common_data[(a,b)]:
                L1+=[L[a][common_user]-ra]
                L2+=[L[b][common_user]-rb]
            num=sum([x*y for x,y in zip(L1,L2)])
            l1=[x**2 for x in L1]
            l2=[y**2 for y in L2]
            denom = math.sqrt((sum(l1)*sum(l2)))

            #setting the similarity to -2 if the denominator equals 0 
            if denom==0:
                result=-2
            else: 
                result=num/denom
        return result,n
    
    t0=time.time()
    #complete the output file by iterating on the movies
    with open(output_file,'w') as f:
        movies=[int(movie) for movie in L.keys()]
        ordered=sorted(movies)
        ordered_movies=[str(movie) for movie in ordered]
        for movie1 in ordered_movies:
            current_max=-3
            corresponding_movie=0
            for movie2 in ordered_movies:
                if movie1!=movie2:
                    a=similarity(movie1,movie2,L)[0]
                    if a>current_max:
                        current_max=a
                        corresponding_movie=str(movie2)
            #completing the line corresponding to movie1
            n=similarity(movie1,corresponding_movie,L)[1]
            if current_max<-1:
                f.write(movie1+ " \n")
            else:
                f.write(movie1 + " ("
                +str(corresponding_movie)+", "+str(current_max)+", "+str(n)+")"+"\n")
            #then we go back in to the first for loop 
            # and do it again for the next movie
    t1=time.time()
    print("Similarities computed in "+str(t1-t0)+"seconds")