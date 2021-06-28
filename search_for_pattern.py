#shutil module 
import shutil

shutil.unpack_archive('unzip_me_for_instructions.zip','','zip') #(name of zip file, where to extract it - '' is a default folder,file type)
#os,re modules 
import os,re
#Function to search a pattern - return pattern or None
def search_for_pattern(pattern,files,folder): 
    for f in files:
        with open(folder+'\\'+f) as open_file: # folder+'\\'+f - full path 
            temp = re.findall(pattern,open_file.read())
            if temp != []:
                return temp
#Main 
pattern = r'\d{3}-\d{3}-\d{4}'
path = os.getcwd()+'\\extracted_content'
phones = []

for folder,sub_folders,files in os.walk(path):
    temp = search_for_pattern(pattern,files,folder)
    if temp != None:
        phones.extend(temp)
print(phones)