# Task 1: Define Raw Data
signals: list[float] = [10.5, 3.2, 45.0, 0.5, 12.1, 2.8, 80.5]

# Task 2: Filter Noise (List Comprehension with 'if')
# Syntax: [expression for item in list if condition]
valid_signals = [s for s in signals if s > 5.0]

# Task 3: Boost the Signal (List Comprehension transformation)
# Syntax: [expression * 1.1 for item in list]
boosted_signals = [round(s * 1.1, 2) for s in valid_signals]

# Task 4 & 5: Analysis
peak_signal = max(boosted_signals)
average_signal = sum(boosted_signals) / len(boosted_signals)

print(f"Valid Signals Found: {valid_signals}")
print(f"Boosted Signals (10% increase): {boosted_signals}")
print(f"--- Telemetry Report ---")
print(f"Peak Strength: {peak_signal}")
print(f"Average Strength: {round(average_signal, 2)}")

