import argparse
from io.simulator import run_simulation

def main():
    parser = argparse.ArgumentParser(description='ROMION SIM™')
    parser.add_argument('--grad_warp', type=float, default=1.2e-17, help='Gradient warp [m^-1]')
    parser.add_argument('--sigma_c', type=float, default=2.0, help='Entropia topologiczna')
    parser.add_argument('--steps', type=int, default=100, help='Liczba kroków')
    parser.add_argument('--output', type=str, default='romion_sim_results.csv', help='Plik wyjściowy')
    args = parser.parse_args()
    results = run_simulation(args.grad_warp, args.sigma_c, args.steps)
    print(results.head())

if __name__ == "__main__":
    main()
