import pandas as pd
import numpy as np

# Import file
election_data = pd.read_csv('./python-challenge/PyPoll/Resources/election_data.csv')

# total number of votes cast
total_votes = len(election_data)

# define some valueables
i = 0

# A complete list of candidates who received votes and how many votes for each of them
election = election_data.Candidate.value_counts()

#specify path for export
path = r'./python-challenge/PyPoll/analysis/winner_analysis.txt'


#export to text file
with open(path, 'a') as f:
    f.truncate(0)
    f.write('Election Results\n')
    f.write('----------------------------\n')
    f.write('Total Votes: ' + str(total_votes) + '\n')
    f.write('----------------------------\n')
    while i <= len(election) - 1:
        percentage =f"{election[i] / total_votes:.3%}" 
        print(percentage)
        i = i + 1
        f.write(str(election.index.values[i - 1]) + ': ' + str(percentage) + "(" + str(election[i-1]) + ")" + "\n")
    f.write('----------------------------\n')
    f.write('Winner: ' + election.idxmax() + '\n')
    f.write('----------------------------\n')
