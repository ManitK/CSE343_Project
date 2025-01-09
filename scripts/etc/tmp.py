import csv
import sys
csv.field_size_limit(sys.maxsize)

file = "/Users/manitk/Desktop/SEM V/ML_Project/Datasets/jira_issues.csv"
# accepted = ['enhancement', 'normal','blocker','major','enhancement','critical','minor']
types = set()
type_dict = {}

with open(file, 'r') as f:
    reader = csv.DictReader(f)
    num_headers = len(reader.fieldnames)
    headers = reader.fieldnames
    for row in reader:
        severity = row['priority']
        if severity not in types:
            types.add(severity)
            type_dict[severity] = 1
        else:
            type_dict[severity] += 1

print(len(types))
# print(types)
sorted_types = sorted(type_dict.items(), key=lambda x: x[1], reverse=True)
for i in sorted_types:
    print(i)