import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('tasks.csv')

# Remove duplicate rows
df = df.drop_duplicates('Ref')

# Initialize counters
open_count = 0
closed_count = 0

# Count 'Open' and 'Closed' tasks
for status in df['Report Status']:
    if status == 'Open':
        open_count += 1
    elif status == 'Closed':
        closed_count += 1

# Print the results
print(f'Open Tasks: {open_count}')
print(f'Closed Tasks: {closed_count}')

# Create a bar chart
labels = ['Open', 'Closed']
values = [open_count, closed_count]

plt.bar(labels, values)
plt.xlabel('Status')
plt.ylabel('Count')
plt.title('Open vs. Closed Tasks')

# Save the chart as an image file
plt.savefig('task_chart.png')

# Optionally, display the path to the saved image
print("Bar chart saved as 'task_chart.png'")
