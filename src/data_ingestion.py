# src/data_ingestion.py

import pandas as pd

def load_data(filepath):
    """
    Loads pollution data from a CSV file.
    Input:
        filepath - path to the CSV file
    Returns:
        df - pandas DataFrame
    """
    df = pd.read_csv(filepath)
    return df

def preprocess_data(df):
    """
    Adds wind angle based on wind direction.
    Input:
        df - raw DataFrame
    Returns:
        df - processed DataFrame with wind_angle column
    """
    direction_map = {
        'N': 0, 'NE': 45, 'E': 90, 'SE': 135,
        'S': 180, 'SW': 225, 'W': 270, 'NW': 315
    }
    df['wind_angle'] = df['wind_direction'].map(direction_map)
    return df
