# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

"""
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average  Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
"""

import os
import csv

def average(numbers_list):    
    total = 0.0    
    for number in numbers_list:    
        total += number    
    avg = total / len(numbers_list)     
    return avg  


# Path to collect data from the Resources folder
input_path = os.path.join('', 'Resources', 'budget_data.csv')

month_count = 0
net_profitloss = 0
profitloss_delta = []
max_increase = 0
min_loss = 0
max_record = {}
min_record = {}
current_value = 0
previous_value = 0

# Read in the CSV file
with open(input_path, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:    
        # print(row)
        current_value = int(row[1])
        
        # summarize net_profitloss
        net_profitloss = net_profitloss + current_value
        
        # calculate profitloss_delta
        if month_count > 0 :
            # start on index [1] of data set and find the difference betwen the current value and the previous value
            delta = current_value - previous_value
            
            # set previous value to current value
            previous_value = current_value        
                        
            # add profitloss_delta to collection
            profitloss_delta.append(delta)  
            
            # find/set max value
            if current_value > max_increase:
                max_increase = current_value
                # add row info to max_record
                max_record = {
                    "Date": row[0],
                    "Amount": row[1]
                    }   
            
            # find/set min value
            if current_value < min_loss:
                min_loss = current_value
                
                # add row info to min_record
                min_record = {
                    "Date": row[0],
                    "Amount": row[1]
                    }   
                                
        else:             
            # skip first month and set previous value to current value
            previous_value = current_value
            
            profitloss_delta.append(0)
            
        # increment mounth_count
        month_count += 1
        
# calculate profitloss_delta average
profitloss_delta_avg = round(average(profitloss_delta),2)
        
print(f'Total Months: {month_count}')        
print(f'Net Profit/Loss: {net_profitloss}') 
print(f'Average Change: {profitloss_delta_avg}')
print(f'Greatest Gain: {max_increase}')
print(f'Greatest Loss: {min_loss}')












       