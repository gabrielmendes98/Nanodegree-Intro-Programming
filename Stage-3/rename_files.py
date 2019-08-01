import os
def rename_files():
    file_list = os.listdir(r"C:\\Users\\GABRIEL\\Desktop\\Blocks")
    print (file_list)
    os.chdir(r"C:\\Users\\GABRIEL\\Desktop\\Blocks")

    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "s"))

    print "Finish. Exiting..."

rename_files()
