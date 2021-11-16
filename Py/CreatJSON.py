import os
StartData = '/Users/paulcarter/Documents/GITHUB/Melbage/LinkChecker/Data/TFhrefData_v1.txt'
JsonFile = '/Users/paulcarter/Documents/GITHUB/Melbage/LinkChecker/Data/HtmlRecords.json'
#contents=[]
with open(StartData) as file_object:
    contents = file_object.read()
  #  print(contents)
FileList = contents.splitlines()
print(FileList)

#define the list of records which don't have any Href in them 
NoHrefList=[]
HrefList=[] 

for i in FileList:
    if i.find(":") > 0:
        HrefList.append(i)
    else:
        NoHrefList.append(i)
    
                
#print(NoHrefList)
print(HrefList)