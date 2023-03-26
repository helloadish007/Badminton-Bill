#Author : ADISH007

import streamlit as st
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


st.header('Badminton Billing')

st.image("https://www.kpu.ca/sites/default/files/Recreation/badminton-league.jpg",width=300, use_column_width=300)


st.markdown("""
<style>div[data-testid="stToolbar"] { display: none;}</style>
""", unsafe_allow_html=True)

with st.sidebar.expander("Tool info: "):
     st.write("""
         helps in bill estimation
     """,width=10,use_column_width=20)
     st.text('Creator : ADISH007')
     url = "https://docs.google.com/spreadsheets/d/1XHp-EJqBmmMibz6Dq1xxwF1MqCDP0J9D8i7-I1bAYp8/edit#gid=0"
     st.write("check out this [link](%s)" % url)
     st.markdown("check out this [link](%s)" % url)
     st.sidebar.image("https://images.indianexpress.com/2022/07/Badminton-4-1.jpg")


total = st.text_input('Total Cost:  ', '')
hours = st.slider('Number of hours played', 1, 3, 2)
player_count=[]

#['Aneesh', 'Adish', 'Babin', 'Abimon','Gans','Bala','Abhilash','Venkat','Sandeep','Manoj','Uday','Vijo','Toby','Dileep Boy Reddy','Amit']
#['Aneesh', 'Babin', 'Abimon','Abhilash','Toby','Bala','Amit','Manoj']

if hours==1:
    players1 = st.multiselect(
    'Who all played ? ',
    ['Adish','Vasu bro','Ashik bro','Vaisakh','Bala','Karthik','Reymon','Abhishek','Anandu','Manikantan','Aneesh','Bharath','Unni','Vichu','Navneeth','Navneeth K','Rahul'],
    ['Adish','Vasu bro','Bala','Karthik','Reymon','Abhishek','Anandu'])
    player_count.append(len(players1))

elif hours==2:
    players1 = st.multiselect(
    'Who all played in 1st hour? ',
    ['Adish','Vasu bro','Ashik bro','Vaisakh','Bala','Karthik','Reymon','Abhishek','Anandu','Manikantan','Aneesh','Bharath','Unni','Vichu','Navneeth','Navneeth K','Rahul'],
    ['Adish','Vasu bro','Bala','Karthik','Reymon','Abhishek','Anandu'])

    players2 = st.multiselect(
    'Who all played in 2nd hour? ',
    ['Adish','Vasu bro','Ashik bro','Vaisakh','Bala','Karthik','Reymon','Abhishek','Anandu','Manikantan','Aneesh','Bharath','Unni','Vichu','Navneeth','Navneeth K','Rahul'],
    ['Adish','Vasu bro','Bala','Karthik','Reymon','Abhishek','Anandu'])

    player_count.append(len(players1))
    player_count.append(len(players2))

elif hours==3:
    players1 = st.multiselect(
    'Who all played in 1st hour? ',
    ['Adish','Vasu bro','Ashik bro','Vaisakh','Bala','Karthik','Reymon','Abhishek','Anandu','Manikantan','Aneesh','Bharath','Unni','Vichu','Navneeth','Navneeth K','Rahul'],
    ['Adish','Vasu bro','Bala','Karthik','Reymon','Abhishek','Anandu'])

    players2 = st.multiselect(
    'Who all played in 2nd hour? ',
    ['Adish','Vasu bro','Ashik bro','Vaisakh','Bala','Karthik','Reymon','Abhishek','Anandu','Manikantan','Aneesh','Bharath','Unni','Vichu','Navneeth','Navneeth K','Rahul'],
    ['Adish','Vasu bro','Bala','Karthik','Reymon','Abhishek','Anandu'])

    players3 = st.multiselect(
    'Who all played in 3rd hour? ',
    ['Adish','Vasu bro','Ashik bro','Vaisakh','Bala','Karthik','Reymon','Abhishek','Anandu','Manikantan','Aneesh','Bharath','Unni','Vichu','Navneeth','Navneeth K','Rahul'],
    ['Adish','Vasu bro','Bala','Karthik','Reymon','Abhishek','Anandu'])

    player_count.append(len(players1))
    player_count.append(len(players2))
    player_count.append(len(players3))


    
st.header(" Bill Generated : ")
players_combine=[]
if total:
    Cost_per_hour=int(total)/int(hours)
    if len(player_count)==1:
        cost_incurred1=Cost_per_hour/player_count[0]
        for i in players1:
            st.write(i,': Rs ',cost_incurred1)
    if len(player_count)==2:
        cost_incurred1=Cost_per_hour/player_count[0]
        cost_incurred2=Cost_per_hour/player_count[1]
        players_combine.extend(players1)
        players_combine.extend(players2)
        
        for i in set(players_combine):
            if players_combine.count(i)==1:
                s=0
                if i in players1:
                    s+=cost_incurred1
                elif i in players2:
                    s+=cost_incurred2
                st.write(i,": Rs ",s)
            elif players_combine.count(i)==2:
                st.write(i,": Rs ",cost_incurred1+cost_incurred2)
    if len(player_count)==3:
        cost_incurred1=Cost_per_hour/player_count[0]
        cost_incurred2=Cost_per_hour/player_count[1]
        cost_incurred3=Cost_per_hour/player_count[2]
        players_combine.extend(players1)
        players_combine.extend(players2)
        players_combine.extend(players3)
        
        for i in set(players_combine):
            if players_combine.count(i)==2:
                s=0
                if i in players1:
                    s+=cost_incurred1
                elif i in players2:
                    s+=cost_incurred2
                elif i in players3:
                    s+cost_incurred3
                st.write(i,": Rs ",s)
            elif players_combine.count(i)==3:
                st.write(i,": Rs ",cost_incurred1+cost_incurred2+cost_incurred3)
            elif players_combine.count(i)==1:
                ss=0
                if i in players1:
                    ss=cost_incurred1
                elif i in players2:
                    ss=cost_incurred2
                elif i in players3:
                    ss=cost_incurred3
                st.write(i,": Rs ",ss)



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)


