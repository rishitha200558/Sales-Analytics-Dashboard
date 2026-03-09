import pandas as pd

data = pd.read_csv("data/train.csv")

print("First 5 rows:")
print(data.head())

print("\nDataset Information:")
print(data.info())

print("\nSummary Statistics:")
print(data.describe())

print("\nMissing Values:")
print(data.isnull().sum())
import matplotlib.pyplot as plt

data['Sales'].hist()

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()
top_products = data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)

print("\nTop 10 Products:")
print(top_products.head(10))