#program:npv

#NPV Calculator for ISE321

#TODO add AW calculator
#TODO add IRR


#Variable dictionary
#c --> Cost per year
#d --> Discount Rate
#f --> discount factor
#g --> Gain per year
#i --> Year Counter
#j --> NPV Summation
#p --> profit 
#
#




#Discount Rate
d = input("DR as int: ")
#d = 15


#Upfront Costs
u = input ("Upfront costs:  ")
#u = 30000

#Total amount of time to run in years
t = int(input("Time in years: "))
#t = 20

#Total cost per year
c = float(input("Cost per year: "))
#c = 18200

#Total Gain per year
g = float(input("Gain per year: "))
#g = 24000

#Initialize counter variables

#Year counter
i = 0

#NPV Sum variable
j = 0


#Set Discount rate to decimal
d = d/100

#Calculations for first year
if i == 0:
	#Calculate discount factor
	f = (1+d)**(0+-i)

	#Calculate Profit
	p = 0 +-u

	#Calculate NPV
	n = f * p

	#Sum NPV to itself 
	j = j + n

	#Go to next year
	i = i + 1


#Calculations for all remaining years 
while i <= t:
		
		#Discount factor calculation
		f = (1+d)**(0+-i)

		#Profit calculation
		p = g + - c

		#NPV Calculation
		n = p * f

		#NPV Summation
		j = j + n

		#print(i,'\t',round(f,4),'\t', round(p,2), '\t', round(n,2))

		#Go to next year
		i = i + 1


print ("Total NPV: " + str(round(j,2)))

