# Simple Shiny App in Python

This is a simple Shiny application built with Python that demonstrates interactive data visualization.

## Features

- Interactive slider to control the number of data points
- Multiple plot types: Scatter plot, Histogram, and Line plot
- Customizable plot title
- Summary statistics table
- Responsive layout with sidebar and main panel

## Requirements

- Python 3.7+
- shiny
- matplotlib
- pandas
- numpy

## Installation

1. Make sure you have Python installed
2. Install the required packages:
   ```bash
   pip install shiny matplotlib pandas numpy
   ```

## Running the App

To run the Shiny app, execute:

```bash
python app.py
```

The app will start and be available at `http://localhost:8000` in your web browser.

## App Structure

The app consists of:
- **Sidebar**: Contains input controls for customizing the visualization
- **Main Panel**: Displays the interactive plot and summary statistics table

## Usage

1. Use the slider to adjust the number of random data points (10-500)
2. Select different plot types from the dropdown menu
3. Enter a custom title for your plot
4. View the summary statistics in the table below the plot
