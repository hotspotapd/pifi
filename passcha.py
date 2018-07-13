#! /usr/bin/python3

def change_password(resultsDict, newpwd):
 resultsDict["wpa_passphrase"] = newpwd
 print_file(resultsDict)

def print_file(resultsDict):
 newfile= open('/etc/hostapd/hostapd.conf' , 'w')   
 for key in resultsDict.keys():
    s = key + "=" + resultsDict[key]  + "\n"
    newfile.write(s) 
 newfile.close()

def get_password(old, new, resultsDict):
      if resultsDict["wpa_passphrase"] == old:
        return (True, change_password(resultsDict, new))
      else:
        return (False, resultsDict)
