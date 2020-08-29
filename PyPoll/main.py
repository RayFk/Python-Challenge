# import csv modules
import csv
# import operating system modules
import os

# define csv_path
csv_path = os.path.join("Resources", "election_data.csv")

# define output text file
txt_path = os.path.join("analysis", "election_analysis.txt")

# opening csv file and storing as csv_file
with open(csv_path, newline="") as csv_file:

    # use csv_reader to read file content
    csv_reader = csv.reader(csv_file, delimiter=",")

    # print csv_reader (contents of csv file)
    # print(csv_reader)

    # define and store header
    csv_header = next(csv_reader)

    # print header
    # print(csv_header)

    # define total votes
    votes = 0

    # create candidate dictionary to store candidates and vote count
    candidates = {}

    # iterate over all rows in csv_file and add contents to list
    for row in csv_reader:

        # keep track of total votes and  candidate votes
        # votes.append(row[0])
        votes += 1
        # check if candidate exists in candidates dictionary.
        # if so, increment vote count by 1, else add candidates to dictionary
        curr_candidate = row[2]

        if curr_candidate in candidates:
            candidates[curr_candidate] += 1
        else:
            candidates[curr_candidate] = 1

    # verify length of votes
    # print(votes)

    # print out a specific candidates vote count
    # print(candidates["Khan"])

    # create candidate vote percentage dictionary
    vote_percentage = {}

    # store pairs of candidates in vote count for printing
    pairs = candidates.items()

    # define winner
    winner = ("", 0)

    # iterate over candidates dictionary and calculate vote percentage
    for item in pairs:
        # testing values
        # print(item)
        candidate = item[0]
        # create a variable to calculate current candidate vote percentage
        percentage = (candidates[candidate] / votes) * 100
        # check current winner
        if item[1] > winner[1]:
            winner = item
        # store candidate percentage in vote percenage dictionary
        vote_percentage[candidate] = percentage

        # print vote percentage dictionary
        # print(vote_percentage[candidate])

        # print values on terminal
    print("Election Results")
    print("-------------------------")
    print("Total Votes: {}".format(votes))
    print("-------------------------")
    # print all trios of candidate, vote count, percentage
    for pair in pairs:
        print("{0}: {1:.2f}% ({2})".format(
            pair[0],round(vote_percentage[pair[0]],2), pair[1]))
    print("-------------------------")
    print("Winner: {}".format(winner[0]))
    print("-------------------------")

        # writing analysis to text file
with open(txt_path, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("----------------------------\n")
    txt_file.write("Total Votes: {}\n".format(votes))
    txt_file.write("----------------------------\n")
    for pair in pairs:
        txt_file.write("{0}: {1:.2f}% ({2})\n".format(
            pair[0],round(vote_percentage[pair[0]],2), pair[1]))
    txt_file.write("-------------------------\n")
    txt_file.write("Winner: {}\n".format(winner[0]))
    txt_file.write("-------------------------\n")
