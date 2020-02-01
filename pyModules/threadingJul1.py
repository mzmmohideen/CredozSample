from threading import Thread 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    a = 1
    while a:
        print('a', a)
        a+=1
        if a == 1000:
            a = 0
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__":
    print('session started')
    t1 = Thread(target=print_square, args=(10,))
    # print(dir(t1))
    t2 = Thread(target=print_cube, args=(10,))
    t1.start() 
    t1.join()       
    t2.start()
    # t2.join()

    print("DONE")
else:
    print("here it will work")
    print_square(10)
    print_cube(10)


    # creating thread 
    # t1 = threading.Thread(target=print_square, args=(10,)) 
    # t2 = threading.Thread(target=print_cube, args=(10,)) 
  
    # # starting thread 1 
    # t1.start() 
    # # starting thread 2 
    # t2.start() 
  
    # # wait until thread 1 is completely executed 
    # t1.join() 
    # # wait until thread 2 is completely executed 
    # t2.join()
    # both threads completely executed 
    print("Done!") 