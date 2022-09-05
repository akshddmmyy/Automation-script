
# coding: utf-8

# In[4]:


import os,shutil,re,magic
if os.getcwd() != "C:\\Users\\admin\\Desktop" :
     os.chdir("C:\\Users\\admin\\Desktop")
        
names=input(prompt='enter dir nme to save contnts to')

if os.path.isfile(names):
    
    names=input(prompt='file with same name exists and enter dir nme to save contnts to')
    os.mkdir(names)
    
elif not os.path.exists(names):
    
    os.mkdir(names)
    
else:
    print("dir with name exist and file will save ti it")


for item in os.listdir():
    #(a,b)=os.path.splitext(item)
    
    if os.path.isfile(item):
        
        x=magic.from_file(item)
        
        if bool(re.findall('\\bpdf\\b',x,re.IGNORECASE)):
            k=os.path.join(names,'pdf')
            if os.path.exists(k):   
                shutil.move(item,k)
            else:
                os.mkdir(k)
                shutil.move(item,k)
                
        
        elif bool(re.findall('\\bhtml\\b',x,re.IGNORECASE)):
            k=os.path.join(names,'html')
            if os.path.exists(k): 
                shutil.move(item,k)
            else:
                os.mkdir(k)
                shutil.move(item,k)
        
        elif bool(re.findall('\\bexecutable\\b',x,re.IGNORECASE)):
            k=os.path.join(names,'exe')
            if os.path.exists(k):
                shutil.move(item,k)
            else:
                os.mkdir(k)
                shutil.move(item,k)
        
        elif bool(re.findall('\\bexcel\\b',x,re.IGNORECASE)):
            k=os.path.join(names,'xls')
            if os.path.exists(k):
                shutil.move(item,k)
            else:
                os.mkdir(k)
                shutil.move(item,k)
    
        elif bool(re.findall('\\bmedia\\b',x,re.IGNORECASE)) or bool(re.findall('\\bimage\\b',x,re.IGNORECASE)):
        
            k=os.path.join(names,'media')
            if os.path.exists(k):
                shutil.move(item,k)
            else:
                os.mkdir(k)
                shutil.move(item,k)
        
        elif bool(re.findall('\\btext\\b',x,re.IGNORECASE)):
            k=os.path.join(names,'txt')
            if os.path.exists(k):
                shutil.move(item,k)
            else:
                os.mkdir(k)
                shutil.move(item,k)
                
        elif bool(re.findall('\\bshortcut\\b',x,re.IGNORECASE)):
            k=os.path.join(names,'windows_shortcuts')
            if os.path.exists(k):
                shutil.move(item,k)
            else:
                os.mkdir(k)
                shutil.move(item,k)
              
        elif bool(re.findall('\\barchive\\b',x,re.IGNORECASE)):
            k=os.path.join(names,'archive')
            if os.path.exists(k):
                shutil.move(item,k)
            else:
                os.mkdir(k)
                shutil.move(item,k)
                
        elif bool(re.findall('\\bmicrosoft word\\b',x,re.IGNORECASE)):
            k=os.path.join(names,'word_files')
            if os.path.exists(k):
                shutil.move(item,k)
            else:
                os.mkdir(k)
                shutil.move(item,k)

