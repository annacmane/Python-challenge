
#Import modules for this csv
import os
import csv

# Path to collect data from CSV
PyPoll_csv = os.path.join("..","Resources","election_data.csv")

with open(PyPoll_csv, 'r') as Pollcsv:
    pollReader = csv.reader(Pollcsv, delimiter=",")
    polldata = list(pollReader) #   converts reader into a list
    polldata.pop(0) # deletes first line from file that held the headers. no more headers going forward

    votes = len(polldata)

    Stockham = []
    DeGette = []
    Doane = []

    for row in polldata:
        if row[2] == "Charles Casper Stockham":     # will add to Stockham list
            Stockham.append(int(row[0]))    
        if row[2] == "Diana DeGette":   # will add to DeGette list
            DeGette.append(int(row[0]))
        if row [2] == "Raymon Anthony Doane":   # will add to Doane list
            Doane.append(int(row[0]))

    totalStockham = len(Stockham)
    totalDeGette = len(DeGette)
    totalDoane = len(Doane)

    percentStockham = round((totalStockham/votes)*100,3)
    percentDeGette = round((totalDeGette/votes)*100,3)
    percentDoane = round((totalDoane/votes)*100,3)

    winner = max([totalStockham,totalDeGette,totalDoane])
    
    if winner == totalStockham:
        message = "Winner: Charles Casper Stockham"
    elif winner == totalDeGette:
        message = "Winner: Diana DeGette"
    else:
        message = "Winner: Raymon Anthony Doane"

    print(f"Election Results")
    print(f"--------------------------------")
    print(f"Total Votes: {votes}")
    print(f"--------------------------------")
    print(f"Charles Casper Stockham: {percentStockham}% ({totalStockham})")
    print(f"Diana DeGette: {percentDeGette}% ({totalDeGette})")
    print(f"Raymon Anthony Doane: {percentDoane}% ({totalDoane})")
    print(f"--------------------------------")
    print(message)
    print(f"--------------------------------")

newFile = open("output.txt","w")
newFile.write(f"Election Results\n")
newFile.write(f"--------------------------------\n")
newFile.write(f"Total Votes: {votes}\n")
newFile.write(f"--------------------------------\n")
newFile.write(f"Charles Casper Stockham: {percentStockham}% ({totalStockham})\n")
newFile.write(f"Diana DeGette: {percentDeGette}% ({totalDeGette})\n")
newFile.write(f"Raymon Anthony Doane: {percentDoane}% ({totalDoane})\n")
newFile.write(f"--------------------------------\n")
newFile.write(f"{message} \n")
newFile.write(f"--------------------------------\n")