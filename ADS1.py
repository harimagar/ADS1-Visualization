# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 19:08:21 2023

@author: HP
"""

import matplotlib.pyplot as plt
import pandas as pd

def read_data_from_csv(file_path):
    """
    Read crime data from a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    Tuple: A tuple containing lists of years and various crime categories.
    """
    data = pd.read_csv(file_path)
    return (
        data['Year'],
        data['Murder'],
        data['Robbery'],
        data['Burglary'],
        data['Forcible_Rape'],
        data['Vehicle_Theft'],
        data['Aggravated_assault'],
        data['Larceny_Theft']
    )

def plot_single_category(years, data, label, color):
    """
  Plot a single crime category over the years.

  Parameters:
  - years (list): List of years.
  - data (list): List of crime data for a specific category.
  - label (str): Label for the legend.
  - color (str): Color for the plot.

  Returns:
  None
  """
    plt.plot(years, data, marker='o', linestyle='-', color=color, label=label)

def plot_multiple_categories(years, categories, labels):
    """
    Plot multiple crime categories on the same graph.

    Parameters:
    - years (list): List of years.
    - categories (list of lists): List of crime data for multiple categories.
    - labels (list): List of labels for the legend.

    Returns:
    None
    """
    for data, label in zip(categories, labels):
        plot_single_category(years, data, label, next(plt.gca()._get_lines.prop_cycler)['color'])

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Number of Incidents(per million)')
    plt.title('Crime Trends Over the Years')

    # Add a legend
    plt.legend()

    # Display the plot
    plt.show()

# Read data from CSV
file_path = 'D:/assignment/ADS1/Code/US_Crime_Rates_1960_2014.csv'  # Replace with the actual path to your CSV file
years, murder, robbery, burglary, rape, vehicle_theft, assault, larceny_theft = read_data_from_csv(file_path)

# Plot multiple categories
plot_multiple_categories(
    years,
    [ rape, vehicle_theft, larceny_theft],
    ['Forcible Rape', 'Vehicle Theft', 'Larceny Theft']
)



def create_scatter_plot(x_data, y_data, x_label, y_label, title):
    """
    Create a scatter plot.

    Parameters:
    - x_data (list): X-axis data.
    - y_data (list): Y-axis data.
    - x_label (str): Label for the x-axis.
    - y_label (str): Label for the y-axis.
    - title (str): Title of the plot.

    Returns:
    None
    """
    plt.scatter(x_data, y_data, marker='o', color='b')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def plot_crime_vs_population(years, crime_data, population_data, crime_label):
    """
    Plot a crime category against the population over the years.

    Parameters:
    - years (list): List of years.
    - crime_data (list): List of crime data for a specific category.
    - population_data (list): List of population data.
    - crime_label (str): Label for the crime category.

    Returns:
    None
    """
    crime_rate = [crime / population * 1000 for crime, population in zip(crime_data, population_data)]
    create_scatter_plot(years, crime_rate, 'Year', f'{crime_label} Rate (per 1000 people)', f'{crime_label} Rate vs Year')

# Create scatter plots
plot_crime_vs_population(years, assault, burglary, 'Aggravated Assault')

def create_histogram(ax, data, label, bins=10):
    """
    Create a histogram plot.

    Parameters:
    - ax (AxesSubplot): The subplot.
    - data (list): Data for the histogram.
    - label (str): Label for the x-axis.
    - bins (int, optional): Number of bins for the histogram. Default is 10.

    Returns:
    None
    """
    ax.hist(data, bins=bins, color='skyblue', edgecolor='black')
    ax.set_xlabel(label)
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram of {label}')
    
def plot_histogram_crime_categories(years, crime_data, labels):
    """
    Plot histograms for multiple crime categories in one figure.

    Parameters:
    - years (list): List of years.
    - crime_data (list of lists): List of crime data for multiple categories.
    - labels (list): List of labels for the x-axis.

    Returns:
    None
    """
    fig, axes = plt.subplots(nrows=1, ncols=len(crime_data), figsize=(15, 5))

    for ax, data, label in zip(axes, crime_data, labels):
        create_histogram(ax, data, label)

    plt.tight_layout()
    plt.show()

# Read data from CSV
file_path = 'D:/assignment/ADS1/Code/US_Crime_Rates_1960_2014.csv'  # Replace with the actual path to your CSV file
years, murder, robbery, burglary, rape, vehicle_theft, assault, larceny_theft = read_data_from_csv(file_path)

# Plot histograms
plot_histogram_crime_categories(years, [murder, robbery, burglary], ['Murder', 'Robbery', 'Burglary'])








