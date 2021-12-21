import os
import queue
# Traverses every file in a directory and adds a header text containing legal information
# Traverse through each file in directory


# returns True if file is txt or js, False otherwise
def txt_or_js(filename):
    # if(".txt" or ".js" in filename):
    #     return True
    # else:
    #     return False
    if filename[len(filename) - 4: len(filename)] == ".txt":
        return True
    elif filename[len(filename) - 3: len(filename)] == ".js":
        return True
    else:
        return False


# returns list (as strings) of text and js files' addresses from folder
def files_in_folder(folder_address):
    # Get list of all files in folder
    # Scan list and remove any files that don't end in .txt or .js
    # Update each string in list by concatenating directory address in front of the filename
    # Return the list of file addresses
    all_files = os.listdir(folder_address)
    # print(all_files)
    # print("range = " + str(len(all_files)))
    # for index in range(len(all_files)):
    index = 0
    while index < int(len(all_files)):
        # print(index)
        # print(all_files)
        if not txt_or_js(all_files[index]):
            all_files.pop(index)
        else:
            index = index + 1

    directory_address = folder_address
    for i in range(len(all_files)):
        all_files[i] = directory_address + "\\" + all_files[i]

    return all_files


# updates queue_of_folders with subfolders' addresses in folder parameter
def update_queue_with_subfolders_in(folder_address, queue_param):
    folder_obj = os.scandir(folder_address)
    for entry in folder_obj:
        if entry.is_dir():
            # update Queue
            entry_as_address = folder_address + "\\" + entry.name
            queue_param.put(entry_as_address)
    folder_obj.close()
    return queue_param


def update_file_with_info(file_address):
    # open file
    # copy the files contents
    # close file
    try:
        f = open(file_address, 'r')
        original_file_contents = f.read()
    finally:
        f.close()

    # write to the same file the legal information
    # append the same file with the contents originally copied from it
    with open(file_address, 'w') as f:
        f.write("This is the legal information added to the beginning of the file\n")
        f.write(original_file_contents)
    # file automatically closes at end of statement


def run():
    # queue variable
    queue_of_folders = queue.Queue()
    queue_of_folders.put("C:\\Users\sghap.LAPTOP-D23AABQP.000\Desktop\Sample_directory - Copy")

    while not queue_of_folders.empty():
        current_folder_address = queue_of_folders.get()
        file_addresses_list = files_in_folder(current_folder_address)
        for file_address in file_addresses_list:
            # update file with legal info on top
            update_file_with_info(file_address)
        queue_of_folders = update_queue_with_subfolders_in(current_folder_address, queue_of_folders)


run()
