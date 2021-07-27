from geopy.geocoders import Nominatim
import networkx as nx
import osmnx as ox
from geopy import Point
geolocator = Nominatim(user_agent="tutorial")
location = geolocator.reverse(Point("35.891822", "128.610749"))
# 대구광역시 북구 산격동 대학로 80

def

if __name__ == "__main__":
    n = "대구광역시 북구 산격동 대학로 80"
    app = Nominatim(user_agent='tutorial')
    location = app.geocode('{n}'.format(n=n))

    print(location.latitude, location.longitude)

    point = location.latitude,location.longitude
    G = ox.graph_from_point(point, network_type='drive', dist=1000)

    G_proj = ox.project_graph(G)
    intersections = ox.consolidate_intersections(G_proj, rebuild_graph=False, tolerance=15, dead_ends=False)

    G2 = ox.consolidate_intersections(G_proj, rebuild_graph=True, tolerance=15, dead_ends=False)
    print("Intersections: {}, G: {}, G2: {}".format(len(intersections), len(G), len(G2)))

    fig, ax = ox.plot_graph(G, node_color='r',figsize=(20,20))
    fig, ax = ox.plot_graph(G2, node_color='b')

