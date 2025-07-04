import pandas as pd

def export_results(results, output_file='romion_sim_results.csv'):
    """Eksportuje wyniki do CSV."""
    df = pd.DataFrame(results)
    df.to_csv(output_file, index=False)
    return df
