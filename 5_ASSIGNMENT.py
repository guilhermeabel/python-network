import csv


with open('csv/devices.csv', 'r') as file:
    reader = csv.reader(file, delimiter=':')
    main_list = list()
    for row in reader:
        main_list.append(row)

print(main_list)


# with open('txt/devices.txt') as f:
#     devices = f.read().splitlines()

# mylist = list()

# for item in devices:
#     tmp = item.split(':')
#     mylist.append(tmp)

# print(mylist)
