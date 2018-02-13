import os
import csv
month = []#create empty list for month
revenue =[]#crete empty list for revenue
changeinrevenue =[]#create empty list for change in revenue
csvpath = os.path.join("budget_data_1.csv")#declare path to csv file
with open(csvpath, newline='', encoding='utf-8') as csvfile: #open and read csvfile
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)#skip the first row in the csvfile which we know contains headers
    for row in csvreader:#loop through each row in the csv and add the revenue to the revenue list and date to the month list
        revenue.append(float(row[1]))
        month.append(row[0])
for i in range (1,len(revenue)):#loop through each row and....
        changeinrevenue.append(-revenue[i-1]+revenue[i])#...obtain chain in revenue by taking the negative value of the row above and adding it to the current rows revenue
        avgdeltarev = sum(changeinrevenue)/len(changeinrevenue)#obtain average chain in revenue by summing all change in revenue and dividing by the number of deltas we have
        maxdeltarev = max(changeinrevenue)#obtain the greatest positive value in the changeinrevenue list
        maxdeltadate = str(month[changeinrevenue.index(max(changeinrevenue))])#get the date that corresponds with the greatest positive value in changeinrevenue list
        mindeltarev = min(changeinrevenue)#same as above but for most negative value
        mindeltadate = str(month[changeinrevenue.index(min(changeinrevenue))])
#print out summary
Summary = (
        f"\nData from {csvpath}\n"
        f"..............................\n"
        f"Total Months: {len(month)}.\n"
        f"Total Revenue: ${sum(revenue)}.\n"
        f"Average Change in Revenue: {avgdeltarev}\n"
        f"Greatest increase in revenue is ${maxdeltarev} during {maxdeltadate}.\n"
        f"Greatest decrease in revenue is ${mindeltarev} during {mindeltadate}.\n"
)
print(Summary)
#do the same for second fule
month = []#create empty list for month
revenue =[]#crete empty list for revenue
changeinrevenue =[]#create empty list for change in revenue
csvpath = os.path.join("budget_data_2.csv")#declare path to csv file
with open(csvpath, newline='', encoding='utf-8') as csvfile: #open and read csvfile
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)#skip the first row in the csvfile which we know contains headers
    for row in csvreader:#loop through each row in the csv and add the revenue to the revenue list and date to the month list
        revenue.append(float(row[1]))
        month.append(row[0])
for i in range (1,len(revenue)):#loop through each row and....
        changeinrevenue.append(-revenue[i-1]+revenue[i])#...obtain chain in revenue by taking the negative value of the row above and adding it to the current rows revenue
        avgdeltarev = sum(changeinrevenue)/len(changeinrevenue)#obtain average chain in revenue by summing all change in revenue and dividing by the number of deltas we have
        maxdeltarev = max(changeinrevenue)#obtain the greatest positive value in the changeinrevenue list
        maxdeltadate = str(month[changeinrevenue.index(max(changeinrevenue))])#get the date that corresponds with the greatest positive value in changeinrevenue list
        mindeltarev = min(changeinrevenue)#same as above but for most negative value
        mindeltadate = str(month[changeinrevenue.index(min(changeinrevenue))])
#print out summary
Summary = (
        f"\nData from {csvpath}\n"
        f"..............................\n"
        f"Total Months: {len(month)}.\n"
        f"Total Revenue: ${sum(revenue)}.\n"
        f"Average Change in Revenue: {avgdeltarev}\n"
        f"Greatest increase in revenue is ${maxdeltarev} during {maxdeltadate}.\n"
        f"Greatest decrease in revenue is ${mindeltarev} during {mindeltadate}.\n"
)
print(Summary)