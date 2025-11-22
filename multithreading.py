import time
import threading

balance = 1000
lock = threading.Lock()   # to prevent race condition

def withdraw(name, amount):
    global balance
    print(name, "is trying to withdraw", amount)
    time.sleep(2)

    # Locking the critical section
    with lock:
        if balance >= amount:
            balance -= amount
            print(name, "Successfully withdrew", amount, "Remaining Balance:", balance)
        else:
            print(name, "Could not withdraw. Not enough balance!")

# creating two threads
t1 = threading.Thread(target=withdraw, args=("Ravi", 700))
t2 = threading.Thread(target=withdraw, args=("Amit", 700))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Balance:", balance)
