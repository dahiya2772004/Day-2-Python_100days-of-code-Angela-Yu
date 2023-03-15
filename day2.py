print("welcome to split bill calculator") #title
bill=float(input("what was the total bill? $")) #input for bill
tip=int(input("How much tip would you like to give? 10, 12 or 15?")) # asking user for tip percentage
people = int(input("How many people to split bill with?")) # asking user for no. of people
billwithtip=tip/100 *bill+bill.      #calculating total bill with tip
print(round(billwithtip/people,2)) #displaying final bill per person