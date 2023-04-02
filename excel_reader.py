import pandas as pd

def read_excel_file(file_path):
    """
    Read the contents of an Excel file and return a pandas DataFrame.

    :param file_path: The path to the Excel file.
    :return: A pandas DataFrame containing the data from the Excel file.
    """
    data_frame = pd.read_excel(file_path, engine='openpyxl')
    return data_frame
