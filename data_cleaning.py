# Import Modules
import pandas as pd
import csv

# Dataframe
df = pd.read_csv("final_data.csv")
print("Original Data --> (Rows, Columns) =", df.shape)

# Removing Many Unneccessary Columns
del df["Luminosity"]
del df["Star_name"]
del df["Mass"]
del df["Distance"]
del df["Radius"]


print("After Removing Many Columns --> (Rows, Columns) =", df.shape)
print(df.head())

df = df.rename({
    "Star_name.1" : "Star_name",
    "Distance.1" : "Distance",
    "Mass.1" : "Mass",
    "Radius.1" : "Radius"

}, axis='columns')


df.to_csv("final_cleaned.csv")