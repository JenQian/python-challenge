# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")



    i=0
    total=0
    greatest_increase=0.0
    greatest_decrease=0.0
    greatest_increase_date=""
    greatest_decrease_date=""
    previous_value=0.0
    total_change=0.0
    diff=0.0


    # Read each row of data after the header
    for row in csvreader:
        i = i+1
       	record = float(row[1])
        total = total + record
        

        diff = record - previous_value
        if i == 1:
        	diff=0


        total_change = total_change + diff

        
       

        if diff >= greatest_increase:
            greatest_increase = diff
            greatest_increase_date = row[0]

        if diff < greatest_decrease:
            greatest_decrease = diff
            greatest_decrease_date = row[0]


        previous_value=record


text = (f"Financial Analysis\n"
		f"----------------------------\n"
		f"Total Months:{i}\n"
		f"Total:${total}\n"
		f"Average Change:{ total_change/(i-1)}\n"
		f"Greatest Increase in Profits:{greatest_increase_date, greatest_increase}\n"
		f"Greatest Decrease in Profits:{greatest_decrease_date, greatest_decrease}\n"
	)

with open('summary.txt', "w") as txt_file:
   txt_file.write(text)


    
    
  

print ("Financial Analysis")
print ("----------------------------")


#The total number of months included in the dataset

print("Total Months:",i)

#The net total amount of "Profit/Losses" over the entire period
print("Total:$", total)

#The average of the changes in "Profit/Losses" over the entire period
print("Average Change:", total_change/(i-1))

#The greatest increase in profits (date and amount) over the entire period
#print(csvreader[-1])
print("Greatest Increase in Profits:", greatest_increase_date, greatest_increase)
#The greatest decrease in losses (date and amount) over the entire period
print("Greatest Decrease in Profits:", greatest_decrease_date, greatest_decrease)