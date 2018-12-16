import folium
map = folium.Map(location=[32.318230, -86.902298],zoom_start=6,tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My map1")
fg.add_child(folium.Marker(location=[32.2, -86.5],popup="This is  a marker", tooltip=folium.Tooltip(text='Marker tooltip'), icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")
