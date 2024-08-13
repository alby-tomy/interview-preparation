import time
import threading

def print_number():
    for i in range(1,6):
        time.sleep(1)
        print(f"number : {i}")
        
def sequence_print():
    for i in range(1,6):
        time.sleep(1.5)
        print(f"sequence number {i}")
        
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=sequence_print)

# starting threading

t1.start()
t2.start()

# Wait for both threads to complete
t1.join()
t2.join()

print("Done with multithreading!")