from core.engine import simulate_step
from core.topology import create_hypergraph
from io.exporter import export_results
from io.logger import log_event

def run_simulation(grad_warp, sigma_c, n_steps=100):
    """Główna pętla symulacyjna."""
    H = create_hypergraph()
    results = []
    for step in range(n_steps):
        result = simulate_step(H, grad_warp, sigma_c, step)
        log_event(result)
        results.append(result)
    df = export_results(results)
    print(f"Średnie δt: {df['delta_t'].mean():.3f} ms")
    print(f"Średnie P(Δ): {df['P_delta'].mean():.3f}")
    return df
