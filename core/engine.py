import numpy as np
from .metrics import P_delta, calc_delta_t, assign_attrs
from .topology import update_hypergraph

def simulate_step(H, grad_warp, sigma_c, step):
    """Symuluje pojedynczy krok Δ."""
    p = P_delta(grad_warp, sigma_c)
    if np.random.rand() < p:
        delta_t = calc_delta_t(grad_warp)
        event_type = 'meta_foton' if p > 0.7 else 'meta_WZ'
        attrs = assign_attrs(event_type)
        H = update_hypergraph(H, attrs, step)
        return {'type': event_type, 'delta_t': delta_t, 'P_delta': p, 'attrs': attrs}
    return {'type': 'zapadnięcie', 'delta_t': 0, 'P_delta': p, 'attrs': None}
