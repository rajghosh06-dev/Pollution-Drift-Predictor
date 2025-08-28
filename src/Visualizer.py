# src/visualizer.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_drift(df):
    """
    Plots wind speed vs particulate level, colored by wind direction.
    Input:
        df - DataFrame with pollution data
    Output:
        Scatter plot
    """
    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=df, x='wind_speed', y='particulate_level', hue='wind_direction')
    plt.title('Wind Speed vs Particulate Level')
    plt.xlabel('Wind Speed')
    plt.ylabel('Particulate Level')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
