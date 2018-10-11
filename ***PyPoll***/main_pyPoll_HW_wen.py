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
#
### End of Instructions ###

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
input_ElectionCSV = os.path.join('.', 'Python_HomeWork_input', 'election_data.csv')
#testinput_ElectionCSV = os.path.join('.','Python_HomeWork_input', 'TEST_election_data.csv')
outputFile = os.path.join('.', 'Python_HomeWork_output', 'PyPoll_ElectionResults.txt')

# open the data... for reading, split on commas, skip header,
# and make hash
with open(input_ElectionCSV, 'r') as electionFile:
#with open(testinput_ElectionCSV, 'r') as electionFile:

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

# Write all of the PyBank Analysis data to Text file:
with open(outputFile, "w", newline="") as outtextfile:

    print(f"\n\nElection Results")
    print(f"\n\nElection Results", file=outtextfile)
    print("-" * 25)
    print("-" * 25, file=outtextfile)
    print(f"Total Votes: {voterCount}")
    print(f"Total Votes: {voterCount}", file=outtextfile)
    print("-" * 25)
    print("-" * 25, file=outtextfile)

    # This loop is to get canidate, canidate votes and canidage percentage... plus print out
    for key, value in myvotes.items():
        canidate = key
        canidateVotes = value
        #canidatePercent = round((canidateVotes / voterCount) * 100, 5)
        canidateTEST = (canidateVotes /voterCount) * 100
        print(str(canidate) + ": " + "%.3f" % (canidateTEST) + "% (" + str(canidateVotes) + ")")
        print(str(canidate) + ": " + "%.3f" % (canidateTEST) + "% (" + str(canidateVotes) + ")", file=outtextfile)

        if canidateVotes > maxVote:
            maxVote = canidateVotes
            winner = canidate

    print("-" * 25)
    print("-" * 25, file=outtextfile)
    print(f"Winner: {winner}")
    print(f"Winner: {winner}", file=outtextfile)
    print("-" * 25 + "\n\n")
    print("-" * 25 + "\n\n", file=outtextfile)
