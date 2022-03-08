import pandas as pd
from collections import Counter

fileName = 'filename.txt'

with open(fileName) as f:
    lines = f.readlines()

lines = [word.strip('\n') for word in lines] #Remove new line character
df = pd.DataFrame.from_dict(dict(Counter(lines)), orient='index') #Creates a df with each word followed by its count
df2 = df.sort_values(0, ascending=False) #sorts based on the number of appearances
df2.to_csv('listcount.csv') #writes to csv file
