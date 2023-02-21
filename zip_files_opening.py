import zipfile
with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
    zip_ref.extractall(directory_to_extract_to)
    
    
    
import os
  
# Get the list of all files and directories
# in the root directory
path = "C:/Users/salta/Documents/Ryte/"

dir_list = os.listdir(path)
  
print("Files and directories in '", path, "' :") 
  
# print the list
print(dir_list)


path_names = []
for i in dir_list:
    #print(i)
    if 'RxNorm_2' in i:
        a = 'C:/Users/salta/Documents/Ryte/'+i
        path_names.append(a)
        
        
big_list = []
for i in path_names:
    dir_list = os.listdir(i)
    for j in dir_list:
        path_full = i+'/'+j
        print(i+'/'+j)
        
        
        
        big_list.append(path_full)
        
        
zip_files = []
for i in big_list:
    if '.zip' in i:
        zip_files.append(i)
        print(i)
        
zip_files = []
for i in big_list:
    if '.zip' in i:
        zip_files.append(i)
        print(i)
        
        
directory_to_extract_to = []
for i in zip_files:
    po = i.split('.')[0]+'/'
    #print(po)
    directory_to_extract_to.append(po)
    
    
import zipfile
for i in range(len(zip_files)):
    
    with zipfile.ZipFile(zip_files[i], 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to[i])
    
