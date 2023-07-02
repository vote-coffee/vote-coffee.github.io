import folium

m = folium.Map()

# import the library
import folium

# Make an empty map
m = folium.Map(location=[0,19], tiles="OpenStreetMap", zoom_start=2.75)

# Show the map
m
# Import the pandas library
import pandas as pd



# Make a data frame with dots to show on the map
df = pd.read_csv('~/Documents/Vote/Transparency Report 2022 first spreadsheet - Pivot Table 1.csv', encoding='UTF-8')
data = pd.DataFrame({
   'lon':[125.393055, -90.762839, -45.540274, -75.551688, -71.924204, 36.589861, -84.052937, 29.482266, 39.000000, 37.08333, 36.95795, 37.389356, 29.188545, -76.116591, -9.454314, -78.914057, 36.471495, -96.942033, -75.71612, -44.911213, -96.766797, 38.892622, 29.027759, 34.565438, -75.523132, 99.387648],
   'lat':[-8.934299, 14.562289, -21.350519, 3.179585, -13.51131, 7.870844, 9.750881, -2.905747, 8.000000, 9.81667, -0.490283, -0.446917, -2.249763, 1.766878, 8.496109, -5.64950, 7.795951, 19.253614, 3.225101, -20.938166, 18.272414, 5.758985, -1.696206, 0.792869, 5.034336, 22.241308],
   'name':['Atsabe: 17kg @ 11,70€/kg', 'Bella Vista: 176kg @ 10,40€/kg', 'Cafeina: 11400kg @ 5,29€', 'Hernan Montano: 997kg @ 10,57€/kg: ', 'Hugo Mariño: 30kg @ 32,20€/kg', 'Hunda Oli: 720kg @ 6,21€/kg', 'Idaly Calderon: 134kg @ 14,47€/kg', 'Izuba: 540kg @ 9€/kg', 'Jabanto Group: 1145kg @ 9,90€/kg', 'Jiratamo: 2023kg @ 5,70€/kg', 'Kiandu: 90kg @ 12,70kg', 'Kii: 120kg @ 12,90€/kg', 'Kilimbi: 120kg @ 10,70€/kg', 'Luis Alberto: 264kg @ 11,50€/kg', 'Macenta Beans: 460kg @ 8,50€/kg', 'Maribel Herrera: 207kg @ 9,10€/kg', 'Mustefa Abakeno: 960kg @ 9,70€/kg', 'Ombligo de Luna: 70kg @ 9,90€/kg', 'Passiflora: 681kg @ 8,20€/kg', 'Sancoffee: 1738kg @ 6,30€/kg', 'Sierra Mazateca: 205kg @ 7,40€/kg', 'Sookoo Group: 2172kg @ 11,30€/kg', 'SOPACDI: 120kg @ 8,90€/kg', 'Kikai: 88kg @ 11,80€/kg', 'Villamaria: 196kg @ 10,50€/kg', 'Xingang: 50kg @13€/kg'],
   'value':[0.5, 0.5, 3.8, 1.1, 0.2, 1, 0.44, 0.96, 1.2, 1.61, 0.36, 0.4, 0.4, 0.6, 0.78, 0.54, 1.1, 0.31, 0.94, 1.49, 0.54, 1.65, 0.4, 0.36, 0.5, 0.25]

}, dtype=str)

# want to add colour scale https://stackoverflow.com/questions/37466683/create-a-legend-on-a-folium-map
data
# add marker one by one on the map

for i in range(0,len(data)):
   folium.CircleMarker(
      location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
      popup=data.iloc[i]['name'],
      radius=float(data.iloc[i]['value'])*20,
      color='darkgreen',
      fill=True,
      fill_color='mediumseagreen'
   ).add_to(m)

# Show the map again
m

m.save("footprint.html")




