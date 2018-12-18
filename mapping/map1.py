import folium
import pandas
map = folium.Map(location=[32.318230, -86.902298],zoom_start=6,tiles="Mapbox Bright")

data = pandas.read_csv("Volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])

def color_mapper(elevation):
    if(elevation < 1000):
        color='green'
    elif(1000<= elevation < 3000):
        color='orange'
    else:
        color='red'
    return color

html = """<h4>Volcano information:</h4>
Height: %s m
"""

fg = folium.FeatureGroup(name="My map1")
for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt,ln],popup=folium.Popup(iframe), tooltip=folium.Tooltip(text=str(el) + " M"),
    icon=folium.Icon(color=color_mapper(el))))
map.add_child(fg)

map.save("Map1.html")
