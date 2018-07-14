#! /usr/bin/python3

def change_password(resultsDict, newpwd):
    return modify_config("wpa_passphrase", newpwd, resultsDict)

def print_file(resultsDict):
 newfile = open('/etc/hostapd/hostapd.conf' , 'w')   
 for key in resultsDict.keys():
    s = key + "=" + resultsDict[key]  + "\n"
    newfile.write(s) 
 newfile.close()

def modify_config(key, newValue, resultsDict):
    resultsDict[key] = newValue
    print_file(resultsDict)
    return resultsDict
    
def get_password(old, new, resultsDict):
  if resultsDict["wpa_passphrase"] == old:
    return (True, change_password(resultsDict, new))
  else:
    return (False, resultsDict)

def change_ssid(new_ssid, resultsDict):
    return modify_config("ssid", new_ssid, resultsDict)

def read_config():
    with open('/etc/hostapd/hostapd.conf', "r") as f:
        f_contents = f.readlines()
        resultsDict = {}
        for line in f_contents:
          key,value = line.split("=")
          resultsDict[key] = value.strip()
    f.close()
    return resultsDict