import os

# There is a data folder in the same directory as the main file
# Change "/../data" to navigate to the correct folder
# In case there is an absolute path in a different location:
## Or comment out: dir_path = os.path.dirname(os.path.realpath(__file__))
## And uncomment: dir_path = "" and give the absolute path
def read_files_in_dir():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    # dir_path = ""

    # Return the full path + filename
    return [os.path.join(dir_path + "/../data", f) for f in os.listdir(dir_path + "/../data") if os.path.isfile(os.path.join(dir_path + "/../data", f))]