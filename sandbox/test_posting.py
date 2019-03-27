from netwulf.tools import bind_positions_to_network
if __name__ == "__main__":
    import pprint 
    pp = pprint.PrettyPrinter(indent=4)

    G = nx.Graph()
    G.add_nodes_from(range(10))
    G.add_nodes_from("abcde")

    from netwulf import visualize
    props, config = visualize(G)

    pp.pprint(props)
    bind_positions_to_network(G, props)
    visualize(G, config=config)