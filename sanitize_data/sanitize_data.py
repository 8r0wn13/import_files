def sanitize_data(df):
    # Remove all empty columns
    df.dropna(how="all", axis=1, inplace=True)

    # Remove all empty rows
    ## If the file headers are in more than 1 column, increase -1 to a higher number, e.g. -2, -3, etc
    df.dropna(axis=0, thresh=df.shape[1]-1, inplace=True)   
    
    # Remove all empty columns
    df.dropna(how="all", axis=1, inplace=True)

    # Set the first row to column headers
    # Delete the first row as these are the headers
    # Reset the index, so line items starts with 0
    df.columns = df.iloc[0]
    df.drop(df.index[0], inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    return df