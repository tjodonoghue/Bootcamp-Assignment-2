
import pandas as pd

#Import the CSV file to read
path = r"C:\Users\Gamer PC\Desktop\Git\Bootcamp-Assignment-2\PyPoll\election_data.csv"
df = pd.read_csv(path)
df

#Finding total number of votes
num_votes=len(df["Ballot ID"])
print(num_votes) 

#Finding each unique candidate 
candidates= df["Candidate"].unique()
print(candidates)

#Finding percentage of votes for each candidate, rounded to 3 digits. 
percent_for_candidate = round((((df["Candidate"].value_counts())/369711) * 100), 3)
print(percent_for_candidate)

#Finding total number of votes for each candidate
total_for_candidate = df["Candidate"].value_counts()
print(total_for_candidate)

#To find the winner, I find where the highest value is equal to the total votes in candidates
most_votes = total_for_candidate.max()
print(most_votes)
winner = total_for_candidate[total_for_candidate == most_votes].index[0]
print(winner) 

#Finally, we print the results
report_text = f""" Election Results

------------------------------------

Total Votes: {num_votes}

------------------------------------

"""

for candidate in candidates: 
    report_text = report_text + f"{candidate}: {percent_for_candidate[candidate]}% ({total_for_candidate[candidate]})\n"

winner_text = f"""

-------------------------------------

Winner: {winner} 
"""
result_text = report_text + winner_text

with open("election_results.txt", "w") as file:
    file.write(result_text)

print(result_text)
