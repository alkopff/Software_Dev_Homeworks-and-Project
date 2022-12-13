import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
import sys
import warnings


class Truss:

    def __init__(self, files):
        '''init reads the files containing the data for the truss, 
        creates the system Ax=b where unknowns are beam forces and reaction forces
        and solves it when possible'''
        self.joints_file=files[0]
        self.beams_file=files[1]
        if len(files)>3:
            self.output_file=files[2]
        
        self.read_data()

        if len(sys.argv)==4:
            self.PlotGeometry(files[2])

        self.create_system()

        self.solve_system()
        
        

    def read_data(self):
        '''Loads the data files of the trussand convert them into np.arrays, 
        computes the number of joints, 
        the number of rigidly supported joints and the number of beams.
        Raises an error if the geometry is not suitable for the analysis'''

        self.joints = np.loadtxt(self.joints_file, dtype=np.float64)[:,1:]
        self.beams = np.loadtxt(self.beams_file, dtype=np.int8)[:,1:] 
        self.n_beams=len(self.beams)
        self.n_joints=len(self.joints)

        #counts the number of rigidly supported joints
        self.n_zerodisp=0
        for i in range(self.n_joints):  
            if self.joints[i,4]==1:
                self.n_zerodisp+=1

        #Check if the number of unknowns as the number of equations
        #raises Error otherwise
        if 2*self.n_joints!=self.n_beams+2*self.n_zerodisp:
            raise RuntimeError('Truss geometry not suitable for static equilbrium analysis')
  

    def PlotGeometry(self,output_file):
        '''If the input precises an output file, this method plots the geometry of the truss
        and saves it into this file'''

        plt.axis('equal')
        for beam in range(self.n_beams):
            joint_a=self.beams[beam,0]
            joint_b=self.beams[beam,1]
            xa,ya=self.joints[joint_a-1,0],self.joints[joint_a-1,1]
            xb,yb=self.joints[joint_b-1,0],self.joints[joint_b-1,1]
            plt.plot([xa,xb],[ya,yb],'b')
            
        plt.savefig(output_file)

    def create_system(self):
        '''Creates the system Ax=b where the x contains the beam forces
        and the projections of reaction forces on the rigidly supported joints.
        b contains the projections of the external forces for each joint
        A is a sparse matrix'''
        row=[]
        col=[]
        values=[]
        self.b=np.zeros(2*self.n_joints)

        for beam in range(self.n_beams):
            joint_a=self.beams[beam,0]
            joint_b=self.beams[beam,1]
            xa,ya=self.joints[joint_a-1,0],self.joints[joint_a-1,1]
            xb,yb=self.joints[joint_b-1,0],self.joints[joint_b-1,1]
            dist_ab=math.sqrt((xb-xa)**2+(yb-ya)**2)
            cosine=(xb-xa)/dist_ab
            sine=(yb-ya)/dist_ab
            
            row+=[2*joint_a-2,2*joint_a-1,2*joint_b-2,2*joint_b-1]
            col+=[beam for i in range(4)]
            values+=[cosine,sine,-1*cosine,-1*sine]

        #filling the matrix with the reaction forces Rx and Ry 
        #for each rigidly supported joint                   
        for i in range(self.n_joints):
            if self.joints[i,4]==1: #only filling the rows of joints that are rigidly supported
                row+=[2*i,2*i+1]

        col+=[self.n_beams+j for j in range(2*self.n_zerodisp)]
        values+=[1 for k in range(2*self.n_zerodisp)]
                

        self.A_matrix=csr_matrix((values, (row, col)), shape=(2*self.n_joints, self.n_beams+2*self.n_zerodisp))
        
        #creating vector b of size 2*n_joints with the Fx et Fy components forces for each joint
        for i in range(self.n_joints):
            self.b[2*i]=self.joints[i,2]
            self.b[2*i+1]=self.joints[i,3]


    def solve_system(self):
        ''' solves the system if it is not singular'''

        #Catch warnings as exceptions
        warnings.filterwarnings('error')
        #Solve if the matrix is not singular
        try:
            self.x = spsolve(self.A_matrix, self.b)
        except Exception as e:
            raise RuntimeError("Cannot solve the linear system, unstable truss?")
        self.beam_forces=self.x[:-2*self.n_zerodisp] #only keeping the beam forces and not the reaction forces


    def __repr__(self):  
        '''prints a table with two columns, one for the beams and one for the associated beam forces'''  

        string  = "Beam    Force\n"
        string += "----   -------\n"
        for i in range(len(self.beam_forces)):
            string += "  " + str(i+1) + "  {: 8.3f}\n".format(self.beam_forces[i])
        return string
