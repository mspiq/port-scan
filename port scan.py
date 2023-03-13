from socket import *
print '''
                   _                         
                  | |                        
  _ __   ___  _ __| |_   ___  ___ __ _ _ __  
 | '_ \ / _ \| '__| __| / __|/ __/ _` | '_ \ 
 | |_) | (_) | |  | |_  \__ \ (_| (_| | | | |
 | .__/ \___/|_|   \__| |___/\___\__,_|_| |_|
 | |                                         
 |_|                                        
by Mohamed Salah
https://www.facebook.com/mspiq

'''
target = raw_input ("Enter host to scan :")
TRIP = gethostbyname(target)
print "scan to host ip=", TRIP

for i in range (20, 1000):
    f = socket(AF_INET, SOCK_STREAM)

    x = f.connect_ex((TRIP, i))

    if(x == 0) :
        print "print open =", i
