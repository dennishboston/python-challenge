import os
import csv
import numpy as np
import pandas as pd



fileName = "budget_data_1.csv"



Pybank_csv = os.path.join(fileName)




total_m = 0
total_r = 0
prev_month_rev = 0
rev_change = 0
rev_change_list = [] 
avg_rev = 0
greatest_increase =["",0] 
greatest_decrease =["",np.infty] 



with open(Pybank_csv, newline="") as csvfile:
    csv = csv.DictReader(csvfile, delimiter=",")
    for row in csv:
        
        total_m = total_m + 1
        total_r = total_r + int(row['Revenue'])
        
        #revenue change
        rev_change = int(row["Revenue"]) - prev_month_rev 
        prev_month_rev = int(row["Revenue"]) 
        rev_change_list = rev_change_list + [rev_change] 
        
        #biggest increase
        if (rev_change > greatest_increase[1]):
            greatest_increase[1] = rev_change 
            greatest_increase[0] = row['Date']
 
        #biggest decrease
        if (rev_change < greatest_decrease[1]):
            rev_change_list[1] = rev_change 
            greatest_decrease[0] = row['Date'] 
       
#Avg Revenue Change
avg_change_per_m = sum(rev_change_list) / len(rev_change_list)

#print
print("\nFinancial Analysis \n--------------------------------------------------")
print("Total Months: " + str(total_m))
print("Total Revenue:  $" + str(total_r))
print("Average Monthly Change: " + str(avg_change_per_m)) 
print("Greatest Monthly Increase: " + str(greatest_increase[0]) + "  $(" + str(greatest_increase[1]) + ")")   
print("Greatest Monthly Decrease: " + str(greatest_decrease[0]) + "  $(" + str(greatest_decrease[1]) + ")")


