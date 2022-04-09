import csv
rowOut0head = "Financial Analysis"
rowOut1dash = "----------------------------"
rowOut2totMon = "Total Months: "
rowOut3tot = "Total: "
rowOut4AvgChg = "Average Change: "
rowOut5bigInc = "Greatest Increase in Profits: "
rowOut6bigDec = "Greatest Decrease in Profits: "
rowCTR = 0
rowSUM = 0.0
priorVAL = 0.0
changeSUM = 0.0
deltaMaxIncrease = 0.0
deltaMaxDecrease = 0.0

with open('budget_data.csv', encoding='utf-8') as myfile:
    reader = csv.reader(myfile, delimiter=',')
    print(reader)
    csv_header = next(reader)
    print(f"CSV Header: {csv_header}")
    for row in reader:
        rowCTR += 1
        rowSUM += float(row[1])
        changeSUM += float(row[1]) - priorVAL
        if float(row[1]) - priorVAL > deltaMaxIncrease:
            deltaMaxIncrease = float(row[1]) - priorVAL
        if priorVAL - float(row[1]) > deltaMaxDecrease:
            deltaMaxDecrease = float(row[1]) - priorVAL      
            
        priorVal = float(row[1])
        
rowOut2totMon = rowOut2totMon + str(rowCTR)
rowOut3tot = rowOut3tot + "${:,.2f}".format(rowSUM)
rowOut4AvgChg = rowOut4AvgChg + "${:,.2f}".format(changeSUM/rowCTR)
rowOut5bigInc = rowOut5bigInc + "${:,.2f}".format(deltaMaxIncrease)
rowOut6bigDec = rowOut6bigDec + "${:,.2f}".format(deltaMaxDecrease)

print(rowOut0head)
print(rowOut1dash)
print(rowOut2totMon)
print(rowOut3tot)
print(rowOut4AvgChg)
print(rowOut5bigInc)
print(rowOut6bigDec)

with open('results.txt', 'w', encoding='utf-8') as myfileOUT:
    myfileOUT.write(rowOut0head + "\n")
    myfileOUT.write(rowOut1dash + "\n")
    myfileOUT.write(rowOut2totMon + "\n")
    myfileOUT.write(rowOut3tot + "\n")
    myfileOUT.write(rowOut4AvgChg + "\n")
    myfileOUT.write(rowOut5bigInc + "\n")
    myfileOUT.write(rowOut6bigDec + "\n")