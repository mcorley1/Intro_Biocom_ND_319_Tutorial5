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