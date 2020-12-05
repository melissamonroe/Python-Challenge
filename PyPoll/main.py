import os
import csv

# col headers Voter ID, County, and Candidate.
# The total number of votes cast
voteid_count = 0

# A complete list of candidates who received votes
name_list = []

candidate_list = []
# The percentage of votes each candidate won
# The total number of votes each candidate won
name_votes = []

candidates = {}
candidate = {}
# The winner of the election based on popular vote.

# Path to collect data from the Resources folder
input_path = "Resources\election_data.csv"

# Read in the CSV file
with open(input_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        # print(row)

        # increment total vote count
        voteid_count += 1

        name = row[2]

        if name not in name_list:
            # add name to names
            name_list.append(name)

            candidate = {
                "name": name,
                "votes": 1
            }
            candidate_list.append(candidate)
            candidates = candidate_list
        else:
            # find candidate and increment their vote
            candidate_index = 0
            for candidate in candidates:
                if candidate["name"] == name:
                    # increment candidate vote
                    candidate_vote_count = candidate["votes"] + 1
                    candidate = {
                        "name": name,
                        "votes": candidate_vote_count,
                    }
                    break
                # increment candidate index
                candidate_index += 1

            # replace existing candidate with updated vote count
            candidate_list[candidate_index] = candidate

        # for testing to break faster
        # if voteid_count > 200:
        #     break


############# Election Report #############

election_report_text = '-------------------------\n'
election_report_text = 'Election Results\n'
election_report_text += '-------------------------\n'
election_report_text += f'Total Votes: {voteid_count}\n'
election_report_text += '-------------------------\n'

max_candidate = {"name": "", "votes": 0}

for candidate in candidates:
    # calculate vote percent = {candidate["votes"]} / total votes
    vote_percent = round((candidate["votes"] / voteid_count), 3) * 100
    election_report_text += f'{candidate["name"]} {vote_percent}% ({candidate["votes"]}) \n'
    if candidate["votes"] > max_candidate["votes"]:
        max_candidate = candidate


election_report_text += '-------------------------\n'
election_report_text += f'Winner: {max_candidate["name"]}\n'
election_report_text += '-------------------------\n'

# print report to console
print(election_report_text)

# save election report to Analysis dir
election_report = open(os.path.join(
    '', 'Analysis', 'election_report.txt'), "w")
election_report.write(election_report_text)
election_report.close()


"""
Example Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
"""
