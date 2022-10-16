import networkx as nx
import matplotlib.pyplot as plt
from classes.bfs import BfsTraverser
G = nx.Graph()
nodes=["Karen","J6","Gitaru","J1","J4","J7"]
G.add_nodes_from(nodes)
G.nodes()#confirm nodes
#Add Edges and their weights
G.add_edge("Karen","J1",weight="2.8")
G.add_edge("Karen","J6",weight="4")
G.add_edge("J1","J4",weight="2.6")
G.add_edge("J6","Gitaru",weight="10")
G.add_edge("J6","J7",weight="6")
G.add_edge("J6","J4",weight="6")
G.add_edge("Gitaru","J7",weight="6")
#position the nodes to resemble Nairobis map
G.nodes["Karen"]['pos']=(0,0)
G.nodes["J6"]['pos']=(0,2)
G.nodes["J1"]['pos']=(2,-2)
G.nodes["J4"]['pos']=(4,-2)
G.nodes["J7"]['pos']=(0,4)
G.nodes["Gitaru"]['pos']=(-1,3)
#store all positions in a variable
node_pos = nx.get_node_attributes(G,'pos')
#call BFS to return set of all possible routes to the goal
route_bfs = BfsTraverser()
routes = route_bfs.BFS(G,"Karen","Gitaru")
print(route_bfs.visited)
route_list = route_bfs.visited
#color the nodes in the route_bfs
node_col = ['darkturquoise' if not node in route_list else 'peru' for node in G.nodes()]
peru_colored_edges = list(zip(route_list,route_list[1:]))
#color the edges as well
#print(peru_colored_edges)
edge_col = ['darkturquoise' if not edge in peru_colored_edges else 'peru' for edge in G.edges()]
arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos,node_color= node_col, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2,edge_color= edge_col)
#nx.draw_networkx_edge_labels(G, node_pos,edge_color= edge_col, edge_labels=arc_weight)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
