# Rabin-Karp algorithm in python
import tracemalloc
import time

# change this to how many possible inputs
d = 10

def search(pattern, text, q):
    patternLength = len(pattern)
    stringLength = len(text)
    patternHash = 0
    stringHash = 0
    h = 1
    i = 0
    j = 0

    for i in range(patternLength-1):
        h = (h*d) % q 

    # Calculate hash value for pattern and text
    for i in range(patternLength):
        patternHash = (d*patternHash + ord(pattern[i])) % q # hash value for pattern
        stringHash = (d*stringHash + ord(text[i])) % q # hash value for text

    # Find the match
    for i in range(stringLength-patternLength+1):
        if patternHash ==stringHash:
            for j in range(patternLength):
                if text[i+j] != pattern[j]:
                    break

            j += 1
            if j == patternLength:
                return str(i+1)

        if i < stringLength-patternLength:
            stringHash = (d*(stringHash-ord(text[i])*h) + ord(text[i+patternHash])) % q

            if stringHash < 0:
                stringHash = stringHash+q
		

# CHANGE HERE, ALSO CHANGE d VALUE ON LINE 6
# d value is the possible inputs, if numberical 10, if lowercase alphabet 26, if combined lower and upper 52
pattern = "ada"
text = "aaaadaaaaa"

# CHANGE THIS TO the next prime number from the length of text
q = 11

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