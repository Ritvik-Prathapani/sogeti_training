import threading
import time

def daemon_task():
    while True:
        print("Daemon thread running...")
        time.sleep(1)

# def non_daemon_task():
#     for i in range(5):
#         print("Non-daemon thread running...")
#         time.sleep(1)

# Creating a daemon thread
daemon_thread = threading.Thread(target=daemon_task, daemon=True)

# # Creating a non-daemon thread
# non_daemon_thread = threading.Thread(target=non_daemon_task)

# # Start both threads
daemon_thread.start()
# non_daemon_thread.start()

# # Wait for the non-daemon thread to finish
# non_daemon_thread.join()
time.sleep(5)
print("Main thread exiting...")
