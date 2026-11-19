import pandas as pd

def clean_data(file_path):
    df = pd.read_excel(file_path)
    df = df.drop_duplicates()
    df = df.dropna(how="all")
    return df
