import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Easy Data Viz')
# File upload
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    # Data Filtering
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    filter_conditions = []
    
    for column in columns:
        unique_values = df[column].unique()
        selected_values = st.multiselect(f"Select values for {column}", unique_values)
        if selected_values:
            filter_conditions.append(df[column].isin(selected_values))
    
    if filter_conditions:
        filtered_df = df[filter_conditions[0]]
        for condition in filter_conditions[1:]:
            filtered_df = filtered_df[condition]
        st.write(filtered_df)
    else:
        filtered_df = df
    
    # Data Visualization
    st.subheader("Plot Data")
    plot_type = st.selectbox("Select Plot Type", ["Line Plot", "Bar Plot", "Scatter Plot", "Histogram", "Correlation Heatmap"])
    
    if plot_type != "Correlation Heatmap":
        x_column = st.selectbox("Select x-axis column", columns)
        y_column = st.selectbox("Select y-axis column", columns)

    if plot_type == "Line Plot":
        st.line_chart(filtered_df.set_index(x_column)[y_column])
    elif plot_type == "Bar Plot":
        st.bar_chart(filtered_df.set_index(x_column)[y_column])
    elif plot_type == "Scatter Plot":
        plt.figure(figsize=(10, 6))
        sns.scatterplot(data=filtered_df, x=x_column, y=y_column)
        st.pyplot(plt)
    elif plot_type == "Histogram":
        plt.figure(figsize=(10, 6))
        sns.histplot(data=filtered_df, x=x_column)
        st.pyplot(plt)
    elif plot_type == "Correlation Heatmap":
        plt.figure(figsize=(10, 6))
        sns.heatmap(filtered_df.corr(), annot=True, cmap="coolwarm")
        st.pyplot(plt)
    
    # Download Filtered Data
    st.subheader("Download Filtered Data")
    csv = filtered_df.to_csv(index=False)
    st.download_button(label="Download as CSV", data=csv, file_name='filtered_data.csv', mime='text/csv')
else:
    st.write("Waiting for File Upload...")

    
    









