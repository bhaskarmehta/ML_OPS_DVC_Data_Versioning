import pandas as pd
import os


#Create a Simple DataFrame with column names

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)


#Add a new row in the DataFrame for v2
new_row = {'Name': 'David', 'Age': 28, 'City': 'San Francisco'}
df.loc[len(df.index)] = new_row # Add the new row to the DataFrame . len(df.index) gives the length of the DataFrame
                                # df.loc[] will assign the new_row to the len(df.index) location

# Insure the "data" directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# Define a file path within the "data" directory
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file in the "data" directory, including clomn names
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")