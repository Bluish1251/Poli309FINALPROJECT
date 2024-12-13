import pandas as pd

# Load the dataset
data = pd.read_csv(r'C:\Users\Cm6of\Desktop\temp\pollresults.csv')

# Display the first few rows of the dataset
print(data.head())

# Check the unique values in the 'issues' column
print(data['issues'].unique())
