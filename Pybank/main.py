
#   Pypoll - budget analysis

#   import the os and the csv modules
import os
import csv

#   set path to input and output files
file_to_analyse = os.path.join("Resources", "budget_data.csv")
analysis_file_to_output = os.path.join("analysis", "budget_analysis.txt")

#   set the delimiter used in the budget file
with open(file_to_analyse) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

#   read the header row
    csv_header = next(csv_reader)

#   declare counters and summary variables
    line_count = 0
    no_of_months = 0
    net_profit_loss = 0
    profit_change = 0
    net_profit_change = 0
    current_month = ''
    current_month_profit = 0
    previous_month = ''
    previous_month_profit = 0
    largest_profit_change = 0
    largest_profit_changemonth = ''
    smallest_profit_change = 0
    smallest_profit_change_month = ''

#   process each row after the first month's row and capture month and profit
    for row in csv_reader:
        line_count = line_count + 1
        current_month = (row[0])
        current_month_profit = int(row[1])

#   calculate net_profit_loss
        no_of_months = no_of_months + 1 
        net_profit_loss = net_profit_loss + current_month_profit
        
#  calculate profit change from current month to previous month
        if line_count > 1:
            current_month_profit = int(row[1])
            profit_change = current_month_profit - previous_month_profit
            net_profit_change = net_profit_change + profit_change
        previous_month_profit = current_month_profit

#   calculate largest increase in profit and the month when it occurred
        if profit_change > largest_profit_change:
            largest_profit_change = profit_change 
            largest_profit_month = current_month

#   calculate largest decrease in profit and the month when it occurred
        if profit_change  < smallest_profit_change:
            smallest_profit_change = profit_change
            smallest_profit_month = current_month
                
#   calculate the average change in profits
average_change_in_profit = net_profit_change / (no_of_months - 1)

#   print the financial analysis to the terminal and write it to the output CSV file
output = (
    f'Financial Analysis \n'
    f'------------------------- \n'
    f'Total Months: {no_of_months} \n'
    f'Total:  ${net_profit_loss} \n'
    f'Average   Change: ${average_change_in_profit:.2f} \n'
    f'Greatest Increase in Profits :  {largest_profit_month}  (${largest_profit_change}) \n'
    f'Greatest Decrease in Profits :  {smallest_profit_month} (${smallest_profit_change}) \n')
print (output)

with open(analysis_file_to_output, "w") as txt_file:
    txt_file.write(output)
