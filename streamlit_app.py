import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

# Set the title of the Streamlit app
st.title('Stock Market Line Graph')

# Upload the CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.write("Data Preview:")
    st.dataframe(df)

    # Check if required columns are present in the DataFrame
    if 'Date' in df.columns and 'Close' in df.columns:
        # Convert the 'Date' column to datetime format
        df['Date'] = pd.to_datetime(df['Date'])

        # Set 'Date' as the index of the DataFrame
        df.set_index('Date', inplace=True)

        # Plot the line graph
        st.write("Line Graph:")
        st.line_chart(df['Close'])

        # Optionally, plot using matplotlib for more customization
        st.write("Matplotlib Line Graph:")
        fig, ax = plt.subplots()
        ax.plot(df.index, df['Close'], label='Close Price')
        ax.set_xlabel('Date')
        ax.set_ylabel('Close Price')
        ax.set_title('Stock Market Close Price Over Time')
        ax.legend()

        st.pyplot(fig)
    else:
        st.write("The CSV file does not contain the required 'Date' and 'Close' columns.")

else:
    st.write("Please upload a CSV file.")
