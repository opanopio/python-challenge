import os
import csv
import collections

csvpath = os.path.join("..//PyRoll//Resources//election_data.csv")

with open(csvpath) as pyrollfile:

    csvreader = csv.reader(pyrollfile, delimiter=',')
    header = next(csvreader)

    total_votes= 0

    print("Election Results")
    print("________________")

    for pyroll in csvreader:

        total_votes += 1
    print(f"Total Votes: {total_votes}")
    print("________________")
    
        #CCVotes_Rec= row[2]
    print("Charles Casper Stockham: {Percent_Votes} {CCVotes_Rec}")


    print("Diana DeGette: {Percent_Votes} {Votes_Rec}")


    print("Raymon Anthony Doane: {Percent_Votes} {Votes_Rec}")
    print("________________")
    print("Winner: {Winr}")
    print("________________")

    #create a list who voters voted for
    #create a dict for the vote count
    #Key is the candidate name
    #For Loop needed to pull votes
