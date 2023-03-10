# Python program for Finite Automata
# Pattern searching Algorithm

import time #to track run time
import tracemalloc #to track memory usage

# charNo is the number of characters in the input alphabet
charNo = 256

# pat -> pattern we want to search
# txt -> text test case
# patLength -> length of the pattern
# x -> next matching character of the pattern 
# nextState -> variable to store the next state 
#			-> it will be the variable to store the longest pattern match. 


#function to calculate the next state from the current state
def getNextState(pat, patLength, state, x):

	#if the state is still lesser than the patLength, it means that it has not reached the final state
	#therefore it will continue to traverse 

	#but paired with the and statement x, 
	#it means that if it has not reached the final state and met the same character while traversing, it will increment states.
	if state < patLength and x == ord(pat[state]):
		return state+1
	i=0

	#for loop to traverse through all the states
	for nextState in range(state,0,-1):
		if ord(pat[nextState-1]) == x: #if we are approaching the next state that is the next character of the pattern we search
			while(i<nextState-1):
				if pat[i] != pat[state-nextState+1+i]: #if encountered a character mismatch for the character after the approaching character (found by index)
					break							   #the current point of the nextState will not be stored
				i+=1								   #continue traversal.
			if i == nextState-1:	#if found the match for the approaching character, store the point as the next state
				return nextState	#and return the value.
	return 0


#This is the known function to build the Finite Automata transition table for a given pattern
def computeTransitionTable(pat, patLength):
	global charNo
	#prompt transition table 
	TT = [[0 for i in range(charNo)]\
		for _ in range(patLength+1)]
	for state in range(patLength+1):
		for x in range(charNo):
			call = getNextState(pat, patLength, state, x) #calling the function to traverse and collect the states
			TT[state][x] = call #input to the table adding the values of the states
	return TT

#main function to initiate the pattern search
def search(pat, txt):
	global charNo
	patLength = len(pat)
	textLength = len(txt)
	TT = computeTransitionTable(pat, patLength) #start the process of building the transition table
	state=0	#starting state declaration
	for i in range(textLength):
		state = TT[state][ord(txt[i])] #traversing through the input pattern
		if state == patLength:		   #if pattern is found, print the index
			print("Pattern found at index: {}".\
				format(i-patLength+1)) 
	print("Search Finished")			#once done with all the search, it will print this statement

txt ="pRiVeT"
pat = "privet"

start = time.time()
tracemalloc.start()
search(pat, txt)

end = time.time()
memory = tracemalloc.get_traced_memory()
tracemalloc.stop()
tracemalloc.clear_traces()

print("======================================================")
print("\nMemory (current, peak): ", memory)
print("\nTime: ", end-start, " seconds")
print("\nText : " + "\n" + txt)
print("\nPattern : " + pat)
print("======================================================")

#this code is inspired by Atul Kumar