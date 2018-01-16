
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



# read data from csv files to dataframe
df2 = spark.read.csv('E:/kaggle/titanic/train_kaggle.csv',header=True)
df2.count()
df2.show()
df2.show(n=30)
df2.cache()
df2.count()
df1.write.csv('e:/test1.csv')

# ---------------------------------------

df3 = df2.select('Pclass','SibSp','Survived')
df3.show()

# --------------------------------------------

df4 = df2.filter(df2.Age > 40).select('Pclass','SibSp','Survived')
df4.show()
df4.count()
df4.describe().show()
df5 = df2.drop('SibSP')

