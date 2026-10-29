import streamlit as st

import app_py

st.title('STREAMLIT DATABASE UI')

option = st.sidebar.selectbox('Select Your Option: ',
                    ('SELECT ALL RECORDS',
                     'SELECT RECORD BY ID',
                     'INSERT RECORD',
                     'DELETE RECORD BY ID',
                     'UPDATE RECORD BY ID'))

if option == 'SELECT ALL RECORDS':
    if st.button('SHOW DATA'):
        result = app_py.select_all_records()
        st.write(tuple(result))
elif option == 'SELECT RECORD BY ID':
    id = st.number_input("Enter movie ID: ")
    if st.button('SHOW DATA'):
        result = app_py.select_record_by_id(id)
        st.write(result)
elif option == 'INSERT RECORD':
    title = st.text_input("Enter movie title: ")
    country = st.text_input("Enter the country that made the movie: ")
    year = st.text_input("Enter movie release year: ")
    imdb_rate = st.number_input("Enter movie IMDB rate: ", min_value=0.0, max_value=10.0, step=0.1)
    if st.button('INSERT DATA'):
        app_py.insert_record(title, country, year, imdb_rate)
        st.write("Done!")
elif option == 'UPDATE RECORD BY ID':
    id = st.number_input("Enter movie ID: ")
    year = st.text_input("Update movie release year: ")
    imdb_rate = st.number_input("Update movie IMDB rate: ", min_value=0.0, max_value=10.0, step=0.1)
    if st.button('UPDATE DATA'):
        app_py.update_record_by_id(id, imdb_rate, year)
        st.write("Done!")
elif option == 'DELETE RECORD BY ID':
    id = st.number_input("Enter movie ID: ")
    if st.button('DELETE DATA'):
        app_py.delete_record_by_id(id)
        st.write("Done!")