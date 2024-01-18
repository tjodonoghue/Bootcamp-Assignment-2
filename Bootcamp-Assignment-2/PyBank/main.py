import pandas as pd 

#import the csv file to be referenced throughout the code
path = r"C:\Users\Gamer PC\Desktop\Git\Bootcamp-Assignment-2\PyBank\budget_data.csv"
df = pd.read_csv(path)
df

#find total number of months 
num_months=len(df["Date"])
print(num_months)

#Find the net total profit and loses, expressed here as "pnl"
pnl = df["Profit/Losses"].sum()
print(pnl)
df["Change"] = df["Profit/Losses"].diff()
df

#Total change, and average change. First total change was found (expressed as "change"), then was divided by 85 to find average
change = df["Change"].sum()
average_change = change/85
print(average_change)

#Find greatest increase/decrease in profit, expressed as "min_change" and "max_change"
max_change = df["Change"].max()
print(min_change)
print(max_change)

#To show date and amount, we find the data point for each within the series
df_min_change = df[df["Change"] == min_change]
df_min_change

df_max_change = df[df["Change"] == max_change]
df_max_change

#Then we convert the data point into readable text

min_row_values = df_min_change.iloc[0].astype(str)
min_change_date = min_row_values["Date"]
min_change_value = min_row_values['Change']
print(min_change_date)
print(min_change_value)
max_row_values = df_max_change.iloc[0].astype(str)
max_change_date = max_row_values["Date"]
max_change_value = max_row_values['Change']
print(max_change_date)
print(max_change_value)


#Finally, we create the financial report using an f-string.
report_text = f"""Financial Analysis
----------------------------
Total Months: {num_months}
Total: ${pnl}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {max_change_date} (${max_change_value})
Greatest Decrease in Profits: {min_change_date} (${min_change_value})
"""

with open("financial_analysis.txt", "w") as file:
    file.write(report_text)

print(report_text)
