import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My parents new healthy diner")
streamlit.header("Breakfast menu")
streamlit.text("🥣 🥗  🥑🍞")
streamlit.text( "🥣Omega 3 & Blueberry oatmeal")
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑🍞 All Veggie pickles and multigrain sandwitch')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.text(type(my_fruit_list))

#streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
# Display the table on the page.
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
    else:
        fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
        streamlit.write('The user entered ', fruit_choice)
        fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
        streamlit.text("advice about fruit:" + fruit_choice )
        streamlit.dataframe(fruityvice_normalized)
except URLError as e:
        streamlit.error()





# write your own comment -whaft does the next line do? 
# streamlit.text(fruityvice_normalized)
# write your own comment - what does this do?
#

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text(my_data_rows)
streamlit.text("The Fruit load list contains:")
streamlit.dataframe(my_data_rows)

#Allow the end user to add fruit.
my_fruit_list2 = my_data_rows
streamlit.text(type(my_fruit_list2))
streamlit.text(my_fruit_list2)
 

#add_my_fruit = streamlit.multiselect("what fruit would you like to add? ", list(my_fruit_list2.0), ['banana'])

my_cur.execute("insert into fruit_load_list values ('from streamlit')")


  
                                    
