from sqlalchemy.orm import sessionmaker
from projectorm import UserInput, Prediction
from sqlalchemy import create_engine
import streamlit as st# Streamliy

engine = create_engine('sqlite:///utkarsh.sqlite3')
Session = sessionmaker(bind = engine)
sess = Session()

st.title("Database with SQLalchemy")

area = st.number_input('Area', value = 400)
rooms = st.number_input('Number of rooms',max_value = 50,min_value = 1, value = 3)
age =  st.number_input("Age of house")
submit = st.button("Submit")

if submit :
    try :
        entry = UserInput(house_area = area, no_of_rooms = rooms, age = age, location = "LUCKNOW")
        sess.add(entry)#sess => database
        sess.commit()
        st.success("added to database")
    except Exception as e:
        st.error("hello Error")
        st.error(e)

if st.checkbox('view data') :
    result = sess.query(UserInput).all()
    for item in result :
        st.subheader(item.location)
        st.text(item.house_area)
        st.text(item.no_of_rooms)
        st.text(item.age)