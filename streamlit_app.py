import streamlit
streamlit.title("My parents new healthy diner")
streamlit.header("Breakfast menu")
streamlit.text("🥣 🥗  🥑🍞")
streamlit.text( "🥣Omega 3 & Blueberry oatmeal")
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 All Veggie pickles and multigrain sandwitch')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
