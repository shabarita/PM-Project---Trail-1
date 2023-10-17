import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('tasks.csv')

# Remove duplicate rows
df = df.drop_duplicates()

# Group by 'Task Group' and count 'Open' and 'Closed' tasks
grouped = df.groupby(['Task Group', 'Report Status']).size().unstack().fillna(0)

# Create individual bar charts for each 'Task Group'
for task_group, data in grouped.iterrows():
    data.plot(kind='bar', title=f'{task_group} - Open vs. Closed Tasks')
    plt.xlabel('Status')
    plt.ylabel('Count')
    
    # Save the chart as an image file
    plt.savefig(f'{task_group}_task_chart.png')
    
    # Show the chart
    plt.show()

# Create a clustered bar chart
grouped.plot(kind='bar', stacked=True, title='Open vs. Closed Tasks by Task Group')
plt.xlabel('Task Group')
plt.ylabel('Count')

# Save the clustered chart as an image file
plt.savefig('clustered_task_chart.png')

# Show the clustered chart
plt.show()

# Print the results
print("Count of 'Open' and 'Closed' Tasks by 'Task Group':")
print(grouped)
