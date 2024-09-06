import math
import statistics

def calculate_statistics(data):
    if not data:
        return "Data list is empty"
    
    # Mean
    mean = statistics.mean(data)

    # Standard Deviation
    std_dev = statistics.stdev(data)

    # Median
    median = statistics.median(data)

    # Absolute Variance (Mean Absolute Deviation)
    abs_variance = sum(abs(x - mean) for x in data) / len(data)

    return {
        "Standard Deviation": std_dev,
        "Median": median,
        "Absolute Variance": abs_variance
    }

# Example usage
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = calculate_statistics(data)
print(result)
