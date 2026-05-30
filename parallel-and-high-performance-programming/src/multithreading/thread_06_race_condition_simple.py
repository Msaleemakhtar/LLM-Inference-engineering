import threading  # Threading module to create and manage threads
import time  # Time module used for sleeping to simulate work

# Shared variable accessed and modified by both threads
shared_data = 0

def funcA():
	# Declare that we intend to modify the module-level `shared_data`
	global shared_data
	# Loop 10 times to perform repeated updates
	for i in range(10):
		# Read the shared value into a local variable to simulate read-modify-write
		local = shared_data
		# Increment the local copy by 10
		local += 10
		# Sleep to simulate work and create opportunities for context switches
		time.sleep(1)
		# Write the updated local value back to the shared variable
		shared_data = local
		# Print the value written by Thread A for debugging/visibility
		print("Thread A wrote: %s" % shared_data)


def funcB():
	# Declare that we intend to modify the module-level `shared_data`
	global shared_data
	# Loop 10 times to perform repeated updates
	for i in range(10):
		# Read the shared value into a local variable to simulate read-modify-write
		local = shared_data
		# Decrement the local copy by 10
		local -= 10
		# Sleep to simulate work and create opportunities for context switches
		time.sleep(1)
		# Write the updated local value back to the shared variable
		shared_data = local
		# Print the value written by Thread B for debugging/visibility
		print("Thread B wrote: %s" % shared_data)


# Create two threads, one running `funcA` and the other `funcB`
t1 = threading.Thread(target=funcA)
t2 = threading.Thread(target=funcB)

# Start both threads so they run concurrently
t1.start()
t2.start()

# Wait for both threads to finish before exiting the program
t1.join()
t2.join()