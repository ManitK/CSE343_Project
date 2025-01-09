import csv
import sys
csv.field_size_limit(sys.maxsize)

file = "/Users/manitk/Desktop/SEM V/ML_Project/Datasets/jira_issues.csv"
defect = ['Bug', 'Defect', 'Patch', 'Test', 'Clarification', 'Quality Risk', 'Support Patch', 'Backport', 'TCK Challenge', 'CTS Challenge']
improvement = ['Improvement', 'New Feature', 'Feature Request', 'Enhancement', 'Wish', 'Component Upgrade', 'Dependency upgrade', 'Remove Feature', 'Library Upgrade', 'Component  Upgrade', 'Refactoring', 'Release','Deprecation']
task = ['Task', 'Sub-task', 'Story', 'Documentation', 'Question', 'Brainstorming', 'Technical task', 'Umbrella', 'Suitable Name Search', 'Tracker', 'Epic', 'Requirement', 'New JIRA Project', 'Temp', 'RTC', 'Pruning', 'Support','Requirement']
new_data = []
a = 0
b = 0
c = 0
with open(file, 'r') as f:
    reader = csv.DictReader(f)
    num_headers = len(reader.fieldnames)
    print(num_headers)
    headers = reader.fieldnames
    for row in reader:
        severity = row['type']
        if severity in defect:
            # row['type'] = 'Defect'
            new_data.append(row)
            a += 1
        elif severity in improvement:
            # row['type'] = 'Improvement'
            new_data.append(row)
            b += 1
        elif severity in task:
            # row['type'] = 'Task'
            new_data.append(row)
            c += 1

print(len(new_data))
print(a,b,c)    