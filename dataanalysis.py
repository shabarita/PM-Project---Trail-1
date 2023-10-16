import csv

# Initialize counters for tasks
open_count = 0
closed_count = 0
overdue_count = 0

# Open the CSV file for reading
with open('tasks.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        report_status = row['Report Status']
        over_due = row['OverDue']

        if report_status == 'Open' and over_due == 'True':
            overdue_count += 1
        elif report_status == 'Open' and over_due == 'False':
            open_count += 1
        else:
            closed_count += 1

# Print the results
print(f'Open Tasks: {open_count}')
print(f'Closed Tasks: {closed_count}')
print(f'Overdue Tasks: {overdue_count}')
