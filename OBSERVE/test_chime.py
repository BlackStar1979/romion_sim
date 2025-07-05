from astropy.io import fits
import pandas as pd
from romion_sim.core.metrics import P_delta, calc_delta_t
from romion_sim.io.logger import log_event

def parse_chime_data(file_path, output_file='chime_anomalies.csv'):
    try:
        data = fits.open(file_path)
        times = data['TIMES'].data
        dm_values = data['DM'].data
        locations = data['LOC'].data
        anomalies = []
        for t, dm, loc in zip(times, dm_values, locations):
            delta_t = t * 1e-3
            grad_warp = calc_delta_t(delta_t)
            sigma_c = 1.6094 + np.random.uniform(-0.2, 0.4)
            P_delta_val = P_delta(grad_warp, sigma_c)
            if dm < 10 and abs(delta_t - 1) < 0.1:
                anomaly = {
                    'ID': loc['ID'], 'delta_t': delta_t, 'DM': dm,
                    'grad_warp': grad_warp, 'sigma_c': sigma_c, 'P_delta': P_delta_val
                }
                log_event(anomaly)
                anomalies.append(anomaly)
        df = pd.DataFrame(anomalies)
        df.to_csv(output_file, index=False)
        return df
    except Exception as e:
        print(f"Błąd: {e}")
        return None
