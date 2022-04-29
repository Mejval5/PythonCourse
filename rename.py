import os
import shutil
dir = "./data/"

for file in os.listdir(dir):
    
    # index_data = file.find("#5")
    
    # if index_data > -1:
    #     newDir = dir + "data5/"
    #     oldFile = dir + file
    #     newFile = newDir + file
    #     print(oldFile)
    #     print(newFile)
    #     os.makedirs("./data/data5/", exist_ok=True)
    #     shutil.copy(oldFile, newFile)
    #     os.remove(oldFile)
    
    # newFile = file[:index_data] + "#" + file[index_data:]
    # print(newFile)
    # puvodni_cesta = dir + file
    # nova_cesta = dir + newFile
    # print(puvodni_cesta)
    # print(nova_cesta)
    
    #os.rename(puvodni_cesta, nova_cesta)
    
    my_file = open(dir + file, encoding="windows-1250")
    content = my_file.read()
    my_file.close()
    content = content.replace("super panda cirkus", "kukuřice")
    print(content)
    
    my_file = open(dir + file, encoding="UTF-8", mode="w")
    my_file.write(content)
    my_file.close()
