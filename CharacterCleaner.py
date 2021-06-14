import pandas as pd
import string

data = pd.read_csv('train_sentiment_cleaned.csv')

#col = list(data['Name'])
col = list(data['Description'])

charList = list(string.printable)

newCol = list()

for vIndex in range(0,len(col)):
    value = col[vIndex]
    valueList = list(str(value))
    newValueList = list()
    for cIndex in range(0,len(valueList)):
        char = valueList[cIndex]
        if (char not in charList) or (char == ','):
            newValueList.append(' ')
        else:
            newValueList.append(char)
    newValue="".join(newValueList)
    newCol.append(newValue)

df = pd.DataFrame(newCol)
df.to_csv('CharRemoveDesc.csv',index=False,header=False)
