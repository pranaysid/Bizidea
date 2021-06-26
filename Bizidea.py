import folium
import pandas as pd
import requests
import streamlit as st
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static

''' 
#  Welcome :pray:
'''
st.header('You can get a business idea by entering some details!')
main_place = st.text_input( 'Enter the name of the place where you would like to setup a business','Gachibowli')




df = pd.DataFrame({'Place': main_place},index=[0])
#Creating an instance of Nominatim Class
geolocator = Nominatim(user_agent="my_request")
#applying the rate limiter wrapper
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
#Applying the method to pandas DataFrame
df['location'] = df['Place'].apply(geocode)
df['Latitude'] = df['location'].apply(lambda x: x.latitude if x else None)
df['Longitude'] = df['location'].apply(lambda x: x.longitude if x else None)



a=df.iloc[0]['Latitude']
b=df.iloc[0]['Longitude']


#folium_static(main_map)
#st.write("<h2 style= 'text-align: center;font-weight: bold;color:#dcd0ff;'>Map of ",main_place,"</h1>", unsafe_allow_html=True)

# defining the Foursquare Credentials and Version
CLIENT_ID = '0SE0FIONCAABB1M1SFEIWJCQMYQJDUY1E2SKB0OJMOFL0PYQ'
CLIENT_SECRET = '2NQUJCYNY0USN2HLTIAINWLGH3MEKY5EM3EASFA31WT1EIYR'
VERSION = '20201409'

radius = 3500
LIMIT = 100

venues = []

for lat, long in zip(df['Latitude'], df['Longitude']):
    # creating the API request URL
    url = "https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}".format(
        CLIENT_ID,
        CLIENT_SECRET,
        VERSION,
        lat,
        long,
        radius, 
        LIMIT)
    
    # making the GET request

    results = requests.get(url).json()["response"]['groups'][0]['items']

for venue in results:
    venues.append((
            venue['venue']['name'], 
            venue['venue']['location']['lat'], 
            venue['venue']['location']['lng'],  
            venue['venue']['categories'][0]['name']))

venues_df = pd.DataFrame(venues)

# column names
venues_df.columns = [ 'VenueName', 'VenueLatitude', 'VenueLongitude', 'VenueCategory']
pd.set_option('display.max_rows', None)

map_1 = folium.Map(location=[a,b], zoom_start=13)


for lat, lng in zip(venues_df['VenueLatitude'],venues_df['VenueLongitude']):
    folium.CircleMarker(
        [lat, lng],
        radius=8,
        color='blue',
        fill=True,
        fill_color='#f77300',
        fill_opacity=0.7).add_to(map_1) 


# st.write("<h3 style= 'text-align: center;font-weight: bold;'>Cluster of Businesses located in ",main_place,"</h3>", unsafe_allow_html=True)

#---------
#---------
#---------
#---------
#---------
#---------
#---------

#enter another places names

str1 = str('Enter a neighbourhood with which you would like to compare with '+main_place) 
sur1 = st.text_input(str1,'Kukatpally')



df2 = pd.DataFrame({'Place': sur1},index=[0])
 
#Creating an instance of Nominatim Class
geolocator = Nominatim(user_agent="my_request")
 
#applying the rate limiter wrapper
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
 
#Applying the method to pandas DataFrame
df2['location'] = df2['Place'].apply(geocode)
df2['Latitude'] = df2['location'].apply(lambda x: x.latitude if x else None)
df2['Longitude'] = df2['location'].apply(lambda x: x.longitude if x else None)

c=df2.iloc[0]['Latitude']
d=df2.iloc[0]['Longitude']

radius = 3500
LIMIT = 100

venues2 = []

for lat, long in zip(df2['Latitude'], df2['Longitude']):
    # creating the API request URL
    url2 = "https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}".format(
        CLIENT_ID,
        CLIENT_SECRET,
        VERSION,
        lat,
        long,
        radius, 
        LIMIT)
    
    # making the GET request

    results2 = requests.get(url2).json()["response"]['groups'][0]['items']

for venue in results2:
    venues2.append((
        venue['venue']['name'], 
        venue['venue']['location']['lat'], 
        venue['venue']['location']['lng'],  
        venue['venue']['categories'][0]['name']))

# converting the venues list into a new DataFrame
venues2_df = pd.DataFrame(venues2)

# column names
venues2_df.columns = [ 'VenueName', 'VenueLatitude', 'VenueLongitude', 'VenueCategory']
pd.set_option('display.max_rows', None)

map_2 = folium.Map(location=[c,d], zoom_start=13)


for lat, lng in zip(venues2_df['VenueLatitude'],venues2_df['VenueLongitude']):
    folium.CircleMarker(
        [lat, lng],
        radius=8,
        color='blue',
        fill=True,
        fill_color='#f77300',
        fill_opacity=0.7).add_to(map_2)  
    


#---------
#---------
#---------
#---------
#---------
#---------
#---------


str2 = str('Enter another neighbourhood with which you would like to compare with '+main_place)
sur2 = st.text_input(str2,'Hitec City')

df3 = pd.DataFrame({'Place': sur2},index=[0])
 
#Creating an instance of Nominatim Class
geolocator = Nominatim(user_agent="my_request")
 
#applying the rate limiter wrapper
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
 
#Applying the method to pandas DataFrame
df3['location'] = df3['Place'].apply(geocode)
df3['Latitude'] = df3['location'].apply(lambda x: x.latitude if x else None)
df3['Longitude'] = df3['location'].apply(lambda x: x.longitude if x else None)

e=df3.iloc[0]['Latitude']
f=df3.iloc[0]['Longitude']

radius = 3500
LIMIT = 100

venues3 = []

for lat, long in zip(df3['Latitude'], df3['Longitude']):
    # creating the API request URL
    url3 = "https://api.foursquare.com/v2/venues/explore?client_id={}&client_secret={}&v={}&ll={},{}&radius={}&limit={}".format(
        CLIENT_ID,
        CLIENT_SECRET,
        VERSION,
        lat,
        long,
        radius, 
        LIMIT)
    
    # making the GET request

    results3 = requests.get(url3).json()["response"]['groups'][0]['items']
    

for venue in results3:
        venues3.append((
        venue['venue']['name'], 
        venue['venue']['location']['lat'], 
        venue['venue']['location']['lng'],  
        venue['venue']['categories'][0]['name']))

# converting the venues list into a new DataFrame
venues3_df = pd.DataFrame(venues3)

# column names
venues3_df.columns = [ 'VenueName', 'VenueLatitude', 'VenueLongitude', 'VenueCategory']
pd.set_option('display.max_rows', None)

map_3 = folium.Map(location=[e,f], zoom_start=13)


for lat, lng in zip(venues3_df['VenueLatitude'],venues3_df['VenueLongitude']):
    folium.CircleMarker(
        [lat, lng],
        radius=8,
        color='blue',
        fill=True,
        fill_color='#f77300',
        fill_opacity=0.7).add_to(map_3)  


#---------
#---------
#---------
#---------
#---------
#---------
#---------

st.write('Latitude and Longitude of **',main_place,'**are ',df.iloc[0]['Latitude'],'&',df.iloc[0]['Longitude'])
st.write('Latitude and Longitude of **',sur1,'**are ',df2.iloc[0]['Latitude'],'&',df2.iloc[0]['Longitude'])
st.write('Latitude and Longitude of **',sur2,'**are ',df3.iloc[0]['Latitude'],'&',df3.iloc[0]['Longitude'])


#---------
#---------
#---------
#---------
#---------
#---------
#---------

maps_1 = folium.Map(location=[a,b], zoom_start=11.5)
for i in range(0,1):
   folium.Marker(
      location=[a,b],
      popup=df3.iloc[i]['Place'],
      # icon = folium.Icon(icon='cloud',color='green')
   ).add_to(maps_1)

maps_2 = folium.Map(location=[c,d], zoom_start=11.5)
for i in range(0,1):
   folium.Marker(
      location=[c,d],
      popup=df3.iloc[i]['Place'],
      # icon = folium.Icon(icon='cloud',color='green')
   ).add_to(maps_2)

maps_3 = folium.Map(location=[e,f], zoom_start=11.5)
for i in range(0,1):
   folium.Marker(
      location=[e,f],
      popup=df3.iloc[i]['Place'],
      # icon = folium.Icon(icon='cloud',color='green')
   ).add_to(maps_3)


place_map = st.selectbox("",(main_place,sur1,sur2))

if place_map == main_place:
    folium_static(maps_1)
elif place_map == sur1:
    folium_static(maps_2)
else:
    folium_static(maps_3)

cluster_map = st.radio(
    "Select an area",
    (main_place,sur1,sur2))

if cluster_map == main_place:
    st.write("<h3 style= 'text-align: center;color: #F63366;font-family:courier;font-weight: bold;'>Cluster of Businesses located in ",main_place,"</h3>", unsafe_allow_html=True)
    folium_static(map_1)
elif cluster_map == sur1:
    st.write("<h3 style= 'text-align: center;color: #F63366;font-family:courier;font-weight: bold;'>Cluster of Businesses located in ",sur1,"</h3>", unsafe_allow_html=True)
    folium_static(map_2)
else:
    st.write("<h3 style= 'text-align: center;color: #F63366;font-family:courier;font-weight: bold;'>Cluster of Businesses located in ",sur2,"</h3>", unsafe_allow_html=True)
    folium_static(map_3)
    
option = st.selectbox("Which place's venues would you like to see",( main_place,sur1,sur2))


if option == main_place:
    st.dataframe(venues_df)
elif option == sur1:
    st.dataframe(venues2_df)
else:
    st.dataframe(venues3_df)

venues_category = venues_df.groupby(['VenueCategory']).size().sort_values(ascending=False)
venues2_category = venues2_df.groupby(['VenueCategory']).size().sort_values(ascending=False)
venues3_category = venues3_df.groupby(['VenueCategory']).size().sort_values(ascending=False)

# option = st.selectbox("Venues grouped by categories",('#', main_place,sur1,sur2))

# if option == '#':
#     st.write("-")
# elif option == main_place:
#     st.dataframe(venues_category)
# elif option == sur1:
#     st.dataframe(venues2_category)
# else:
#     st.dataframe(venues3_category)

col1, col2, col3 = st.beta_columns(3)

with col1:
    st.write("List of Venues at "+main_place)
    st.dataframe(venues_category)

with col2:
    st.write("List of Venues at "+sur1)
    st.dataframe(venues2_category)

with col3:
    st.write("List of Venues at "+sur2)
    st.dataframe(venues3_category)