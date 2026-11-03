import pandas as pd

# 1. Define your data using a dictionary
data = {
    "Product": ["Laptop", "Smartphone", "Tablet", "Headphones"],
    "Price": [999.99, 599.49, 349.99, 89.99],
    "Units_Sold": [120, 250, 180, 410],
    "In_Stock": [True, True, False, True]
}

# 2. Create the DataFrame
df = pd.DataFrame(data)

# 3. Display the full DataFrame
print("--- Full DataFrame ---")
print(df)

df.to_csv("df.csv")