import folium
import pandas as pd
import numpy as np
import requests
import streamlit as st
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from streamlit_folium import folium_static
import random

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
        radius=5,
        color='#006080',
        fill=True,
        fill_color='#80dfff',
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
        radius=5,
        color='#006080',
        fill=True,
        fill_color='#80dfff',
        fill_opacity=0.99).add_to(map_2)  
    


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
        color='#006080',
        fill=True,
        fill_color='#80dfff',
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


# place_map = st.selectbox("",(main_place,sur1,sur2))

# if place_map == main_place:
#     folium_static(maps_1)
# elif place_map == sur1:
#     folium_static(maps_2)
# else:
#     folium_static(maps_3)

# cluster_map = st.radio(
#     "Select an area",
#     (main_place,sur1,sur2))

# if cluster_map == main_place:
#     st.write("<h3 style= 'text-align: center;color: #F63366;font-family:courier;font-weight: bold;'>Cluster of Businesses located in ",main_place,"</h3>", unsafe_allow_html=True)
#     folium_static(map_1)

# elif cluster_map == sur1:
#     st.write("<h3 style= 'text-align: center;color: #F63366;font-family:courier;font-weight: bold;'>Cluster of Businesses located in ",sur1,"</h3>", unsafe_allow_html=True)
#     folium_static(map_2)
# else:
#     st.write("<h3 style= 'text-align: center;color: #F63366;font-family:courier;font-weight: bold;'>Cluster of Businesses located in ",sur2,"</h3>", unsafe_allow_html=True)
#     folium_static(map_3)

venues_df.index = np.arange(1,len(venues_df)+1)
venues2_df.index = np.arange(1,len(venues2_df)+1)
venues3_df.index = np.arange(1,len(venues3_df)+1)
    
# option = st.selectbox("Which place's venues would you like to see?",( main_place,sur1,sur2))


# if option == main_place:
#     st.dataframe(venues_df)
# elif option == sur1:
#     st.dataframe(venues2_df)
# else:
#     st.dataframe(venues3_df)

# venues_category = pd.DataFrame(columns = ['Categories', 'Count'] )
# venues2_category = pd.DataFrame(columns = ['Categories', 'Count'] )
# venues3_category = pd.DataFrame(columns = ['Categories', 'Count'] )


v_cat=venues_df.groupby(['VenueCategory'])['VenueCategory'].count().sort_values(ascending=False)
v_cate = pd.DataFrame(dict(Categories=v_cat.index, Aggregate=v_cat.values))
v_cate.index = np.arange(1,len(v_cate)+1)


v2_cat=venues2_df.groupby(['VenueCategory'])['VenueCategory'].count().sort_values(ascending=False)
v2_cate = pd.DataFrame(dict(Categories=v2_cat.index, Aggregate=v2_cat.values))
v2_cate.index = np.arange(1,len(v2_cate)+1)


v3_cat=venues3_df.groupby(['VenueCategory'])['VenueCategory'].count().sort_values(ascending=False)
v3_cate = pd.DataFrame(dict(Categories=v3_cat.index, Aggregate=v3_cat.values))
v2_cate.index = np.arange(1,len(v2_cate)+1)




# venues_category = venues_df.groupby(['VenueCategory']).size().sort_values(ascending=False)
# venues2_category = venues2_df.groupby(['VenueCategory']).size().sort_values(ascending=False)
# venues3_category = venues3_df.groupby(['VenueCategory']).size().sort_values(ascending=False)

# option = st.selectbox("Venues grouped by categories",('#', main_place,sur1,sur2))

# if option == '#':
#     st.write("-")
# elif option == main_place:
#     st.dataframe(venues_category)
# elif option == sur1:
#     st.dataframe(venues2_category)
# else:
#     st.dataframe(venues3_category)

# col1, col2, col3 = st.beta_columns(3)

# with col1:
#     st.write("List of Venues at "+main_place)
#     st.dataframe(v_cate)

# with col2:
#     st.write("List of Venues at "+sur1)
#     st.dataframe(v2_cate)

# with col3:
#     st.write("List of Venues at "+sur2)
#     st.dataframe(v3_cate)



two_three_merge = v2_cate.merge(v3_cate,how='outer',sort='False')



two_three_draft = pd.DataFrame(columns=['Categories'])
two_three_draft= two_three_merge[['Categories']].drop_duplicates(keep=False)
two_three = two_three_draft[['Categories']].reset_index(drop=True)
two_three.index = np.arange(1,len(two_three)+1)
# st.dataframe(two_three)


just_1 = pd.DataFrame(columns=['Categories'])
just_1 = v_cate[['Categories']]
just_one = just_1.sort_values('Categories',ascending= True)
just_one.index = np.arange(1,len(just_one)+1)
# st.dataframe(just_one)

sub =pd.concat([two_three, just_one, just_one]).drop_duplicates(keep=False)
sub.index = np.arange(1,len(sub)+1)

final_list = sub['Categories'].tolist()

rand = random.randint(2,3)
UpdatedList = random.sample(final_list, 2)


# st.write("<h2 style= 'text-align: center;color: #F63366;font-family: 'Titillium Bold';font-weight: bold;'>Bizidea suggests you the following ideas!</h2>", unsafe_allow_html=True)
# st.write("<h3 style= 'text-align: center;font-family: 'Andale Mono';font-weight: bold;'>",UpdatedList[0],"</h3>", unsafe_allow_html=True)
# st.write("<h3 style= 'text-align: center;font-family: 'Andale Mono';font-weight: bold;'>",UpdatedList[1],"</h3>", unsafe_allow_html=True)


side_box = st.sidebar.selectbox("Which of the following would you like to look at?",("Bizidea","Cluster of Businesses","Area Location", "Venues at a location", "List of Venues"))

if side_box == "Area Location":
    place_map = st.selectbox("",(main_place,sur1,sur2))
    if place_map == main_place:
        folium_static(maps_1)
    elif place_map == sur1:
        folium_static(maps_2)
    else:
        folium_static(maps_3)
elif side_box == "Venues at a location":
    option = st.selectbox("Which place's venues would you like to see?",( main_place,sur1,sur2))
    if option == main_place:
        st.dataframe(venues_df)
    elif option == sur1:
        st.dataframe(venues2_df)
    else:
        st.dataframe(venues3_df)
elif side_box == "List of Venues":
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        st.write("List of Venues at "+main_place)
        st.dataframe(v_cate)
    with col2:
        st.write("List of Venues at "+sur1)
        st.dataframe(v2_cate)
    with col3:
        st.write("List of Venues at "+sur2)
        st.dataframe(v3_cate)
elif side_box == "Cluster of Businesses":
    cluster_map = st.radio("Select an area",(main_place,sur1,sur2))
    if cluster_map == main_place:
        st.write("<h3 style= 'text-align: center;color: #4DA8DA;font-family: 'Terminal Dosis';font-weight: bold;'>Cluster of Businesses found in ",main_place,"</h3>", unsafe_allow_html=True)
        folium_static(map_1)
    elif cluster_map == sur1:
        st.write("<h3 style= 'text-align: center;color: #4DA8DA;font-family: 'Terminal Dosis';font-weight: bold;'>Cluster of Businesses found in ",sur1,"</h3>", unsafe_allow_html=True)
        folium_static(map_2)
    else:
        st.write("<h3 style= 'text-align: center;color: #4DA8DA;font-family: 'Terminal Dosis';font-weight: bold;'>Cluster of Businesses found in ",sur2,"</h3>", unsafe_allow_html=True)
        folium_static(map_3)
elif side_box == "Bizidea":
    st.write("<h2 style= 'text-align: center;color: #F63366;font-family: 'Titillium Bold';font-weight: bold;'>Bizidea suggests you the following ideas!</h2>", unsafe_allow_html=True)
    st.write("<h3 style= 'text-align: center;font-family: 'Andale Mono';font-weight: bold;'>",UpdatedList[0],"</h3>", unsafe_allow_html=True)
    st.write("<h3 style= 'text-align: center;font-family: 'Andale Mono';font-weight: bold;'>",UpdatedList[1],"</h3>", unsafe_allow_html=True)