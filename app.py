import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''
def on_submit(date, time, p_lat, p_lon, d_lon, d_lat, pass_count):
    print(date)
    print(time)
    dt = '2012-10-06 12:10:20'
    r = requests.get(f'https://taxifare.lewagon.ai/predict?pickup_datetime={dt}&pickup_longitude={p_lon}&pickup_latitude={p_lat}&dropoff_longitude={d_lon}&dropoff_latitude={d_lat}&passenger_count={pass_count}')
    print(r)
    result = r.json()['fare']
    st.text(f'Your Fare will be {result}')
    
with st.form(key='my_form'):
	date = st.date_input(label='date')
	time = st.time_input(label='time')
	p_lat = st.text_input(label='pickup latitude')
	p_lon = st.text_input(label='pickup longitude')
	d_lon = st.text_input(label='dropoff longitude')
	d_lat = st.text_input(label='dropoff latitude')
	pass_count = st.select_slider(label='passenger count', options=range(1,11), value=1)    
	submit_button = st.form_submit_button(label='Submit', on_click=on_submit(date, time, p_lat, p_lon, d_lon, d_lat, pass_count))
 
           # inputs = {pickup_datetime: datetime,  # 2013-07-06 17:18:00
            #pickup_longitude: float,    # -73.950655
           # p#ickup_latitude: float,     # 40.783282
           # dr#opoff_longitude: float,   # -73.984365
           # dropoff_latitude: float,    # 40.769802
           # passenger_count: int}
 
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''