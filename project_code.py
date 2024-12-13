# Connor Morris Poli 309 Pt2 Proj Code
# Heat map for poll results for my essay

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os.path

DATASET = "pollresults.csv"

# Load the dataset
data = pd.read_csv(os.path.join(
    os.path.dirname(__file__),
    DATASET
))

# Data Cleaning and Filtering
education_map = {
    1: "Less than High School",
    2: "High School Graduate",
    3: "Some College",
    4: "Associate Degree",
    5: "Bachelor's Degree",
    6: "Master's Degree",
    7: "Doctoral/Professional Degree"
}
data['edu'] = data['edu'].astype(float).map(education_map)
education_order = [
    "Less than High School",
    "High School Graduate",
    "Some College",
    "Associate Degree",
    "Bachelor's Degree",
    "Master's Degree",
    "Doctoral/Professional Degree"
]

data['edu'] = pd.Categorical(data['edu'], categories=education_order, ordered=True)
data['issues'] = data['issues'].fillna('')  # Replace NaN with empty strings
data_expanded = data.assign(
    SocialJusticePriority=data['issues'].str.split(',')
).explode('SocialJusticePriority')  # Split 'issues' into rows
data_expanded['SocialJusticePriority'] = data_expanded['SocialJusticePriority'].str.strip()
data_filtered = data_expanded[data_expanded['edu'].notnull()]
data_filtered = data_filtered[data_filtered['SocialJusticePriority'].notnull()]

priority_map = {
    "1": "Abortion",
    "2": "Prices",
    "3": "Housing",
    "4": "Politicians",
    "5": "Immigration",
    "6": "Climate",
    "7": "Wars",
    "8": "Crime",
    "9": "Education",
    "10": "Taxes",
    "11": "Guns",
    "12": "Race"
}
data_filtered['SocialJusticePriority'] = data_filtered['SocialJusticePriority'].map(priority_map)

# Group by education and priority to calculate normalized counts
summary = (
    data_filtered.groupby(['edu', 'SocialJusticePriority'])
    .size()
    .unstack(fill_value=0)
    .apply(lambda x: x / x.sum(), axis=1)  # Normalize proportions (0 to 1)
)

# Plotting/Creating the heatmap
plt.figure(figsize=(14, 8))
sns.heatmap(
    summary, cmap="YlGnBu", annot=True, fmt=".2f", linewidths=0.5, 
    cbar_kws={'label': 'Proportion of Prioritization'}
)
plt.title("Social Justice Prioritization by Education Level", fontsize=18)
plt.xlabel("Social Justice Priority", fontsize=12)
plt.ylabel("Education Level", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

# Save the heat map if needed
#plt.savefig(r'[YOUR FILE PATH GOES HERE]', dpi=300) 
plt.show()
