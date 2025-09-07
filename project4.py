import streamlit as st
import pandas as pd

data = pd.read_csv("most-popular_updated_15_feb.csv")

df_full = pd.DataFrame(data)

df_20 = df_full.loc[0:19]
print(df_20)

df = data[['show_title', 'hours_viewed_first_28_days']].head(20)

st.subheader("Biểu đồ cột: Giờ xem trong 28 ngày đầu")
st.bar_chart(df, x="show_title", y="hours_viewed_first_28_days")
