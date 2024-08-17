## Overview
Vizualite is a simple and interactive data visualization tool built with Streamlit. It allows users to upload CSV or Excel files, filter the data based on multiple conditions, and create various types of visualizations. The tool also provides a summary of the data and allows users to download the filtered dataset.

## Features
File Upload: 
Upload CSV or Excel files to analyze and visualize the data.

Data Preview: 
View the first few rows of the dataset to understand its structure.

Data Summary: 
Get a statistical summary of the dataset, including mean, median, and standard deviation.

Data Filtering: 
Filter the dataset based on selected values from each column.

Data Visualization: Generate various types of plots:
Line Plot
Bar Plot
Scatter Plot
Histogram
Correlation Heatmap
Download Filtered Data: Download the filtered dataset as a CSV file for further analysis.
How It Works
File Upload:

Upload a CSV or Excel file using the "Upload CSV or Excel file" button.
The tool supports .csv and .xlsx file formats.
Data Preview:

After uploading, a preview of the first few rows of the dataset is displayed.
Data Summary:

A statistical summary of the dataset is provided, including key metrics like mean, median, standard deviation, etc.
Data Filtering:

Users can filter the data by selecting specific values for each column.
Multiple filters can be applied simultaneously.
Data Visualization:

Choose the type of plot you want to generate:
Line Plot: Plots a line chart with selected x and y-axis columns.
Bar Plot: Creates a bar chart using the selected x and y-axis columns.
Scatter Plot: Generates a scatter plot with the selected columns.
Histogram: Displays the distribution of a selected column.
Correlation Heatmap: Shows the correlation matrix of the dataset.
The visualizations are displayed directly within the app.
Download Filtered Data:

After filtering the data, users can download the filtered dataset as a CSV file.


Installation
To run the Easy Data Viz app locally, follow these steps:

Clone the repository:
git clone https://github.com/yourusername/easy-data-viz.git
cd easy-data-viz
Install the required Python packages:


pip install -r requirements.txt
Run the Streamlit app:


streamlit run app.py
Open your browser and go to http://localhost:8501 to interact with the app.

Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue to discuss any changes.
