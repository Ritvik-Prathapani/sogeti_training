import threading
import time

class TicketBookingSystem:
    def __init__(self, total_tickets):
        self.total_tickets = total_tickets  # Total available tickets
        self.lock = threading.Lock()  # Lock to prevent race conditions

    def book_ticket(self, user, num_tickets):
        with self.lock:  # Ensure only one thread modifies tickets at a time
            print(f"{user} is trying to book {num_tickets} tickets...")
            time.sleep(1)  # Simulating booking delay

            if self.total_tickets >= num_tickets:
                self.total_tickets -= num_tickets
                print(f"{user} successfully booked {num_tickets} ticket(s).")
            else:
                print(f"Sorry, {user}, not enough tickets available.")

            print(f"Remaining tickets: {self.total_tickets}")

# Initialize the booking system with 5 tickets
ticket_system = TicketBookingSystem(total_tickets=5)

# List of users and their ticket requests
users = [
    ("Alice", 2),
    ("Bob", 1),
    ("Charlie", 3),
    ("David", 2)
]

# Create and start threads for each user trying to book tickets
threads = []
for user, num_tickets in users:
    thread = threading.Thread(target=ticket_system.book_ticket, args=(user, num_tickets))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All booking requests processed!")
