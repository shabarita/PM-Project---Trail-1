import csv
import matplotlib.pyplot as plt

# Initialize counters
open_count = 0
closed_count = 0

# Open the CSV file for reading
with open('tasks.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        report_status = row['Report Status']

        if report_status == 'Open':
            open_count += 1
        elif report_status == 'Closed':
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
