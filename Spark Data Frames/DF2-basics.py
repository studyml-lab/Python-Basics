
# --------------------
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# alternative approach ------------------------
from pyspark import SparkContext
from pyspark.sql import SQLContext
sc = SparkContext('local')
spark = SQLContext(sc)
# -----------------------------


print(spark)

# Create data frame by using data

#fname,lname, age
#Johh, Smith, 47
#James, Smith, 27
#Keith, Maren, 38
# ------------------------------
data = [
        ('Johh', 'Smith', 47),
        ('James', 'Smith', 27),
        ('Keith', 'Maren', 38)      
        ]
header1 = ['fname','lname','age']
df1 = spark.createDataFrame(data,header1)
df1.show(n=2)
df1.first()
df1.count()
df1.printSchema()
df11.show()

df1.write.csv('c:/test1')

# read data from csv files to dataframe
df2 = spark.read.csv('E:/kaggle/titanic/train_kaggle.csv',header=True)
df2.count()
df2.show()
df2.show(n=30)
df2.cache()
df2.count()
df2.describe().show()
df2.
df1.write.csv('e:/test1.csv')

# ---------------------------------------

df3 = df2.select('Pclass','SibSp','Survived','Fare')
df3.show()

# --------------------------------------------

#df4 = df2.filter(df2.Age > 40).select('Pclass','SibSp','Survived')
#df4.show()
#df4.count()
#df4.describe().show()
#df5 = df2.drop('SibSP')

# --------------------------------------------
#df2.describe().show()
#df3.printSchema()

-----------------------------------------

df3 = df3.select(df3.Pclass.cast('double'),df3.SibSp.cast('double'),df3.Survived.cast('double'),df3.Fare.cast('double'))
df3.show()
df3.printSchema()

# Vector assembler

from pyspark.ml.feature import VectorAssembler
df3 = VectorAssembler(inputCols=['Pclass','SibSp','Fare'],outputCol='Features').transform(df3)

df3.show()
#
# 1 choose approach
from pyspark.ml.classification import DecisionTreeClassifier
dt1 = DecisionTreeClassifier(featuresCol='Features',labelCol='Survived',maxDepth=10,impurity='entropy')

# 2 learning process - created a model
model1 = dt1.fit(df3)
model1.depth

# 3 get predictions


df5 = spark.read.csv('E:/kaggle/titanic/test.csv',header=True).select('PassengerId','Pclass','SibSp')
df5
df5 = df5.select(df5.Pclass.cast('double'),df5.SibSp.cast('double'),df5.PassengerId)
df5 = VectorAssembler(inputCols=['Pclass','SibSp'],outputCol='Features').transform(df5)
df20 = model1.transform(df5)


df20.show()

df20.select('PassengerId','prediction').write.csv('c:/test3.csv')





























