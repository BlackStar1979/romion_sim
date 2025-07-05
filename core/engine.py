import numpy as np
from .metrics import P_delta, calc_delta_t, assign_attrs
from .topology import update_hypergraph

def simulate_step(H, grad_warp, sigma_c, step, seed=None):
    if seed is not None:
        np.random.seed(seed)
    """
    Symuluje pojedynczy krok Δ w hipergrafie romionowym.
    Args:
        H (hnx.Hypergraph): Hipergraf do aktualizacji.
        grad_warp (float): Gradient presji warp [m^-1].
        sigma_c (float): Entropia topologiczna.
        step (int): Numer kroku symulacji.
        seed (int, optional): Nasiono losowości dla powtarzalności.
    Returns:
        dict: Zdarzenie z kluczami 'type' (str), 'delta_t' (float), 'P_delta' (float), 'attrs' (dict or None).
    Raises:
        ValueError: Jeśli wejścia są niepoprawne.
    """
    if not isinstance(grad_warp, (int, float)) or grad_warp < 0:
        raise ValueError("grad_warp musi być nieujemną liczbą.")
    if not isinstance(sigma_c, (int, float)) or sigma_c < 0:
        raise ValueError("sigma_c musi być nieujemną liczbą.")
    if not isinstance(step, int) or step < 0:
        raise ValueError("step musi być nieujemną liczbą całkowitą.")
    p = P_delta(grad_warp, sigma_c)
    if np.random.rand() < p:
        delta_t = calc_delta_t(grad_warp)
        event_type = 'meta_foton' if p > 0.7 else 'meta_WZ'
        attrs = assign_attrs(event_type)
        H = update_hypergraph(H, attrs, step)
        return {'type': event_type, 'delta_t': delta_t, 'P_delta': p, 'attrs': attrs}
    return {'type': 'zapadnięcie', 'delta_t': 0, 'P_delta': p, 'attrs': None}
