import folium

""" map_osm = folium.Map(location=[37.579577,126.977252])
map_osm.save('./map1.html') """

""" map_osm = folium.Map(location=[37.579577,126.977252],zoom_start=18)
map_osm.save('./map2.html') """

""" map_osm = folium.Map(location=[37.579577,126.977252],zoom_start=18,tiles='Stamen Terrain')
map_osm.save('./map3.html') """


map_osm = folium.Map(location=[37.579577,126.977252],zoom_start=18)
folium.Marker(location=[37.579577,126.977252]
              ,tooltip='세종문화회관'
              ,icon=folium.Icon(color='red',icon='info-sign')).add_to(map_osm)
folium.CircleMarker(location=[37.578099,126.976881]
                    ,tooltip='광화문'
                    ,radius='100'
                    ,color='red'
                    ,fill_color='yellow').add_to(map_osm)
                    
map_osm.save('./map5.html')
