import pandas as pd
from read_files_in_dir.read_files import read_files_in_dir
from import_files.import_files import import_files
from sanitize_data.sanitize_data import sanitize_data
from validate_data.validate_data import validate_data
from column_mapping.column_mapping import map_columns

files = read_files_in_dir()
df = import_files(files)

# If the file signature cannot be recognized and error is thrown and the application will exit
# Depending how the code is being run, but instead of returning the error message in the terminal an error log can be created
# Replace print(df) with your own code
if not isinstance(df, pd.DataFrame):
    print(df)
    exit

# If the file is read, continue with sanitization and validation
df = sanitize_data(df)

# In case dates don't have the format YYYY-MM-DD, adjust the columns here
try:
    df['Column C'] = pd.to_datetime(df['Column C'], format='%d-%m-%Y')
except:
    print("There is a date field that has an incorrect value and cannot be changed to a dateformat, please check the date fields")
    exit()

df = validate_data(df)
df = map_columns(df)
print(df)


############################ Clean up folders - Delete below code before package is uploaded to GitHub #######################################

import os # Delete after completion of application
import shutil # Delete after completion of application

rm_dirs = ["/import_files/__pycache__", "/read_files_in_dir/__pycache__", "/sanitize_data/__pycache__", "/validate_data/__pycache__", "/column_mapping/__pycache__"]
for rm_dir in rm_dirs:
    shutil.rmtree(os.path.join(os.path.dirname(os.path.realpath(__file__)) + rm_dir))
##############################################################################################################################################