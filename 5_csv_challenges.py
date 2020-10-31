# 1 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Consider the following Python list:
people = [
    ['Dan', 34, 'Bucharest'],
    ['Andrei',21, 'London'],
    ['Maria', 45, 'Paris']
]
# Using the CSV module write each element of the list (which is another list) into a 
# CSV file called people1.csv
# After writing into the file, read and print out the file contents.
# Use the default , (comma) as the delimiter.
# 1 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
import csv
with open('csv/people1.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for line in people:
        writer.writerow(line)

# with open('csv/people1.csv', 'r') as file:
#     reader = csv.reader(file)
#     main_list = list()
#     for row in reader:
#         main_list.append(row)

# print(main_list)
    

# 2 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Change the solution from the previous challenge and use : (colon) as the delimiter.
# 2 =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


reader = csv.reader(open('csv/people1.csv'))
writer = csv.writer(open("csv/people1_2.csv", 'w'), delimiter=':')
writer.writerows(reader)
