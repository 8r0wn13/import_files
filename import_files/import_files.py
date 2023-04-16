import pandas as pd

# Define here which files need to be imported/recognized and their file signature
signature_and_extension = {
    "xlsx": "50 4B 03 04",
    "xls": "D0 CF 11 E0 A1 B1 1A E1",
    "comma_csv": "48 65 61 64 65 72 20 72 6F 77 20 31 2C",
    "tab_csv": "48 65 61 64 65 72 20 72 6F 77 20 31 09"
}

def import_files(files):
    try:
        for f in files:
            # Read the file as bytes
            file = open(f, "rb").read(32)

            # Convert bytes to hex
            fileHexNumbers = " ".join(['{:02X}'.format(byte) for byte in file])

            # Loop through signature_and_extension list and compare the file signature
            # If there is a match, read the file with the right pandas function
            for key, value in signature_and_extension.items():
                sig_length = len(signature_and_extension[key])
                if signature_and_extension[key] == fileHexNumbers[:sig_length] and key in ["xlsx", "xls"]:
                    try:
                        return pd.read_excel(f)
                    except:
                        print("The file could not be read. Check if the file is an Excel file indeed")
                        exit()
                elif signature_and_extension[key] == fileHexNumbers[:sig_length] and key == "comma_csv":
                    try:
                        return pd.read_csv(f)
                    except:
                        print("The file could not be read. Check if the file is a CSV file indeed")
                        exit()
                elif signature_and_extension[key] == fileHexNumbers[:sig_length] and key == "tab_csv":
                    try:
                        # Depending on the system (Mac/Linux/Windows) you need to change the lineterminaator (\r, \n or \r\n)
                        return pd.read_csv(f,sep="\t", lineterminator="\n")
                    except:
                        print("The file could not be read. Check if the file is a CSV file indeed")
                        exit()
                
            # Return error if file signature cannot be recognized
            print("The file signature could not be recognized")
            exit()
    except:
         print("The path is not correct. Check if the application is navigating correctly to the right folder in read_files.py. In case an absolute path is used, check if the absolute path is correct.")
         exit()