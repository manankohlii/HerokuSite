import folium
import pandas
map = folium.Map(loaction=[28.736714, 77.087617],tiles="Stamen Terrain",zoom_start=60)
fg = folium.FeatureGroup(name="My Map")

#fg.add_child(folium.GeoJson(data=(open('world.json','r', encoding='utf-8-sig').read()))
#check videos for polygons and color on the basis of population
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lan = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation<1000:
        return 'green'
    elif elevation<3000 and elevation>1000:
        return 'orange'
    else :
        return 'red'

for lt, ln, elev in zip(lat,lan,elev):
    fg.add_child(folium.Marker(location=[lt, ln],popup=elev,color=color_producer(elev)))


map.add_child(fg)
map.save("map2.html")
