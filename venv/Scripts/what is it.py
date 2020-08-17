copy_file = open("C:\\Users\\Adir\\Desktop\\copy_file.txt")
paste_file = open("C:\\Users\\Adir\\Desktop\\paste_file.txt", 'a')

for line in copy_file.readlines():
    if 'tests/file/myword' in line:
        paste_file.write(line)

copy_file.close()
paste_file.close()