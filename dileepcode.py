import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def read_data(file_path):
    """
    Reads data from the given CSV file and returns a pandas DataFrame.

    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the data from the CSV file.
    """
    data = pd.read_csv(file_path)
    return data

def plot_emissions_by_country(data):
    """
    Plots total greenhouse gas emissions by country for the years 1998-2012.

    Parameters:
    data (pd.DataFrame): DataFrame containing the emissions data.

    Returns:
    None
    """
    years = list(data.columns[4:])
    countries = data['Country Name']
    emissions = data.iloc[:, 4:]

    plt.figure(figsize=(10, 6))
    for i in range(len(countries)):
        if not emissions.iloc[i].isnull().all():
            line_styles = ['-', '--', '-.', ':']
            marker_styles = ['o', 's', '^', 'D']
            color = plt.cm.get_cmap('tab10')(i / len(countries))

            line_style = line_styles[i % len(line_styles)]
            marker_style = marker_styles[i % len(marker_styles)]

            plt.plot(years, emissions.iloc[i], label=countries.iloc[i], linestyle=line_style, marker=marker_style, color=color)

    plt.xlabel('Year')
    plt.ylabel('Total Greenhouse Gas Emissions (kt of CO2 equivalent)')
    plt.title('Total Greenhouse Gas Emissions by Country (1998-2012)')

    handles, labels = plt.gca().get_legend_handles_labels()
    filtered_labels = [label for label in labels if label != 'nan']
    plt.legend(handles, filtered_labels, loc='upper left', bbox_to_anchor=(1.05, 1), title='Legend')

    explanation_text = "This plot shows the total greenhouse gas emissions (in kilotons of CO2 equivalent) for various countries from 1998 to 2012."
    plt.figtext(0.5, 0.01, explanation_text, wrap=True, horizontalalignment='center', fontsize=10)

    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('output_plot.png', bbox_inches='tight')
    plt.show()
def plot_emissions_pie(data, year):
    """
    Plots a pie chart showing the distribution of emissions by country for a specific year.

    Parameters:
    data (pd.DataFrame): DataFrame containing the emissions data.
    year (str): The specific year for which the pie chart will be plotted.

    Returns:
    None
    """
    emissions_year = data[year]
    countries = data['Country Name']

    # Filter out NaN values before creating the pie chart
    valid_indices = ~emissions_year.isnull()
    emissions_year = emissions_year[valid_indices]
    countries = countries[valid_indices]

    # Define a custom colormap for colors
    colors = plt.cm.get_cmap('tab20c')(np.arange(len(countries)) % 20)

    # Explode a specific country for emphasis (e.g., the first country)
    explode = [0.1 if i == 0 else 0 for i in range(len(countries))]

    plt.figure(figsize=(8, 8))
    plt.pie(emissions_year, labels=countries, autopct='%1.1f%%', startangle=140,
            colors=colors, explode=explode, shadow=True, wedgeprops={'edgecolor': 'black'})
    plt.title(f'Total GreenHouse gas emissionss by Country ({year})')

    # Optionally save the pie chart
    plt.savefig(f'emissions_pie_{year}.png', bbox_inches='tight')

    plt.show()

def plot_emissions(data, year):
    """
    Plots a bar chart showing the emissions for each country for a specific year.

    Parameters:
    data (pd.DataFrame): DataFrame containing the emissions data.
    year (str): The specific year for which the bar chart will be plotted.

    Returns:
    None
    """
    emissions_year = data[year].dropna()
    countries = data['Country Name'].iloc[emissions_year.index]

    plt.figure(figsize=(12, 8))
    plt.bar(countries, emissions_year, color='skyblue', edgecolor='black')
    plt.xlabel('Country')
    plt.ylabel('Greenhouse Gas Emissions (kt of CO2 equivalent)')
    plt.title(f'Greenhouse Gas Emissions by Country ({year})')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Optionally save the bar plot
    plt.savefig(f'emissions_barplot_{year}.png', bbox_inches='tight')

    plt.show()


def main():
    # Path to the CSV file
    file_path = r'Total greenhouse gas emissions (kt of CO2 equivalent).csv'

    # Read data from the CSV file
    data = read_data(file_path)
 # Specify the year for the pie chart and histogram
    pie_year = '2012'
    # Plot emissions pie chart
    # Plot emissions by country with custom styles
    plot_emissions_by_country(data)
  # Specify the year for the pie chart
    pie_year = '2012'
    plot_emissions_pie(data, pie_year)
    pie_year = '1998'
    plot_emissions_pie(data, pie_year)
    seleted = '2000'
    plot_emissions(data,seleted)

if __name__ == "__main__":
    main()
