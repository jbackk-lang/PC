from skret_ai import SkretAI

# przykładowe dane wejściowe
ai = SkretAI(a=10.0, b=13.5, c=9.2, d=15.7)

j = ai.process()

print("=== AI SKRĘTOWA — PUNKT J ===")
print(f"Compressed energy:  {j.compressed_energy:.4f}")
print(f"Compressed tension: {j.compressed_tension:.4f}")
print(f"Stability:          {j.stability:.4f}")
