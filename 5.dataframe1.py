# data frame :  2 dimensional 
#    rows == observations / samples
#    columns == features/ attributes
#    each column of different
#    within column we expect the data to be in on simple type
    
import pandas as pd
print(pd.__version__)

# to create data frame from an existing dict/map    

dict1 = {'names': ['ramesh','kalyan','ramu'], 
     'averages': [90,85,72]}
df1 = pd.DataFrame(data=dict1)
print(df1)
type(df1)

# read from external location 
# can be excel/csv/ rdbms systems

traindata = pd.read_csv('e:/titanic/train.csv')
# -----------------

# quick look at data size and column types/names
traindata.shape
traindata.info()


#access column/columns of a dataframe
traindata['Sex']

traindata.Name
traindata.Sex
traindata[['Name','Survived']]
traindata[['Name','Embarked','Pclass']]
traindata['Pclass'] = 2

X_train = traindata[['Embarked','Pclass','Sex']]
X_train.shape  # ----> (891,4)

traindata[['Pclass']].info()


#access rows of a data frame
traindata.iloc[0]
traindata.iloc[0:3]
traindata.iloc[885:891]
traindata.tail(6)
traindata.head(6)

#access both rows and columns of a dataframe
traindata.iloc[0:3,3]
traindata.iloc[0:4,0:3]
traindata.loc[0:3,'Name']

#conditional access of dataframe
traindata.iloc[traindata.Sex == 'female', 3]
traindata.loc[traindata.Sex == 'female', 'Sex']



# ----------- thru numpy arrays 
import numpy as np
df2 = pd.DataFrame(np.random.randn(10, 5))
df3 = DataFrame(np.random.randn(10, 5),
                 columns=['a', 'b', 'c', 'd', 'e'])

# ------------------------------