#Completing Part 1
import pandas #loading the pandas package to use data frames 

data = pandas.read_csv("wages.csv", header=0,sep=",") #loads the file

gender_yrsexp = data.iloc[:,0:2] #subsets data by selecting the first two columns 

uniquegender = gender_yrsexp.drop_duplicates()  #drops duplicates, like the unique function in unix 
uniquegender.shape   #displays shape of array 

sortgender = uniquegender.sort_values(["gender","yearsExperience"])

sortgender.to_csv("part1done.txt", sep=" ")

#Completing Part 2
import pandas
df=pandas.read_csv('wages.csv')
#df=wages.csv data

#Highest earner
highest_earner=df.nlargest(1,'wage')
#output is under highest_earner (male,5,11,39.808917197)

#Lowest earner
lowest_earner=df.nsmallest(1,'wage')
#Output is under lowest_earner (female,9,11,0.07655561)

#Number of females in the top 10
num_of_females=df[df['wage']>=df['wage'].nlargest(10).iloc[-1]]['gender'].eq('female').sum()
#Output is under num_of_females (=2)

#Completing Part 3
import pandas

#Define wages
wages=pandas.read_csv('wages.csv')

#Select for the people who didn't finish school(i.e. 12yrs of school)
education12=wages[wages.yearsSchool==12]

#Calculate the minimum wage for people with 12yrs of school
minimum12=min(education12.wage)

#Select for the people who did finish school(i.e. 16yrs of school)
education16=wages[wages.yearsSchool==16]

#Calculate the minimum wage for people with 16yrs of school
minimum16=min(education16.wage)

#Calculate the difference between the minimum wage for those who finished school vs. those who didn't
print(minimum16-minimum12)
#Difference is 4.0816223772