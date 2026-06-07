import pandas as pd

# Load dataset
df = pd.read_excel("Car_Data_Analysis.xlsx")

# Basic Information
print("Dataset Information")
print(df.info())

print("\nFirst 5 Rows")
print(df.head())

# Statistics
print("\nSummary Statistics")
print(df.describe())

# Average Price
print("\nAverage Price:")
print(df["Price"].mean())

# Median Price
print("\nMedian Price:")
print(df["Price"].median())

# Average Mileage
print("\nAverage Mileage:")
print(df["Mileage"].mean())

# Brand Count
print("\nCars by Brand")
print(df["Brand"].value_counts())

# Most Expensive Car
print("\nMost Expensive Car")
print(df.loc[df["Price"].idxmax()])

# Least Expensive Car
print("\nLeast Expensive Car")
print(df.loc[df["Price"].idxmin()])