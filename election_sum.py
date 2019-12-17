import csv
import pprint
total_votes = 0
candidate_option = []
vote_precent = []
candidate_votes = {}
winner = ""
winning_count = 0


with open("election_data.csv", "r") as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        total_votes = total_votes + 1
        candidate_name = row["Candidate"]
        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)
            candidate_votes[candidate_name] = 0
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
     
        
    election_results = (
        f"\nElection Results\n"
        f"====================\n"
        f"Total Votes: {total_votes}\n"
        f"====================\n"
        f"{candidate_votes}\n"
    )

    

print (election_results)

