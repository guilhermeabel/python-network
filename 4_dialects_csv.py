import csv


# with open('csv/passwd.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=':', lineterminator='\n')
#     for row in reader:
#         print(row)

csv.register_dialect('hashes', delimiter='#',
                     quoting=csv.QUOTE_NONE,
                     lineterminator='\n')

with open('csv/items.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, dialect='hashes')
    for row in reader:
        print(row)

with open('csv/items.csv', 'a') as csvfile:
    writer = csv.writer(csvfile, dialect='hashes')
    writer.writerow(('spoon', 3, 1.5))
