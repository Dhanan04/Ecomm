import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def main():
    st.title("This is my App for Business that i own")
    st.sidebar.title("Upload you file here")
    
    uploaded_file = st.sidebar.file_uploader("Upload your file" , type = ['csv' , 'xlsx'])
    
    
    
    if uploaded_file is not None:
        try :
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else :
                data = pd.read_excel(uploaded_file)
                
                st.sidebar.success("file Uploaded Succesfully")
                
                st.subheader("data Overaview")
                st.dataframe(data.head())
                
                
                
                st.subheader("Basic information of Dataset")
                st.write("Shape of the data", data.shape)
                st.write("Columns in data" , data.columns)
                st.write("Missing values" , data.isnull().sum())
                
                
                st.subheader("I will Show you the Stats of Data")
                st.write(data.describe())
                
        except Exception as e:
            print("It will handle if things go wrong", e)
    else :
        pass            
                
if __name__ == "__main__":
    main()
    
