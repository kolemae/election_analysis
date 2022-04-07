voting_data = []
voting_data.append({"county":"El Paso", "registered_voters": 461149})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data = (
    f"'county' county has 'voters:,' registered voters. ")
print(voting_data)
counties = ["Arapahoe", "Denver", "Jefferson"]
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict:
    print(counties_dict.get(county))
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")
for county_dict in voting_data:
    print(county_dict['county'])
candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What are the total number of votes in the election?"))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)