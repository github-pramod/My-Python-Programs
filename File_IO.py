# ********* To write text in all the mentioned files. **************

import os

num_of_files = input("enter the number of files: ")  # takes the number of files to be changed from user.
for i in range(0, int(num_of_files)):
    file_name = input("enter the file name with extension .txt: ")
    file = os.path.isfile(file_name)  # returns True if the given file is present in the folder where this program is present.
    if file is True:
        with open(file_name, 'a+') as file:
            file.write("\nPython is very interesting programming language!!")

    else:
        with open(file_name, 'w') as file:
            file.write("\nPython is very interesting programming language!!\n")
