import pandas as pd

def validate_data(df):
    # Convert fields to the exptected date type
    # Add the field names to the list in the respective blocks
    
    for d in df.columns:
        # Convert fields to expected date format
        if d in ["Column A", "Column C"]:
            try:
                df[d] = pd.to_datetime(df[d], format='%Y-%m-%d')
            except:
                print(d + " could not be converted to a date due to incorrect values in this column")
                exit()
        # Convert fields to strings
        elif d in ["Column B", "Column D"]:
            try:
                df[d] = df[d].astype(str)
            except:
                print(d + " could not be converted to a string due to incorrect values in this column")
                exit()
        # Convert fields to floats
        elif d in ["Column E"]:
            try:
                df[d] = df[d].astype(float)
            except:
                print(d + " could not be converted to a float due to incorrect values in this column")
                exit()

    return df
   