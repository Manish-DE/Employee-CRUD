# Function to find winner of an election where votes 
# are represented as candidate names 
from collections import Counter 

def winner(input):
    candidate = {} 
    winner=input,m
    for name in input:
        if name in sorted(candidate.keys(),reverse=True):
            candidate[name] += 1
        else:
            candidate[name] = 1

        if candidate[winner].values < candidate[name].values:
            winner = name;
        


    maxVote = sorted(candidate.keys(),reverse=True)
     




# Driver program 
if __name__ == "__main__": 
	input =['john','johnny','jackie','johnny', 
			'john','jackie','jamie','jamie', 
			'john','johnny','jamie','johnny', 
			'john'] 
	winner(input) 
