
#import modules for the program to recognize
import os
import csv

# create a path to the file
budgetDataCSV = os.path.join("..","Resources", "budget_data.csv")

with open(budgetDataCSV, 'r') as records:   # let records mean the journal of gains and losses
    recordsreader = csv.reader(records, delimiter=",")
    data = list(recordsreader)  # this is now reading the csv as a list (each row is a new list)
    data.pop(0)     # delete the first line so its not included. data moving forward will not have header
 
    lines = len(data)   # to calculate the number of entry dates in journal
    
    date = []
    amount = []

    for row in data:
        date.append(row[0])
        amount.append(int(row[1]))
        
        change = []
    
    for x in range(1, lines):
        change.append((int(amount[x]) - int(amount[x-1]))) # this month and day - previous month same day
        average = round(sum(change) / len(change),2)  
        
        totalamount = sum(amount) 
        avgamount = round(sum(amount)/len(amount),2)  
        minimum = min(change) 
        maximum = max(change) 

        minposition = change.index(minimum)+1   # +1 because we need current month (change took 1month back, this cancels it out)
        maxpsotion = change.index(maximum)+1    # ^^^^^^^^

        mindate = date[minposition]
        maxdate = date[maxpsotion]

    print(f"Financial Analysis")
    print(f"-------------------------------------------------")
    print(f"Total Months: {lines}")
    print(f"Total: ${totalamount}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {maxdate} (${maximum})")
    print(f"Greates Decrease in Profits: {mindate} (${minimum})")

newFile = open("output.txt","w")
newFile.write(f"Financial Analyis \n")
newFile.write(f"-------------------------------- \n")
newFile.write(f"Total Months: {lines} \n")
newFile.write(f"Total: ${totalamount} \n")
newFile.write(f"Average Change: ${average} \n")
newFile.write(f"Greatest Increase in Profits: {maxdate} (${maximum}) \n")
newFile.write(f"Greates Decrease in Profits: {mindate} (${minimum}) \n")

