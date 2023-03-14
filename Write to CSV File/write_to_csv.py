import csv
data_to_append = []
data = []

## Use in this list the headers of preset_file.csv
headers = [
    'business ID',
    'national ID',
    'Job Title',
    'Birth Date',
    'Hire Date',
    'Gender'
]

for txt in headers:
    income = input(f'{txt} : ')
    data.append(income)

data_to_append.append(data[:])

file = open('./Write to CSV File/preset_file.csv', 'a', newline='')
writer = csv.writer(file)
writer.writerows(data_to_append)
file.close()
