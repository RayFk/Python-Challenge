# import csv modules
import csv
# import operating system modules
import os

# define csv_path
csv_path = os.path.join("Resources","budget_data.csv")

# define output text file
txt_path = os.path.join("analysis","budget_analysis.txt")

# opening csv file and storing as csv_file
with open(csv_path,newline= "") as csv_file:

    # use csv_reader to read file content
    csv_reader = csv.reader(csv_file,delimiter=",")

    # print csv_reader (contents of csv file)
    # print(csv_reader)
    
    # define and store header
    csv_header = next(csv_reader)

    # print header
    print(csv_header) 

    # define months, revenue, revenue change, and monthly change
    months = [] 
    revenue = []
    revenue_change = []
    monthly_change = []

    # iterate over all rows in csv_file and add contents to list
    for row in csv_reader:
        # keep track of months and revenue 
        months.append(row[0])
        revenue.append(row[1])
    
    # verify length of months
    # print(len(months))

    # calculate total sum of Profit/Losses (using mapfunction to pass int function to all elements inside of revenue) 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    # test_revenue = sum(revenue)

    # print total revenue
    # print(total_revenue)
    # print(test_revenue)

    # calculate the average of Profit/Losses
    i = 0  # create counter
    
    # go through every row in the csv file (length of months is 86)
    for i in range(len(months) - 1):
        
        # define current Profit/Losses 
        profit_loss = int(revenue[i + 1]) - int(revenue[i]) 
        
        # add Profit/Losses to revenue_change list
        revenue_change.append(profit_loss)
    
    # calculate average of changes 
    average = (sum(revenue_change)) / len(months)

    # find max increase in Profits over entire period
    profit_increase = max(revenue_change)
    k = revenue_change.index(profit_increase)
    month_increase = months[k + 1]

    # find max decrease in Losses over entire period
    profit_decrease = min(revenue_change)
    j = revenue_change.index(profit_decrease)
    month_decrease = months[j + 1]

    # print values on terminal
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: {}".format(len(months)))
    print("Total: {}".format(total_revenue))
    print("Average Change: {}".format(round(average, 2)))
    print("Greatest Increase in Profits: {0} {1}".format(month_increase, profit_increase))
    print("Greatest Decrease in Profits: {0} {1}".format(month_decrease, profit_decrease))

# writing analysis to text file
with open(txt_path, "w") as txt_file:
    txt_file.write("Financial Analysis \n")
    txt_file.write("---------------------------- \n")
    txt_file.write("Total Months: {} \n".format(len(months)))
    txt_file.write("Total: {} \n".format(total_revenue))
    txt_file.write("Average Change: {} \n".format(round(average, 2)))
    txt_file.write("Greatest Increase in Profits: {0} {1} \n".format(month_increase, profit_increase))
    txt_file.write("Greatest Decrease in Profits: {0} {1}".format(month_decrease, profit_decrease))