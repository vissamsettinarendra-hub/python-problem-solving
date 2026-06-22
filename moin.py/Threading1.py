#withthreading
# from threading import*
# import time
# def double(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("double:",2*n)
# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("square:",n*n)
# numbers = [1,23,4,5,6]
# begintime=time.time()
# print(time.time())
# t1 = Thread(target=double,args=(numbers,))
# t2 = Thread(target=squares,args=(numbers,)) 
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(time.time())
# print("the total time taken:",time.time()-begintime)  


# # Import everything from the threading module
# from threading import *

# # Import time module for sleep() and time() functions
# import time

# # Function to calculate double of each number
# def double(numbers):
#     # Loop through each number in the list
#     for n in numbers:
#         # Pause execution for 1 second
#         time.sleep(1)

#         # Print double of the current number
#         print("double:", 2 * n)

# # Function to calculate square of each number
# def squares(numbers):
#     # Loop through each number in the list
#     for n in numbers:
#         # Pause execution for 1 second
#         time.sleep(1)

#         # Print square of the current number
#         print("square:", n * n)

# # List of numbers
# numbers = [1, 23, 4, 5, 6]

# # Store the starting time
# begintime = time.time()

# # Print current timestamp
# print(time.time())

# # Create Thread 1
# # target = function to execute
# # args = arguments passed to the function
# t1 = Thread(target=double, args=(numbers,))

# # Create Thread 2
# t2 = Thread(target=squares, args=(numbers,))

# # Start Thread 1
# t1.start()

# # Start Thread 2
# t2.start()

# # Wait for Thread 1 to complete
# t1.join()

# # Wait for Thread 2 to complete
# t2.join()

# # Print ending timestamp
# print(time.time())

# # Calculate total execution time
# print("The total time taken:", time.time() - begintime)
 


#synchronization
# from threading import*
# import time
# def wish(name):
#     for i in range (10):
#         print("Good Evening:",end="")
#         time.sleep(1)
#         print(name)

# t1 = Thread(target = wish, args = ("Dhoni",))

# t2= Thread(target =wish, args= ("yuraj",))

# t1.start()

# t2.start()



# Import Thread class and other threading-related functions
from threading import *

# Import time module to use sleep()
import time

# Function that prints "Good Evening" followed by the given name
def wish(name):
    
    # Loop 10 times
    for i in range(10):
        
        # Print "Good Evening:" without moving to the next line
        print("Good Evening:", end="")
        
        # Pause execution for 1 second
        time.sleep(1)
        
        # Print the name passed to the function
        print(name)

# Create first thread object
# It will execute wish("Dhoni")
t1 = Thread(target=wish, args=("Dhoni",))

# Create second thread object
# It will execute wish("yuraj")
t2 = Thread(target=wish, args=("yuraj",))

# Start first thread
t1.start()

# Start second thread
t2.start()




# #lock
# from threading import*
# import time
# l = Lock()
# def wish(name):
#     l.acquire()
#     for i in range (10):
#         print("Good Evening:",end="")
#         time.sleep(1)
#         print(name)
#     l.release()    

# t1 = Thread(target = wish, args = ("Dhoni",))

# t2= Thread(target =wish, args= ("yuraj",))

# t3= Thread(target =wish, args= ("kohli",))

# t1.start()

# t2.start()

# t3.start()






# # Import all classes and functions from threading module
# from threading import *

# # Import time module for sleep()
# import time

# # Create a Lock object for synchronization
# # Only one thread can acquire this lock at a time
# l = Lock()

# # Function to print greeting messages
# def wish(name):
    
#     # Acquire the lock before entering the critical section
#     # Other threads must wait until the lock is released
#     l.acquire()
    
#     # Loop 10 times
#     for i in range(10):
        
#         # Print greeting without moving to next line
#         print("Good Evening:", end="")
        
#         # Pause execution for 1 second
#         time.sleep(1)
        
#         # Print the name
#         print(name)
    
#     # Release the lock after completing the task
#     # Now another waiting thread can execute
#     l.release()

# # Create Thread 1
# # It calls wish("Dhoni")
# t1 = Thread(target=wish, args=("Dhoni",))

# # Create Thread 2
# # It calls wish("yuraj")
# t2 = Thread(target=wish, args=("yuraj",))

# # Create Thread 3
# # It calls wish("kohli")
# t3 = Thread(target=wish, args=("kohli",))

# # Start Thread 1
# t1.start()

# # Start Thread 2
# t2.start()

# # Start Thread 3
# t3.start()




# #dead lock lock example
# from threading import*
# l =Lock()
# print("main thread trying to acquire Lock")
# l.acquire()
# print("main thread trying to acquire Lock Again")
# l.acquire()




# # Deadlock Example using Lock

# # Import all classes and functions from threading module
# from threading import *

# # Create a Lock object
# l = Lock()

# # Main thread tries to acquire the lock
# print("Main Thread trying to acquire Lock")
# l.acquire()

# # Lock is now acquired successfully by the main thread
# # No other thread can acquire it until it is released

# print("Main Thread trying to acquire Lock Again")

# # Main thread tries to acquire the same lock again
# # Since Lock is already held by the same thread,
# # it will wait forever for the lock to be released

# l.acquire()






#Rlock
from threading import*
import time
l = RLock()
def factorial(n):
    l.acquire()
    if n==0:
        result =1
    else:
        result = n*factorial(n-1)    
    l.release()
    return result
def result(n):
    print("the factorial of",n,"is",factorial(n))    

t1 = Thread(target = result, args = (5,))

t2= Thread(target =result, args= (9,))
t1.start()

t2.start()





# # RLock (Reentrant Lock) Example
# from threading import *      # Import Thread and RLock classes
# import time                  # Import time module

# # Create an RLock object
# # RLock allows the same thread to acquire the lock multiple times
# l = RLock()

# # Function to calculate factorial using recursion
# def factorial(n):

#     # Acquire the lock
#     l.acquire()

#     # Base condition
#     if n == 0:
#         result = 1
#     else:
#         # Recursive call
#         # Same thread acquires the lock again and again
#         result = n * factorial(n - 1)

#     # Release the lock
#     l.release()

#     # Return factorial result
#     return result

# # Function executed by each thread
# def result(n):

#     # Print factorial value
#     print("The factorial of", n, "is", factorial(n))

# # Create first thread
# t1 = Thread(target=result, args=(5,))

# # Create second thread
# t2 = Thread(target=result, args=(9,))

# # Start first thread
# t1.start()

# # Start second thread
# t2.start()





# from threading import*
# import time
# def producer():
#     time.sleep(1)
#     print("producer thread producing items:")
#     print("producer thread giving notification by setting event")
#     event.set()
# def consumer():
#     print("consumer thread is wating for updation")    
#     event.wait()
#     print("consumer thread got notification and consuming items")
# event = Event()
# t1=Thread(target = producer)
# t2=Thread(target = consumer)
# t1.start()
# t2.start()   






# # Import all classes and functions from threading module
# from threading import *

# # Import time module to use sleep()
# import time

# # Producer function
# def producer():
    
#     # Simulate production time by sleeping for 1 second
#     time.sleep(1)
    
#     # Producer creates/produces items
#     print("Producer Thread Producing Items:")
    
#     # Producer sends notification to waiting threads
#     print("Producer Thread Giving Notification By Setting Event")
    
#     # Set the event object
#     # All threads waiting on this event will be notified
#     event.set()

# # Consumer function
# def consumer():
    
#     # Consumer starts and waits for producer notification
#     print("Consumer Thread Is Waiting For Updation")
    
#     # Consumer waits until event is set by producer
#     event.wait()
    
#     # After receiving notification, consumer continues execution
#     print("Consumer Thread Got Notification And Consuming Items")

# # Create an Event object
# # Used for communication between threads
# event = Event()

# # Create producer thread
# t1 = Thread(target=producer)

# # Create consumer thread
# t2 = Thread(target=consumer)

# # Start producer thread
# t1.start()

# # Start consumer thread
# t2.start()