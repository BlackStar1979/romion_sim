import hypernetx as hnx
import numpy as np

def create_hypergraph(n_vertices=1000000, n_edges=100):
    """Tworzy hipergraf H = (V, E, Δ, μ)."""
    V = range(n_vertices)
    E = {f'e{i}': list(np.random.choice(V, size=3, replace=False)) for i in range(n_edges)}
    return hnx.Hypergraph(E)

def update_hypergraph(H, delta_attrs, step):
    """Aktualizuje hipergraf po przeskoku Δ."""
    if delta_attrs:
        new_edge = {f'e{step}': list(np.random.choice(range(H.size()), size=3))}
        H.add_edge(new_edge)
    return H
