import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load the data
    df = pd.read_csv("epa-sea-level.csv")

    # Extract x and y
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(x, y)

    # First line of best fit (1880 to 2050)
    reg = linregress(x, y)
    x_forecast = pd.Series(range(x.min(), 2051))
    y_forecast = reg.slope * x_forecast + reg.intercept
    ax.plot(x_forecast, y_forecast, 'r', label='Best fit: All data')

    # Second line of best fit (from year 2000 to 2050)
    df_2000 = df[df['Year'] >= 2000]
    new_x = df_2000['Year']
    new_y = df_2000['CSIRO Adjusted Sea Level']
    new_reg = linregress(new_x, new_y)
    new_x_forecast = pd.Series(range(2000, 2051))
    new_y_forecast = new_reg.slope * new_x_forecast + new_reg.intercept
    ax.plot(new_x_forecast, new_y_forecast, color='blue', label='Best fit: From 2000')

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.legend()

    # Set specific ticks for testing
    ax.set_xticks([1850, 1875, 1900, 1925, 1950, 1975, 2000, 2025, 2050, 2075])

    # Save and return
    plt.savefig('sea_level_plot.png')
    return plt.gca()
