import pandas as pd
import matplotlib.pyplot as plt

# read the data into a pandas dataframe
df = pd.read_csv('UPI_apps_transaction_data_in_2021.csv')

# filter the data to the desired month
month = 1  # replace with the desired month
filtered_data = df[df['Month'] == month]

# group the data by UPI Banks and sum the value by customers
grouped_data = filtered_data.groupby(['UPI Banks'])['Value (Cr) by Costumers'].sum()

# plot the data
plt.bar(grouped_data.index, grouped_data.values)
plt.xticks(rotation=90, ha='right', fontsize=8)
plt.xlabel('UPI Banks')
plt.ylabel('Total Value (Cr) by Customers')
plt.title('Max UPI Bank by Value for ' + str(month))
plt.tight_layout()
plt.show()
