import streamlit as st
import pandas as pd 
from PIL import Image

st.write("""#stock app which shows **Visually data**""")

image = Image.open("C:/Users/NAWIN/Desktop/NiroshProjects/projects/python/stockapp/stockimg.jpg")
st.image(image,use_column_width=True)

st.sidebar.header('User Input')

def get_input():
    start_date = st.sidebar.text_input("Start Date","2014-01-02")
    end_date = st.sidebar.text_input("End Date","2014-08-04")
    stock_symbol = st.sidebar.text_input("Stock","amzn")
    return start_date, end_date,stock_symbol

def get_company(symbol):
    if symbol == 'amzn':
        return 'Amazon'
    elif symbol == 'fb':
        return 'Facebook'
    elif symbol == 'google':
        return 'Google'
    else:
        'none'

def get_data(symbol,start,end):

    if symbol == 'amzn':
        df = pd.read_csv("C:/Users/NAWIN/Desktop/NiroshProjects/projects/python/stockapp/stocks/AMZN.csv")
    elif symbol == 'fb':
        df = pd.read_csv("C:/Users/NAWIN/Desktop/NiroshProjects/projects/python/stockapp/stocks/FB.csv")
    elif symbol == 'google':
        df = pd.read_csv("C:/Users/NAWIN/Desktop/NiroshProjects/projects/python/stockapp/stocks/google.csv")
    else:
        df = pd.DataFrame(columns = ['Date','Close','Open','Volume','Adj Close','High','Low'])

    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    start_row = 0
    end_row = 0

    for i in range(0,len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break


    for j in range(0,len(df)):
        if end >= pd.to_datetime(df['Date'][len(df)-1-j]):
            end_row = len(df) -1 -j
            break

    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row +1, :]

start,end,symbol = get_input()

df = get_data(symbol,start,end)

company_name = get_company(symbol)

st.header(company_name + "Close price\n")
st.line_chart(df['Close'])

st.header(company_name + "Vloume\n")
st.line_chart(df['Volume'])

st.header('Data Statics')
st.write(df.describe())


