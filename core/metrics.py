import numpy as np
from .config import GRAD_MIN, SIGMA_C_MIN, GRAD_0, SIGMA_0, X, C

def P_delta(grad_warp, sigma_c):
    """
    Oblicza prawdopodobieństwo przeskoku Δ w hipergrafie romionowym.
    Skalibrowane dla zjawisk takich jak FRB (δt ≈ 1 ms), meta-fotony (S=1, G=2, P=0)
    oraz meta-W/Z (S=1, G≥2, P≥4).
    """
    return (1 / (1 + np.exp(-(grad_warp - GRAD_MIN) / GRAD_0)) *
            1 / (1 + np.exp(-(sigma_c - SIGMA_C_MIN) / SIGMA_0)))

def calc_delta_t(grad_warp):
    """
    Oblicza opóźnienie czasowe δt (ms) dla przeskoków Δ.
    Skalibrowane dla odległości 1 Mpc, typowej dla FRB i meta-cząstek.
    """
    return grad_warp * X / C * 1e3

def assign_attrs(event_type):
    """Przypisuje atrybuty (S, G, P) dla zdarzeń."""
    if event_type == 'meta_foton':
        return {'S': 1, 'G': 2, 'P': 0}
    elif event_type == 'meta_WZ':
        return {'S': 1, 'G': 2, 'P': 4}
    return None
