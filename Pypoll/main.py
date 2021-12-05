
#   PyPoll - election results anaysis

import os
import csv

#   declare dictionaries, variables for candidate's name and votes, and winner's name and votes
total_votes = 0
candidate = ""
candidate_votes = {}
candidate_percentages ={}
winner_votes = 0
winner = ""
	
#   set the path to the input and output files
file_to_analyse = os.path.join("Resources", "election_data.csv")
analysis_file_to_output = os.path.join("analysis", "election_analysis.txt")

#   open the file to analyse and set the delimiter
with open(file_to_analyse) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

#   read the header row
    csv_header = next(csv_reader)

#   tally up the votes for each candidate
    for row in csv_reader:
        total_votes = total_votes + 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] = candidate_votes[candidate] + 1
        else:
            candidate_votes[candidate] = 1

#   calculate percentage of votes for each candidate and identify the winner
for this_candidate, vote_count in candidate_votes.items():
    candidate_percentages[this_candidate] = '{0:.0%}'.format(vote_count / total_votes)
    if vote_count > winner_votes:
        winner_votes = vote_count
        winner = this_candidate

#   print out the results to the terminal
print("-------------------------")
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for this_candidate, vote_count in candidate_votes.items():
    print(f"{this_candidate}: {candidate_percentages[this_candidate]} ({vote_count})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#   save the results to the election results file
with open(analysis_file_to_output,'w') as text:
    text.write("-------------------------" + "\n")
    text.write(f"Total Votes: {total_votes}" + "\n")
    text.write("-------------------------" + "\n")
    for this_candidate, vote_count in candidate_votes.items():
        text.write(f"{this_candidate}: {candidate_percentages[this_candidate]} ({vote_count})" + "\n")
    text.write("-------------------------" + "\n")
    text.write(f"Winner: {winner}" + "\n")
    text.write("-------------------------" + "\n")

