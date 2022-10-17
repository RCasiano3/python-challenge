import os
import csv

#Assigning the path to pull the csv file and data and output path to place txt file
filepath = os.path.join("Resources", "budget_data.csv")
outfile = os.path.join("analysis", "FinancialAnalysisResults.txt")

#Opening the csv file to read
with open(filepath, "r") as infile:
    incsv = csv.reader(infile)
    
    csvheader = next(incsv)

#Definition of variables utilized
    profits = []
    months = []
    revchg = []

    #Seperating the profit and months provided within the data
    for row in incsv:
        profits.append(int(row[1]))
        months.append(row[0])
    
    #Calculating the total months request and the total profit requested
    ttlmonths = len(months)
    ttlprofits = sum(profits)
    
    #Calculating the change in revenue
    for c in range(1, len(profits)):
        revchg.append((int(profits[c]) - int(profits[c-1])))
    
    #Calculating the average revenue change, the greatest increase of revenue & the greatest decrease of revenue
    revavg = sum(revchg) / len(revchg)
    grtincrease = max(revchg)
    grtdecrease = min(revchg)
  
    #Printing the final values for each requested value
    print("Financial Analysis")
    
    print("_"*28)
    
    print("Total Months: " + str(ttlmonths))
    
    print("Total: " + "$" + str(ttlprofits))
    
    print("Average Change: " + "$" + str(round(revavg,2)))
    
    print("Greatest Increase in Profits: " + str(months[revchg.index(max(revchg))+1]) + " " + "$" + str(grtincrease))
    print("Greatest Decrease in Profits: " + str(months[revchg.index(min(revchg))+1]) + " " + "$" + str(grtdecrease))

#Export of financial analysis results to text file
with open(outfile, "w+") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("____________________________\n")
    txtfile.write("\n")
    txtfile.write("Total Months: " + str(ttlmonths))
    txtfile.write("\n")
    txtfile.write("Total: " + "$" + str(ttlprofits))
    txtfile.write("\n")
    txtfile.write("Average Change: " + "$" + str(round(revavg, 2)))
    txtfile.write("\n")
    txtfile.write("Greatest Profit Increase: " + str(months[revchg.index(max(revchg))+1]) + " " + "$" + str(grtincrease))
    txtfile.write("\n")
    txtfile.write("Greatest Profit Decrease: " + str(months[revchg.index(min(revchg))+1]) + " " + "$" + str(grtdecrease))
