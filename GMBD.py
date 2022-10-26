import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        import GMZBD
 
 
 
elif bit == "32bit":
 
        import BDXGM
 
