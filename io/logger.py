import logging

def setup_logger():
    """Konfiguruje logger."""
    logging.basicConfig(filename='romion_sim.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s')
    return logging.getLogger()

def log_event(event):
    """Loguje zdarzenie."""
    logger = setup_logger()
    logger.info(f"Zdarzenie: {event['type']}, δt: {event['delta_t']:.3f} ms, P(Δ): {event['P_delta']:.3f}")
