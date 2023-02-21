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
    if 'RxNorm' in i:
        a = 'C:/Users/salta/Documents/Ryte/'+i
        path_names.append(a)
        

prescribe = []
ggg = []
for i in path_names:
    s = os.listdir(i)
    for g in s:
        k = i+'/'+g
        if '.zip' not in k:
            
            
        
        
            #print(k)
            rrf = os.listdir(k)
            lk = i+'/'+g + '/'+ rrf[1]+'/'
            #k = i+'/'+g + '/'+'prescribe' +'/'
            #print(rrf)
            #print(lk)
            prescribe.append(lk)
import os

ggg = []
for h in prescribe:
    if 'prescribe' in h:
        #print(h)
        prescribe_files = os.listdir(h)
        #print(prescribe_files[1])
        end_path = h+prescribe_files[1]+'/'
        ggg.append(end_path)
        #print(end_path)
        
        
for h in prescribe:
    if 'prescribe' in h:
        #print(h)
        prescribe_files = os.listdir(h)
        #print(prescribe_files[1])
        end_path = h+prescribe_files[1]+'/'
        #print(end_path)
        for j in os.listdir(end_path):
            if '.RRF' in j:
                if 'prescribe.RRF' not in j:
                #print(j.split('.'))
                    d = j.split('.')
                    old_name = end_path + j
                    print(old_name)
                    new_name = end_path+d[0] +'_prescribe.RRF'
                    os.rename(old_name, new_name)
                    print(new_name)
            
        
    
        
    
