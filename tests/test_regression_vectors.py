import json
import pytest
from core.topology import create_hypergraph
from core.engine import simulate_step

# Wczytaj dane testowe z pliku JSON
with open('data/test_vectors.json', 'r') as f:
    TEST_VECTORS = json.load(f)

@pytest.mark.parametrize("test_case", TEST_VECTORS)
def test_event_type_matches_expected(test_case):
    grad_warp = test_case["grad_warp"]
    sigma_c = test_case["sigma_c"]
    expected_type = test_case["event_type"]
    
    # Ustawienie stałego seeda dla powtarzalności
    H = create_hypergraph(n_vertices=100, n_edges=2)
    result, _ = simulate_step(H, grad_warp, sigma_c, step=0, seed=42)

    assert result["type"] == expected_type, (
        f"Błąd regresji: dla grad_warp={grad_warp}, sigma_c={sigma_c} "
        f"oczekiwano '{expected_type}', otrzymano '{result['type']}'"
    )
