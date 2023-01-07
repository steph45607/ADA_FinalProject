# Python3 program for Naive Pattern
# Searching algorithm
import tracemalloc
import time

def search(pat, txt):
    M = len(pat)
    N = len(txt)

    # A loop to slide pat[] one by one */
    for i in range(N - M + 1):
        j = 0

        # For current index i, check
        # for pattern match */
        while (j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1

        if (j == M):
            return i


# Driver's Code
txt = "AABAACAADAABAAABAA"
pat = "AABCA"

tracemalloc.start()
start = time.time()
x = search(pat, txt)
end = time.time()
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.clear_traces()

print("time: " + str(end-start))
print("memory: " + str(memory[1]))
if x == None:
	print("Not found")
else:
	print("Found at index: " + str(x))

# This code is contributed
# by PrinciRaj1992
