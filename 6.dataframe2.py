# data frame :  2 dimensional 
#    rows == observations / samples
#    columns == features/ attributes
#    each column of different
#    within column we expect the data to be in same data type
    
import pandas as pd
print(pd.__version__)

# to create data frame from an existing dict/map    

dict1 = {'names': ['ramesh','kalyan','ramu'], 
     'averages': [90,85,72]}
df1 = pd.DataFrame(data=dict1)
print(df1)
type(df1)

# --------from url ---------------

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')

# read from external location 
# can be excel/csv/ rdbms systems

traindata = pd.read_csv('e:/titanic/train.csv')
# -----------------

# quick look at data size and column types/names
# explore the dataframe
traindata.shape
traindata.info()
traindata.dtypes
traindata.columns
len(traindata)

titanic_train.head(5)
titanic_train.tail(5)
titanic_train.index

titanic_train.Sex.value_counts().head(0)
titanic_train.Sex.value_counts().count()
titanic_train.Sex.value_counts().max()
titanic_train.Sex.value_counts().min()


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
traindata.iloc[traindata.Sex == 'female', 3]   # through error
traindata.loc[traindata.Sex == 'female', 'Sex']

# conditional access and update missing values
traindata.loc[traindata['Age'].isnull() == True  , 'Age'] = traindata['Age'].mean()
traindata.loc[traindata['Embarked'].isnull() == True  , 'Embarked'] = 'S'

# create new column

# age / title
traindata['Title'] = 'Mr.'

#create title column from name

def extract_title(name):
     return name.split(',')[1].split('.')[0].strip()
 
titanic['Title'] = titanic['Name'].map(extract_title)

def convert_age(age):
    if(age >= 0 and age <= 10): 
        return 'Child'
    elif(age <= 25): 
        return 'Young'
    elif(age <= 50): 
        return 'Middle'
    else: 
        return 'Old'
titanic['Age1'] = titanic['Age'].map(convert_age)


traindata['Title'] =

# drop existing column
traindata1 = traindata.drop(['Survived'], axis=1, inplace=False)
traindata1.shape

# quick statistics:

traindata.


# concat 
train1 = pd.read_csv('e:/titanic/titanic_data891_copy1.csv')
train2 = pd.read_csv('e:/titanic/titanic_data418_copy2.csv')

train3 = pd.concat([train1,train2])
train3.shape
train3.info()
train3.head(5)

# -------------------------------------------------------------------
# -------------------------------------------------------------------------
# group by

titanic_train.groupby(by=['Sex']).count()

# -------------------------------------------------------------------------
filters

# delete the duplicates 
titanic1 = titanic_train.drop_duplicates(['Sex'])

# select only the 
titanic2 = traindata[(traindata.Sex == 'male') & (traindata.Age > 40)]

# select only the 
titanic3 = titanic_train[['Sex','Age']]
len(titanic2)

# sort the values 
traindata.sort_values(by = "Age", ascending = False)



# ----------- thru numpy arrays 
import numpy as np
df2 = pd.DataFrame(np.random.randn(10, 5))
df3 = pd.DataFrame(np.random.randn(10, 5),
                 columns=['a', 'b', 'c', 'd', 'e'])

# ------------------------------