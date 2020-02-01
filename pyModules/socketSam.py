import socket                
  
# next create a socket object 
s = socket.socket()
print "Socket successfully created"
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 8010               
  
address = ('0.0.0.0', 8010)
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(address)
print "socket binded to %s" %(port) 
  
# put the socket into listening mode 
s.listen(5)      
print "socket is listening"            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print 'Got connection from', addr 
   inp = raw_input("Your Name:")
  
   # send a thank you message to the client.  
   c.send('Welcome %s'%inp) 
  
   # Close the connection with the client 
   # c.close() 


# import socket # for socket 
# import sys  
  
# try: 
#     s = socket.socket() 
#     print "Socket successfully created"
# except socket.error as err: 
#     print "socket creation failed with error %s" %(err) 
  
# # default port for socket 
# port = 80
  
# try: 
#     host_ip = socket.gethostbyname('www.google.com') 
# except socket.gaierror: 
  
#     # this means could not resolve the host 
#     print "there was an error resolving the host"
#     sys.exit() 
  
# # connecting to the server 
# s.connect((host_ip, port))   
# print "the socket has successfully connected to google \
# on port == %s" %(host_ip) 



# Check out pyftpdlib from Giampaolo Rodola. It is one of the very best ftp servers out there for python. It's used in google's chromium (their browser) and bazaar (a version control system). It is the most complete implementation on Python for RFC-959 (aka: FTP server implementation spec).

# From the commandline:

# python -m pyftpdlib
# Alternatively 'my_server.py':

# #!/usr/bin/env python



# from pyftpdlib import servers
# from pyftpdlib.handlers import FTPHandler
# address = ("0.0.0.0", 21)  # listen on every IP on my machine on port 21
# server = servers.FTPServer(address, FTPHandler)
# server.serve_forever()	