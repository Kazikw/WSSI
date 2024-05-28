import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


class Neuron:
    def __init__(self, n_inputs):
        self.weights = np.random.randn(n_inputs)
        self.bias = np.random.randn()

    def forward(self, inputs):
        return np.dot(inputs, self.weights) + self.bias

    def activate(self, z):
        return 1 / (1 + np.exp(-z))

    def __call__(self, inputs):
        z = self.forward(inputs)
        return self.activate(z)


class NeuralNetwork:
    def __init__(self, layers):
        self.layers = []
        for i in range(1, len(layers)):
            layer = [Neuron(layers[i - 1]) for _ in range(layers[i])]
            self.layers.append(layer)

    def forward(self, x):
        for layer in self.layers:
            x = np.array([neuron(x) for neuron in layer])
        return x


def visualize_network_structure(layers):
    G = nx.DiGraph()
    pos = {}
    layer_nodes = []

    for i, n_neurons in enumerate(layers):
        layer = []
        for j in range(n_neurons):
            node = f"L{i}N{j}"
            layer.append(node)
            G.add_node(node, layer=i)
        layer_nodes.append(layer)

    for i in range(len(layers) - 1):
        for node1 in layer_nodes[i]:
            for node2 in layer_nodes[i + 1]:
                G.add_edge(node1, node2)

    for i, layer in enumerate(layer_nodes):
        for j, node in enumerate(layer):
            pos[node] = (i, -j)

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_size=5000, node_color='lightblue', font_size=10, font_weight='bold',
            arrowsize=20)
    plt.show()


layers = [3, 4, 4, 1]


network = NeuralNetwork(layers)

visualize_network_structure(layers)
