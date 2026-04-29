### TIP CALCULATOR ###

print("Welcome to the tip calculator")   #welcome message

total_bill = int(input("What is the total bill?"))  #total bill
tip_percent = int(input("How much would you like to tip (%)?")) # percent of bill to be tipped 
group_size = int(input(" How many people are paying?"))  #size of group that's dining

bill_per_person = round((total_bill * (1 + (tip_percent / 100))) / group_size ,2 ) # calculation of total bill and rounding to 2 decimal points (or cents)

print(f"The total bill per person will be {bill_per_person} for the tip percentage of {tip_percent}% for a group of {group_size} people")
