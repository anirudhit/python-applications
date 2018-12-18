import folium
import pandas

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
map = folium.Map(location=[32.318230, -86.902298],zoom_start=6,tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

html = """<h4>Volcano information:</h4>
Height: %s m
"""

for lt, ln, el in zip(lat, lon, elev):
    iframe = folium.IFrame(html=html % str(el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius = 6, popup=folium.Popup(iframe), tooltip=folium.Tooltip(text=str(el) + " M"),
    fill_color=color_mapper(el), color = 'grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map5.html")
