import os
import pandas as pd
import re

#import the dataset
def import_data(path):
    for file in os.listdir(path):
        import_csv = os.path.join(path,file)
        csv = pd.read_csv(import_csv)
    return csv

def clean_dataset(df):
    dataset = df.copy()

    #rename the column country
    dataset = dataset.rename(columns={'County' : 'Country'})

    #clean the columns
    clean_column_copy = dataset.columns
    transformed_col_list = []
    for col in clean_column_copy:
        cleaned_col = re.sub(r'[0-9]','', col)
        cleaned_col = re.sub(r'\(.*?\)', '', cleaned_col).strip()
        cleaned_col = re.sub(r'\s+', '_', cleaned_col)
        cleaned_col = cleaned_col.upper()
        transformed_col_list.append(cleaned_col)

    #assigng new column names to dataframe
    dataset.columns = transformed_col_list

    #convert all the data to uppercase
    dataset = dataset.map(lambda x: x.upper() if isinstance(x, str) else x)

    #handling missing values
    dataset = dataset.fillna("")

    return dataset
