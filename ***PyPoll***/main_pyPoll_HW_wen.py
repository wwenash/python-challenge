# Homework 03 Python PyPoll
# by: 03_Python_PyPoll_WEN_WASHSTL201809DATA3

#* The total number of votes cast
#* A complete list of candidates who received votes
#* The percentage of votes each candidate won
# * The total number of votes each candidate won
# * The winner of the election based on popular vote.
#* As an example, your analysis should look similar to the one below:

#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#  ```
#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# import packages
import os
import csv

# initialize variables
voterCount = 0
maxVote = 0
winner = " "

# make Lists/Dictionaries
Election = {}
myvotes = {}

# define input and output files
ElectionCSV = os.path.join('../../', 'WASHSTL201809DATA3','03-Python','Homework','Instructions','PyPoll','Resources', 'election_data.csv')
#testElectionCSV = os.path.join('../../', 'WASHSTL201809DATA3','03-Python','Homework','Instructions','PyPoll','Resources', 'TEST_election_data.csv')

with open(ElectionCSV, 'r') as electionFile:
#with open(testElectionCSV, 'r') as electionFile:

    resultsreader = csv.reader(electionFile, delimiter=',')
    header = next(resultsreader)

    for line in resultsreader:
        #print(line)
        Election[line[0]] = line[1:]

#print(f"{Election.keys()}")

# iterate over the elections dict to get total votes and make new dict 
# that contains only the number of votes for each canidate
for key, value in Election.items():
    voterCount += 1
    person = value[1]
    #print(f"{person}")
    
    if person not in myvotes.keys():
        myvotes.update({person:1})
    else:
        myvotes[person] += 1

#print(f"{myvotes} and total votes: {voterCount}")

print(f"\n\nElection Results")
print("-" * 25)
print(f"Total Votes: {voterCount}")
print("-" * 25)

# This loop is to get canidate, canidate votes and canidage percentage... plus print out
for key, value in myvotes.items():
    canidate = key
    canidateVotes = value
    #canidatePercent = round((canidateVotes / voterCount) * 100, 5)
    canidateTEST = (canidateVotes /voterCount) * 100
    print(str(canidate) + ": " + "%.3f" % (canidateTEST) + "% (" + str(canidateVotes) + ")")

    if canidateVotes > maxVote:
        maxVote = canidateVotes
        winner = canidate

print("-" * 25)
print(f"Winner: {winner}")
print("-" * 25 + "\n\n")
