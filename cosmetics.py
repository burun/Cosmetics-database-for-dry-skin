import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams['font.size'] = 15

# Read csv file
data = pd.read_csv('cosmetics.csv', encoding='ISO-8859-1')

# Find ingredients positive for dry skin, and create a new column
data['DryPositive'] = np.where(data['Emollient'] + data['Humectant'] + data['Moisturising'] >= 1, 'positive', 'negative')

# Print the whole table
print(data)

# Print chemical name and skin functions
print(data.loc[:, ['ChemicalName', 'DryPositive']])

# Calculate the percentage of ingredients positive and negative to dry skin
dry_positive, dry_negative = data.groupby(['DryPositive']).size()
labels = ['Positive', 'Negative']
sizes = [dry_positive, dry_negative]
colors = ['yellowgreen', 'gold']

plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90,)
plt.axis('equal')
plt.suptitle("Percentage of ingredients propertity to dry skin")
plt.show()

# Calculate functions of ingredients to dry skin
bar_name = [1,2,3,4]
labels = ['Emollient', 'Humectant', 'Moisturising', 'Negative']
sizes = [np.count_nonzero(data['Emollient']), np.count_nonzero(data['Humectant']), np.count_nonzero(data['Moisturising']), dry_negative]

plt.bar(bar_name, sizes, align="center")
plt.xticks(bar_name, labels)
plt.suptitle("Different functions of ingredients to dry skin")
plt.show()
