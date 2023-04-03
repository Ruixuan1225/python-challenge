import pandas as pd

budget_data = pd.read_csv('./python-challenge/PyBank/Resources/budget_data.csv')

total_months = len(budget_data)

i = 0
total = 0
total_changes = 0
previous = budget_data.loc[0,'Profit/Losses']
greatest_decrease = 0
greatest_increase = 0
greatest_decrease_month = 0
greatest_increase_month = 0

while i <= total_months - 1:
    total = budget_data.loc[i,'Profit/Losses'] + total
    changes = budget_data.loc[i,'Profit/Losses'] - previous
    previous = budget_data.loc[i,'Profit/Losses']
    total_changes = changes + total_changes
    if changes < 0 and changes < greatest_decrease:
        greatest_decrease = changes
        greatest_decrease_month = i
    if changes > 0 and changes > greatest_increase:
        greatest_increase = changes
        greatest_increase_month = i
    i = i + 1

average_change = round(total_changes/(total_months-1),2)    
# print(total_months)
# print(total)
# print(total_changes/(total_months-1))
# print(greatest_increase)
# print(greatest_decrease)

#specify path for export
path = r'./python-challenge/PyBank/analysis/budget_analysis.txt'
#export to text file
with open(path, 'a') as f:
    f.truncate(0)
    f.write('Financial Analysis\n')
    f.write('----------------------------\n')
    f.write('Total Months: ' + str(total_months) + '\n')
    f.write('Total: ' + str(total) + '\n')
    f.write('Average Change: ' + str(average_change) + '\n')
    f.write('Greatesr Increase in Profits: ' + budget_data.loc[greatest_increase_month,'Date'] + '($' + str(greatest_increase) + ')\n')
    f.write('Greatesr Decrease in Profits: ' + budget_data.loc[greatest_decrease_month,'Date'] + '($' + str(greatest_decrease) + ')\n')