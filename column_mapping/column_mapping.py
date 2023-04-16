import pandas as pd

# This is the mapping to convert field names from the source data to the target model
# If field name is not included in the list below it will still be included in the data, simply not renamed
# If the mapping contains a mapping, but such a field doesn't exist in the source data, no mapping will be applied
# Note that the field name from the source file needs to be exact, including capitalization, spaces and special characters
column_mapping = {
    "Column A": "Column V",
    "Column B": "Column W",
    "Column C": "Column X",
    "Column D": "Column Y",
    "Column E": "Column Z"
}

def map_columns(df):
    df.rename(columns=column_mapping, inplace=True)
    
    return df