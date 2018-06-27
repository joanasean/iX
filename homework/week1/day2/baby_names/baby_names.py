# -*- coding: utf-8 -*-
"""
In this example we are going to build an application that reads the most popular names
in the US, taken from the Social Security Administration's site:

https://www.ssa.gov/oact/babynames/

This application will have the following functionalities:

- It will accept a name as an argument
- It will read a list of files (located in the folder data). Each file contains the
most popular baby names for boys and girls for a certain year (the year is in the filename)
# - For the name provided as an argument, print out how many years it's been among the most popular among boys and girls
# """

# path = '/Users/joanasean/Desktop/Data_Science/iX/homework/week1/day2/data/'
# import glob
# import os 

# print (glob.glob ('Desktop/Data_Science/iX/homework/week1/day2/data*.txt'))

# filenames = sorted(glob.glob ('data*.txt'))
# filenames = filenames[:]

# for f in filenames: 

year = 1900
mostnames = []
# counting = []
from collections import Counter 


while year <= 2017: 
	filename = "data/names_" + str(year)+ ".txt"
	reading = (open (filename, 'r')).readline().split("|")
	#print (reading)
	mostnames.append(reading[1]) 
	mostnames.append(reading[2].strip('\n'))
	year += 1


print (Counter(mostnames))



	


# for i in range(0,len(popularguys)):
# 	set(zip(mostnamesguys[i],popularguys[i]))







	

	# mostnames.append(reading)





