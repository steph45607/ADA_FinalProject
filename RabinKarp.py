# Rabin-Karp algorithm in python
import tracemalloc
import time

# change this to how many possible inputs
d = 10

def search(pattern, text, q):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    for i in range(m-1):
        h = (h*d) % q 

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d*p + ord(pattern[i])) % q # hash value for pattern
        t = (d*t + ord(text[i])) % q # hash value for text

    # Find the match
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == m:
                return str(i+1)

        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

            if t < 0:
                t = t+q
		

# CHANGE HERE, ALSO CHANGE d VALUE ON LINE 6
text = "ABCCDDAEFG"
pattern = "CDDE"
# CHANGE THIS TO the next prime number from the length of text
q = 13

tracemalloc.start()
start = time.time()
x = search(pattern, text, q)
end = time.time()
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.clear_traces()

print("time: " + str(end-start))
print("memory: " + str(memory[1]))
if x == None:
	print("Not found")
else:
	print("Found at index: " + (x))