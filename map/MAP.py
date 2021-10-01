import folium
import pandas
df = pandas.read_csv('Volcanoes.txt')

map = folium.Map(location=(40,-100),zoom_start= 5)

html = """
<h3>Volcano name:<br></h3>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
def choose_color(m):
    if m < 1000:
        return 'green'
    elif m<= 3000:
        return 'orange'
    else:
        return 'red'
    
fgv = folium.FeatureGroup(name= 'Volcanoes')

for lt,ln,el,name in zip(df['LAT'],df['LON'],df['ELEV'],df['NAME']):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], popup=folium.Popup(iframe),radius=7,color ='grey', fill_color=choose_color(el), fill_opacity = 0.7))
    
fgp = folium.FeatureGroup(name= 'Population')

fgp.add_child(folium.GeoJson(data = open( 'world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 else 'orange' 
if 10000000 <= x['properties']['POP2005'] <= 20000000 else 'red' }))

      
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())  
map.save('map1.html')
