import shutil
import os
dir = "./data/"
for file in os.listdir(dir):
    print(file)
    # newFile = file.replace("$", "")
    # print(newFile)

    # os.rename(dir + file, dir + newFile)
    # my_file = open(dir + file, encoding="UTF-8")
    # content = my_file.read()
    # content = content.replace("kukuřici", "mrkev")
    # my_file.close()
    # my_file = open(dir + file, encoding="UTF-8", mode="w")
    # my_file.write(content)
    #print(content)
    break
