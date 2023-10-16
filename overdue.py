import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('tasks.csv')

# Remove duplicate rows
df = df.drop_duplicates()

# Filter the DataFrame to include only 'OverDue' tasks with value 'True'
overdue_true = df[df['OverDue'] == True]

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

# Create a clustered bar chart for 'Open' and 'Closed' tasks
grouped[['Open', 'Closed']].plot(kind='bar', stacked=True, title='Open vs. Closed Tasks by Task Group')
plt.xlabel('Task Group')
plt.ylabel('Count')

# Save the clustered chart as an image file
plt.savefig('clustered_task_chart.png')

# Show the clustered chart
plt.show()

# Calculate counts of 'Overdue' tasks with value 'True'
overdue_counts = overdue_true['OverDue'].value_counts()

# Create a bar chart for 'OverDue' tasks with value 'True'
overdue_by_project = overdue_true['project'].value_counts()
overdue_by_project.plot(kind='bar', title='OverDue Tasks by Project (True Only)')
plt.xlabel('Project')
plt.ylabel('Count')

# Save the 'OverDue' chart as an image file
plt.savefig('overdue_task_chart.png')

# Show the 'OverDue' chart
plt.show()

# Print the results
print("Count of 'Open' and 'Closed' Tasks by 'Task Group':")
print(grouped)
print("\nCount of 'Overdue' Tasks with value 'True':")
print(overdue_counts)
