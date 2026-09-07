import pandas as pd

filename = input("Enter CSV file name: ")

data = pd.read_csv(filename)

print("\nDataset:")
print(data)

print("\nRows and Columns:")
print(data.shape)

print("\nData Types:")
print(data.dtypes)

print("\nSummary:")
print(data.describe())

column = input("\nEnter column name to filter: ")
value = input("Enter value: ")

filtered_data = data[data[column].astype(str) == value]

print("\nFiltered Data:")
print(filtered_data)

filtered_data.to_csv("filtered_data.csv", index=False)

print("\nFiltered data saved successfully!")
