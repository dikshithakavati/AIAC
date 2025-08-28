def compute_ratios(values):
    results = []
    for i in range(len(values)):
        for j in range(len(values)):
            # Avoid division by zero when i equals j
            if i != j:
                try:
                    ratio = values[i] / (values[j] - values[i])
                    results.append((i, j, ratio))
                except ZeroDivisionError:
                    # Skip if denominator is zero
                    continue
    return results

num = [5, 10, 15, 20, 25]
print(compute_ratios(num))