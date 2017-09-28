import pandas
pandas.read_csv('wages.csv')

#Select for the people who didn't finish school(i.e. 12yrs of school)
education12=wages[wages.yearSchool==12]

#Calculate the minimum wage for people with 12yrs of school
minimum12=min(education12.wage)

#Select for the people who did finish school(i.e. 16yrs of school)
education16=wages[wages.yearSchool==16]

#Calculate the minimum wage for people with 16yrs of school
minimum16=min(education16.wage)

#Calculate the difference between the minimum wage for those who finished school vs. those who didn't
print(minimum16-minimum12)