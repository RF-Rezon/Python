import time
import multiprocessing

# # Function 1
def task1():
    print("Task 1 started")
    time.sleep(3)
    print("Task 1 finished")


# Function 2
def task2():
    print("Task 2 started")
    time.sleep(3)
    print("Task 2 finished")


# # ----------------------------
# # Without Multiprocessing
# # ----------------------------
# start = time.time()

# task1()
# task2()

# end = time.time()

# print("\nWithout Multiprocessing Time:", end - start)


# ----------------------------
# With Multiprocessing
# ----------------------------
if __name__ == "__main__":

    start = time.time()

    p1 = multiprocessing.Process(target=task1)
    p2 = multiprocessing.Process(target=task2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print("\nWith Multiprocessing Time:", end - start)