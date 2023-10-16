import csv

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
