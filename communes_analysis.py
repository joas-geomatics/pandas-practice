import pandas as pd

data = {
    "commune": ["Grand-Popo", "Ouidah", "Cotonou", "Sèmè-Podji"],
    "population": [150000, 160000, 900000, 250000],
    "superficie_km2": [289, 364, 79, 250],
    "altitude_m": [4, 12, 6, 8],
}

df = pd.DataFrame(data)

# Indicator
df["densite"] = df["population"] / df["superficie_km2"]

# Filter: high coastal risk (example rule)
df_risque_eleve = df[df["altitude_m"] < 5][["commune", "altitude_m", "densite"]]

# Aggregations
population_totale = df["population"].sum()
densite_moy = df["densite"].mean()
alt_moy = df["altitude_m"].mean()

print(df)
print("\nHigh risk (altitude_m < 5):")
print(df_risque_eleve)

print(
    f"\nPopulation totale: {population_totale} hab | "
    f"Densité moyenne: {densite_moy:.2f} hab/km² | "
    f"Altitude moyenne: {alt_moy:.2f} m"
)

# Export
df.to_csv("communes_analyse.csv", index=False)
