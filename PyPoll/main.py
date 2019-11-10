# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv
import operator

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


    i=0
    candidate_dict={}
    


    # Read each row of data after the header
    for row in csvreader:
        i = i+1
        row_candidate = row[2]

        
        if row_candidate in candidate_dict:
        	candidate_dict[row_candidate] += 1

        else:
        	candidate_dict[row_candidate]= 1


        #print(row[1])



print ("Election Results")
print ("----------------------------")

#The total number of votes cast
total_votes=i
print("Total Votes:",total_votes)
print ("----------------------------")

#A complete list of candidates who received votes

for key in candidate_dict.keys() :
    #print (key, ":", value/total_votes, "%(", value, ")")
    #print(key, ": ", candidate_dict[key]/total_votes*100, "%(", candidate_dict[key], ")")
    print(key, ": ", candidate_dict[key]/total_votes*100, "%(", candidate_dict[key],")")

#The percentage of votes each candidate won

#The total number of votes each candidate won


#print(max(candidate_dict.values()))
print("Winner is:")
print(max(candidate_dict, key=candidate_dict.get))

#zip and output



#The winner of the election based on popular vote.
#max(candidate_dict.items(), key=operator.itemgetter(1))[0]


summary = []
for key in candidate_dict.keys() :
  summary.append("{} : {} % ({})".format(key, candidate_dict[key]/total_votes*100, candidate_dict[key]))


text = (f"Election Results\n"
       f"--------------------\n"
       f"Total Votes: {total_votes}\n"
       f"--------------------\n"
       f"{summary[0]}\n"
       f"{summary[1]}\n"
       f"{summary[2]}\n"
       f"{summary[3]}\n"
       f"--------------------\n"
       f"Winner is : {max(candidate_dict, key=candidate_dict.get)}\n"
       f"---------------------\n")
with open('summary.txt', "w") as txt_file:
   txt_file.write(text)


#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------


