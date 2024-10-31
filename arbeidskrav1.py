# -*- coding: utf-8 -*-
"""
PY1010 - Arbeidskrav 1
- Beregne årlige kostnader for en elbil og en bensinbil

Nils Erik Asmundvaag, 31.10.2024

"""

# Forutsetninger for beregningene

ant_dager = 365             # Antall dager i peroden det skal beregnes for
km_aar = 10000              # Antall kjørte km pr år
forsikring_el = 5000        # Forsikring pr år, elbil
forsikring_bensin = 7500    # Forsikring pr år, bensinbil
trafikk_forsikring = 8.38   # Trafikkforsikring pr dag
forbruk_kwh_el = 0.2        # Forbruk Elbil, kWh/km
strompris = 2.0             # Strømpris pr kWh
forbruk_bensin = 1.0        # Pris pr km for bensinbil
bomavgift_el = 0.1          # Bomavgift pr km, elbil
bomavgift_bensin = 0.3      # Bomavgift pr km, bensin

# Beregne kostnader for ett år for en elbil

kost_el = forsikring_el + (trafikk_forsikring * ant_dager) + (forbruk_kwh_el * strompris * km_aar) + (bomavgift_el * km_aar)

# Beregne kostnader for ett år for en bensinbil

kost_bensin = forsikring_bensin + (trafikk_forsikring * ant_dager) + (forbruk_bensin * km_aar) + (bomavgift_bensin * km_aar)

# Skriv ut resultat
print(f"Årlig kostnad elbil:     {kost_el:.2f}")
print(f"Årlig kostnad bensinbil: {kost_bensin:.2f}")
print()
print(f"Differanse: {max(kost_el, kost_bensin) - min(kost_el, kost_bensin):.2f}")
