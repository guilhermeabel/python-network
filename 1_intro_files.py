
# ######################### OPEN FILES METHOD 1

# f = open('txt/file.txt', 'r')

# content = f.read(5)
# print(content)

# content = f.read(3)
# print(content) 

# print(f.tell())

# print(f.seek(2))

# content = f.read(6)
# print(content)

# print(f.closed)
# f.close()

# ######################### OPEN FILES METHOD 2

# with open('txt/file.txt', 'r') as file:
#     file.seek(4)
#     print(file.read(5))

# # STORE LINES IN LIST

# with open('txt/file.txt', 'r') as file:
#     list = file.read().splitlines()
#     print(list)

# with open('txt/file.txt', 'r') as file:
#     list = file.readlines()
#     print(list)

# with open('txt/file.txt', 'r') as file:
#     for line in file:
#         print(line)

# ######################### WRITE FILES

with open('txt/myfile.txt', 'w') as file:  # w irá criar um novo arquivo se não existir
    # e irá SOBRESCREVER se já existir um arquivo de mesmo nome
    file.write('This is a string\n')
    file.write('This is a new string\n')

# ######################### APPEND TO FILES

with open('txt/myfile.txt', 'a') as file:  # append cria um novo arquivo se ele não existe
    file.write('This is a string\n')
    file.write('This is a new string')

# ######################### READ AND WRITE

with open('txt/myfile.txt', 'r+') as file:
    file.seek(5)
    # r+ adiciona na primeira linha, nao no final
    file.write('Line added with r+\n')
