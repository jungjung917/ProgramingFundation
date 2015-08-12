import os
def rename_file():
    saved_path = os.getcwd()
    print(saved_path)
    file_path = saved_path+"/prank"
    file_list = os.listdir(file_path)
    print(file_list)
    os.chdir(file_path)    
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_file()

    

