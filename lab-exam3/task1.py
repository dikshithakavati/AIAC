import time

def fib_dp_tabulation(n):
    """
    Calculate Fibonacci number using Dynamic Programming (Tabulation).
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    # Create a table to store Fibonacci numbers
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    
    # Fill the table iteratively
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fib_recursive(n):
    """
    Calculate Fibonacci number using pure recursion.
    Time Complexity: O(2^n) - Exponential
    Space Complexity: O(n) - Call stack depth
    """
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def get_first_n_fibonacci_dp(n):
    """Get first n Fibonacci numbers using DP tabulation"""
    if n <= 0:
        return []
    
    dp = [0] * n
    if n >= 1:
        dp[0] = 0
    if n >= 2:
        dp[1] = 1
    
    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp


def print_section(title):
    """Print a formatted section title"""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


# Main execution
if __name__ == "__main__":
    print_section("FIBONACCI SEQUENCE - Dynamic Programming vs Recursion")
    
    # Part 1: Print first 15 Fibonacci numbers using DP
    print_section("Part 1: First 15 Fibonacci Numbers (DP Tabulation)")
    fib_sequence = get_first_n_fibonacci_dp(15)
    
    for i, value in enumerate(fib_sequence):
        print(f"F({i}) = {value}")
    
    # Part 2: Runtime Comparison
    print_section("Part 2: Runtime Comparison")
    
    # Test DP Tabulation with larger number
    n_dp = 35
    print(f"\nCalculating F({n_dp}) using DP Tabulation...")
    start_time = time.time()
    result_dp = fib_dp_tabulation(n_dp)
    end_time = time.time()
    time_dp = end_time - start_time
    
    print(f"Result: {result_dp}")
    print(f"Time taken: {time_dp:.6f} seconds")
    
    # Test Recursive with smaller number (to avoid long wait time)
    n_recursive = 35
    print(f"\nCalculating F({n_recursive}) using Pure Recursion...")
    start_time = time.time()
    result_recursive = fib_recursive(n_recursive)
    end_time = time.time()
    time_recursive = end_time - start_time
    
    print(f"Result: {result_recursive}")
    print(f"Time taken: {time_recursive:.6f} seconds")
    
    # Comparison
    print_section("Comparison Summary")
    print(f"\nFor calculating F({n_dp}):")
    print(f"  DP Tabulation Time:  {time_dp:.6f} seconds")
    print(f"  Pure Recursion Time: {time_recursive:.6f} seconds")
    
    if time_recursive > 0:
        speedup = time_recursive / time_dp
        print(f"  Speedup Factor: {speedup:.2f}x faster with DP")
    
    print(f"\nTime Complexity Analysis:")
    print(f"  DP Tabulation:   O(n) - Linear")
    print(f"  Pure Recursion:  O(2^n) - Exponential")
    
    print(f"\nSpace Complexity Analysis:")
    print(f"  DP Tabulation:   O(n) - Stores all values in array")
    print(f"  Pure Recursion:  O(n) - Call stack depth")
    
    print("\n" + "=" * 60)
