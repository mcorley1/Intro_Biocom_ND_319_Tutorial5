#completing exercise5
import pandas #loading the pandas package to use data frames 

data = pandas.read_csv("wages.csv", header=0,sep=",") #loads the file

#completing part1 
gender_yrsexp = data.iloc[:,0:2] #subsets data by selecting the first two columns 

uniquegender = gender_yrsexp.drop_duplicates()  #drops duplicates, like the unique function in unix 
uniquegender.shape   #displays shape of array 

sortgender = uniquegender.sort_values(["gender","yearsExperience"])

sortgender.to_csv("part1done.txt", sep=" ")