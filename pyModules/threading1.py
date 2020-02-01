import threading
import os
import sys
  
def printcube(num):
    """ 
    function to print(cube of given num )
    """
    print("Cube: {}".format(num * num * num))
  
def printsquare(num):
    a = 1
    while a:
        a+=1
        print('a', a)
        if a == 1000:
            a = 0
    """ 
    function to print(square of given num )
    """
    print("Square: {}".format(num * num))
  
def pipe():   

    print("The child will write text to a pipe and ")
    print("the parent will read the text written by child...")

    # file descriptors r, w for reading and writing
    r, w = os.pipe() 

    processid = os.fork()
    print('processid', processid)
    if processid:
       # This is the parent process 
       # Closes file descriptor w
       os.close(w)
       r = os.fdopen(r)
       print("Parent reading")
       str = r.read()
       print("text =", str   )
       sys.exit(0)
    else:
       # This is the child process
       os.close(r)
       w = os.fdopen(w, 'w')
       print("Child writing")
       w.write("Text written by child...")
       w.close()
       print("Child closing")
       sys.exit(0)

#fork
def child():
   print('\nA new child ',  os.getpid())
   os._exit(0)  

def parent():
   while True:
      newpid = os.fork()
      if newpid == 0:
         child()
      else:
         pids = (os.getpid(), newpid)
         print("parent: %d, child: %d\n" % pids)
      reply = raw_input("q for quit / c for new fork")
      if reply == 'c': 
          continue
      else:
          break

if __name__ == "__main__": 
    # creating thread 
    # t1 = threading.Thread(target=printsquare, args=(10,))
    # t2 = threading.Thread(target=printcube, args=(10,))
  
    # # # starting thread 1 
    # t1.start() 
    # # t1.join()
    # # # starting thread 2 
    # t2.start() 
  
    # # wait until thread 1 is completely executed 
    # t1.join() 
    # # wait until thread 2 is completely executed 
    # t2.join() 
    # print(square(10))
    # print(cube(10))
    # both threads completely executed 
    # print("Done!") )
    pipe()
    # pipe()
else:
  printsquare(10)
  printcube(10)