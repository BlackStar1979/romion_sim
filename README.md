# ROMION SIM™ — Topologiczny Silnik Symulacyjny

Symulator przeskoków topologicznych Δ w hipergrafie romionowym, modelujący trajektorie warpowo-topologiczne, takie jak anomalie FRB (δt ≈ 1 ms, DM < 10 pc/cm³), meta-fotony i meta-W/Z.

---

## 📦 Struktura katalogów
romion_sim/
├── core/
│   ├── engine.py
│   ├── topology.py
│   ├── metrics.py
│   └── config.py
├── io/
│   ├── exporter.py
│   ├── logger.py
│   └── simulator.py
├── run_sim.py
├── README.md
├── requirements.txt

romion_sim/
├── core/
│   ├── engine.py
│   ├── topology.py
│   ├── metrics.py
│   ├── config.py
├── io/
│   ├── exporter.py
│   ├── logger.py
│   ├── simulator.py
├── data/
│   ├── test_vectors.json
├── run_sim.py
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore

---

## 🔧 Wymagania

- Python 3.8+
- Biblioteki: `hypernetx`, `numpy`, `pandas`
