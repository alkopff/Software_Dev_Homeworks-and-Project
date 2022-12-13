import glob
import math
import os


class Airfoil:

    #4 methods plus __init_:
    # load_and_read_data(self,inputdir) that creates a matrix of coordinates
    # and a dictionnary for the pressure coefficients
    #compute_foil_length(self) using an approximation
    #compute_cl that creates a dictionnary with the values of cl for each attack angle
    #__repr__ that prints the table when main prints an instance of the airfoil class

    def __init__(self, inputdir):
        self.load_and_read_data(inputdir)
        self.compute_foil_length()
        self.compute_cl()
        self.find_stagnation_points()

    #loads the data and creates a matrix of coordinates
    #and a dictionnary for the pressure coefficients
    def load_and_read_data(self,inputdir):

        paths=glob.glob(inputdir+'*')
        #there must be at least 2 files in the directory
        if len(paths)<2:
            raise RuntimeError(inputdir +" is not a valid directory ")
        files=[os.path.split(x)[1] for x in paths]
        if "xy.dat" not in files:
            raise RuntimeError(inputdir +' does not have a xy.dat file')

        #creating a list with the alpha files only
        alpha_paths=glob.glob(inputdir+'alpha*')
        self.alpha_files=[os.path.split(x)[1] for x in alpha_paths]
        if len(self.alpha_files)==0:
                    raise RuntimeError(inputdir +'does not have data for pressure coefficients')

        #filling the matrix of coordinates
        try:
            with open(inputdir+'xy.dat','r') as f:
                coordinates_lines=f.readlines()
                self.coordinates=[[],[]] 
                ind=0
                for line in coordinates_lines:
                    ind+=1
                    #we don't want to read the first line which is the name of the folder
                    if ind==1:
                        continue
                    else:
                        for i in range(2):
                            self.coordinates[i]+=[float(line.split()[i])]
        except Exception as e:
            raise RuntimeError('wrong format detected in xy.dat')

        #filling the pressure dictionnary
        #Keys=alphas, Values=Cp values
        try:
            self.pressure_dic=dict()
            for pressure_coef_file in self.alpha_files:
                with open(inputdir+pressure_coef_file, 'r') as p:
                    pressure_coeff_lines=p.readlines()
                    alpha_degrees=float(pressure_coef_file.replace('alpha','').replace('.dat',''))
                    ind=0
                    for line in pressure_coeff_lines:
                        ind+=1
                        #We don't want to read the first line which is # Cp
                        if ind==1:
                            continue
                        else:
                            if str(alpha_degrees) not in self.pressure_dic:
                                self.pressure_dic[str(alpha_degrees)]=[float(line.split()[0])]
                            else:
                                self.pressure_dic[str(alpha_degrees)]+=[float(line.split()[0])]
            
        except Exception as e:
            raise RuntimeError(' wrong format detected in the alpha files')
    
    def compute_foil_length(self):
        x_max = max(self.coordinates[0])
        x_min = min(self.coordinates[0])
        self.foil_length = x_max-x_min 
        #foil_length is not totally accurate since we should consider 
        # the corresponding delta(y) and compute the distance between 
        #the points but TAs suggested this approximation was ok

    #creates a dictionnary
    #Keys=alphas, Values=cl
    def compute_cl(self):
        self.cl_dict=dict()
        list_delta_x = [self.coordinates[0][i+1]-self.coordinates[0][i] for i in range(len(self.coordinates[0])-1)]
        list_delta_y = [self.coordinates[1][i+1]-self.coordinates[1][i] for i in range(len(self.coordinates[1])-1)]

        for alpha in self.pressure_dic.keys():
            c_x=-sum([(x*y)/self.foil_length for (x,y) in zip(self.pressure_dic[alpha],list_delta_y)])
            c_y=sum([(x*y)/self.foil_length for (x,y) in zip(self.pressure_dic[alpha],list_delta_x)])
            self.cl_dict[alpha]=(math.cos(float(alpha)*(math.pi)/180)*c_y - math.sin(float(alpha)*(math.pi)/180)*c_x)/self.foil_length

    #creates a dictionnay
    #Keys=alphas, values=list [x,y,Cp] corresponding to the stagnation point
    def find_stagnation_points(self):
        self.stagnation_points=dict()
        for alpha in self.pressure_dic.keys():
            #find the index of the Cp which is closest to 1 and take the corresponding coordinates
            cp_list_modified=[(1-x) for x in self.pressure_dic[alpha]]
            ind=cp_list_modified.index(min(cp_list_modified))
            self.stagnation_points[alpha]=[(self.coordinates[0][ind]+self.coordinates[0][ind+1])/2, (self.coordinates[1][ind]+self.coordinates[1][ind+1])/2, self.pressure_dic[alpha][ind]]
        return self.stagnation_points

    #prints the output table that we want   
    def __repr__(self):
        self.table=''
        table_features='    alpha     cl             stagnation pt \n'
        separator='   -------  -------    --------------------------- \n'
        self.table+=table_features+separator
        alphas=[str(x) for x in self.pressure_dic.keys()]
        dict = self.stagnation_points
        for alpha in sorted(alphas):
            #find the coordinates of the stagnation point and the value of Cp in the stgn points dictionnary
            stag_point=[dict[str(alpha)][i] for i in range(3)]
            cl = self.cl_dict[alpha]
        

        #string formatting examples found on https://shocksolution.com/2011/11/03/python-string-format-examples/
            self.table+= "{:8.2f}  {:8.4f}    ({:8.4f}, {:8.4f}) {:8.4f} \n".format(float(alpha), cl, stag_point[0], stag_point[1], stag_point[2])
        return self.table

