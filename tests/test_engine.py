import pytest
from core.engine import simulate_step
from core.topology import create_hypergraph

def test_simulate_step_valid():
    H = create_hypergraph(n_vertices=10, n_edges=2)
    result = simulate_step(H, 1.2e-17, 2.0, 0, seed=42)
    assert result['type'] in ['meta_foton', 'meta_WZ', 'zapadnięcie']
