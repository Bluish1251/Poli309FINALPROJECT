import pandas as pd
#FOR TESTING 

data = pd.read_csv(r'C:\Users\Cm6of\Desktop\temp\pollresults.csv')
print(data.head())
print(data['issues'].unique())
