#! usr/bin/python3

#with open('/etc/hostapd/hostapd.conf', "r") as f:
 # f_contents = f.readlines()
  #resultsDict = {}
  #for line in f_contents:
   # key,value = line.split("=")
    #resultsDict[key] = value.strip()
    
#f.close()

def change_password(newpwd):
 resultsDict["wpa_passphrase"] = newpwd
 print_file(resultsDict)


def print_file(result):
 newfile= open('/etc/hostapd/hostapd.conf' , 'w')   
 for key in result.keys():
    s = key + "=" + result[key]  + "\n"
    newfile.write(s) 
 newfile.close()

def newDictValues():
   with open('/etc/hostapd/hostapd.conf', "r") as f:
       f_contents = f.readlines()
   newDict = {}
   for line in f_contents:
     key,value = line.split("=")
     newDict[key] = value
   f.close()
   return newDict


def get_password(a, b):
   if a == b:
     return True
   else:
     return False

