import csv
rowOut0head = "Election Results"
rowOut1dash = "----------------------------"
rowOut2totVotes = "Total Votes: "
candidateLIST = []
winnername = ""
voteCTtot = 0
voteCT = 0
recentCandidate = ""
priorWinnerScore = 0.0
z = 0

def take3rd(elem):
    return elem[2]

with open('election_data.csv', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

for c in data:
    voteCTtot += 1
list_len = len(data)
print(list_len)
    
voteCTtot -= 1
    
data.sort(key=take3rd)
    
for y in data:
    z += 1
    if y[0] == 'Ballot ID' or y[0] == '':
        VoteCT = 0
        continue
    voteCT += 1
    # add any non-zero-vote to candidate result list if candidate name changes
    if y[2] != recentCandidate:
        print(recentCandidate)   # ##### TEST TEST TEST TEST
        if recentCandidate != "" :
            candidateLIST.append([recentCandidate, '('+str(round(voteCT/voteCTtot*100.0,2))+'%)', str(voteCT) ])
            if voteCT > priorWinnerScore:
                priorWinnerScore = voteCT
                winnername = y[2]
        recentCandidate = y[2]
        VoteCT = 0
    elif  z == list_len-1:
        print(y[2])   # ##### TEST TEST TEST TEST
        if recentCandidate != "" :
            candidateLIST.append([y[2], '('+str(round(voteCT/voteCTtot*100.0,2))+'%)', str(voteCT) ])
            if voteCT > priorWinnerScore:
                priorWinnerScore = voteCT
                winnername = y[2]

rowOut2totVotes = rowOut2totVotes + str(voteCTtot)
    
print(rowOut1dash)
print(rowOut0head)
print(rowOut1dash)
print(rowOut2totVotes)
print(rowOut1dash)
for x in candidateLIST:
    print(*x)
print(rowOut1dash)
print('Winner: ' + winnername)

with open('results.txt', 'w', encoding='utf-8') as myfileOUT:
    myfileOUT.write(rowOut0head + "\n")
    myfileOUT.write(rowOut1dash + "\n")
    myfileOUT.write(rowOut2totVotes + "\n")
    myfileOUT.write(rowOut1dash + "\n")
    
    for item in candidateLIST:
        myfileOUT.write("{}\n".format(item))
 
    myfileOUT.write(rowOut1dash + "\n")
    myfileOUT.write('Winner: ' + winnername + "\n")