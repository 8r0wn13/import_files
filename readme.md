# Import Files
Import files is a customizable package to import files based on their file signature, not file extension.
Normally files are read by their file extension, but this is not always accurate, f.e. SAP Excel files - *.xls (old Excel format) - are actually tab separated value files.

These modules make sure you can:
* import files
* read any file where the file signature is defined - modify the code to add more signatures
  Current files supported are Excel files (xlsx and xls, tab separated csv files and comma separted files)
* perform clean-up and get rid of empty columns and file headers, except the field names
* validate whether the data in the respective fields have the accurate data type

I kept it so fragmented, as my intention is that people can also only use parts of the package and it will be as generic as possible.
Out of the box it might not be usable, as it requires some configuration in the signature_and_extension and column_mapping dictionary
Instead of dictionaries, also external files can be used, however, this is not accounted for in this package

## Usage
Make sure the required packages are installed as mentioned in requirements.txt
Clone the repo to destination with git clone <<provide GitHub name and package name>>

In case you don't need the whole package, you can also copy the invidual files or lines of code from the files what suits your needs

### read_files.py
Will read the specified directory for files and returns a list with the files with the full path name
So far it is only tested with 1 file source file in the data folder

### import_files.py
This module will follow the following process to actually import the data from files:
* loop through the files found
* read each file in binary
* convert each binary data to hexdecimal
* lookup the file signature in the signature_and_extension dictionary - modify to your own needs depending on the files you use
* depending on the file signature found it will read the data and return it in a dataframe

### sanitize.py
Sanitize will clean up the data, cleansing if you will, by removing the file headers (not the field names) and empty columns
In sanitize.py, update the value -1 to a higher number, if file headers are in multiple columns
It will not remove fields where the values are NaN

### validate.py
Validate will use a dictionary to change the data type of each field according to the dictionary
In case fields cannot be converted to the respective data type, ValueErrors are being returned

The dictionary can be configured as desired

### column_mapping.py
Usually, field names from the source data cannot be used by the target data
This module uses a dictionary where the original field name can be configured and the field name for the targeted data model
Modify the column_mapping dictionary to your use