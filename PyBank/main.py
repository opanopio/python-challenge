import os
import csv

csvpath = os.path.join("..//PyBank//Resources//budget_data.csv")

with open(csvpath) as pybankfile:

    csvreader = csv.reader(pybankfile, delimiter=',')
    
    #List to store data
    Month=[]
    Average_Change=[]
    AverageX=[]
    header = next(csvreader)
    total_profit= 0
    total_months= 0
    
    #For Loop Start
    for pl in csvreader:

        #Total Months
        total_months += 1

        #Total Profit/Losses
        total_profit += int(pl[1])
        
        Month.append(pl[0])
        Average_Change.append(int(pl[1]))

    #Average Change
    for i in range(1, len(Average_Change)):
        AverageX.append(Average_Change[i]-Average_Change[i-1])
        total_averagec=round(sum(AverageX)/len(AverageX),2)

        #Greatest Increase/Decrease in Profits:
        total_GIn=AverageX.index(max(AverageX))+1
        total_GDe=AverageX.index(min(AverageX))+1

    #Report Layout
    print("Financial Analysis")

    print("-------------------")

    print(f"Total Months: {total_months}")

    print(f"Total: ${total_profit}")

    print(f"Average Change: ${total_averagec}")

    print(f"Greatest Increase in Profits: {Month[total_GIn]} ${max(AverageX)}")
        
    print(f"Greatest Decrease in Profits: {Month[total_GDe]} ${min(AverageX)}")