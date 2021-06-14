import pandas as pd
import string

# User Inputs
csv_path = 'replace/with/path/to/csv/file.csv'
col_to_clean = 'Column Name' #assumes file has header rows
new_csv_name = 'CleanedCol' + col_to_clean + '.csv'

#Remaining Code
data = pd.read_csv(csv_path) #reads in CSV

col = list(data[col_to_clean]) #identifies column to be cleaned

charList = list(string.printable) #List of 'acceptable' characters, can be customized to suit needs

newCol = list() #creates empty list corresponding to the cleaned column

for vIndex in range(0,len(col)):
    value = col[vIndex] # takes first row
    valueList = list(str(value)) #converts row into a list of strings
    newValueList = list() #creates empty list for the row's cleaned content
    for cIndex in range(0,len(valueList)):
        char = valueList[cIndex] #takes each individual character in a given row
        if (char not in charList) or (char == ','):
            newValueList.append(' ') #if character is not in the charList or a comma, replaces with a space
        else:
            newValueList.append(char) #if character is not in either of the two categories above, replaces it with the same character as before
    newValue="".join(newValueList) #joins together all characters just evaluated (as its previous value or new value
    newCol.append(newValue) #appends to cleaned column list

df = pd.DataFrame(newCol) #creates pandas data frame out of cleaned column list
df.to_csv(new_csv_name,index=False,header=False) #creates csv with the new cleaned column to copy and paste into data
