import os
import csv

#Assigning the path to pull the csv file data and output path to place txt file
filepath = os.path.join("Resources", "election_data.csv")
outfile = os.path.join("analysis", "ElectionResults.txt")

#Definition of variables utilized
ttlvotes = 0
candidates = []
candidatevotes = []

#Reading of data and calculation of votes per candidate
with open(filepath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        ttlvotes += 1
        candidatein = (row[2])
        if candidatein in candidates:
            candidateindex = candidates.index(candidatein)
            candidatevotes[candidateindex] = candidatevotes[candidateindex] + 1
        else:
            candidates.append(candidatein)
            candidatevotes.append(1)
            
#Calculation of percentage of votes and maximum votes per candidate
percentage = []
maxvotes = candidatevotes[0]
maxindex = 0

for x in range(len(candidates)):
    voteperc = round(candidatevotes[x]/ttlvotes*100, 3)
    percentage.append(voteperc)
    if candidatevotes[x] > maxvotes:
        maxvotes = candidatevotes[x]
        maxindex = x
electionwinner = candidates[maxindex]

#Printing of data analysis results within Terminal
print('Election Results')
print('-'*25)
print(f'Total Votes: {ttlvotes}')
print('-'*25)
for x in range(len(candidates)):
    print(f'{candidates[x]} : {percentage[x]:.3f}% ({candidatevotes[x]})')
print('-'*25)
print(f'Winner: {electionwinner}')
print('-'*25)
#Output printing of data analysis results to text file
with open(outfile, "w+") as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Total Votes: {ttlvotes}\n')
    txtfile.write('-------------------------\n')
    for x in range(len(candidates)):
        txtfile.write(f'{candidates[x]} : {percentage[x]:.3f}% ({candidatevotes[x]})\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Winner: {electionwinner}\n')
    txtfile.write('-------------------------\n')
