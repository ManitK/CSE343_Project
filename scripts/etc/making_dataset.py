import xml.etree.ElementTree as ET

tree = ET.parse('/Users/manitk/Desktop/SEM V/ML_Project/Datasets/msr2013-bug_dataset-master/data/mozilla/Thunderbird/severity.xml')
root = tree.getroot()

bugs = {}
for report in root.findall('report'):
    report_id = report.get('id')
    for update in report.findall('update'):
        timestamp = update.find('when').text
        severity = update.find('what').text
        if severity != 'normal' and severity != 'enhancement':
            bugs[(report_id, timestamp)] = {'severity': severity,'description':""}

# i = 5
# for key, value in bugs.items():
#     if i == 0:
#         break
#     print(key, value)
#     i -= 1

tree = ET.parse('/Users/manitk/Desktop/SEM V/ML_Project/Datasets/msr2013-bug_dataset-master/data/mozilla/Thunderbird/short_desc.xml')
root = tree.getroot()

for report in root.findall('report'):
    report_id = report.get('id')
    for update in report.findall('update'):
        timestamp = update.find('when').text
        desc = update.find('what').text
        key = (report_id, timestamp)
        if key in bugs:
            bugs[key]['description'] = desc

# i = 5
# for key, value in bugs.items():
#     if i == 0:
#         break
#     print(key, value)
#     i -= 1

new_data = {}
for key, value in bugs.items():
    if value['description'] == "":
        continue
    new_data[key] = value

import csv
file = "/Users/manitk/Desktop/SEM V/ML_Project/Datasets/msr2013_csv/mozilla_thunderbird.csv"
with open(file, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['id', 'timestamp','description','severity'])
    for key, value in new_data.items():
        writer.writerow([key[0], key[1], value['description'], value['severity']])