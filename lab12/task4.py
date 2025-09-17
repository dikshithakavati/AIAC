import random
import time
import heapq
from typing import List, Dict, Tuple, Optional
from datetime import datetime, timedelta
import json
import csv


class Stock:
    """Class to represent a stock with price data and performance metrics."""
    
    def __init__(self, symbol: str, opening_price: float, closing_price: float, 
                 volume: int = 1000000, market_cap: float = None):
        self.symbol = symbol.upper()
        self.opening_price = opening_price
        self.closing_price = closing_price
        self.volume = volume
        self.market_cap = market_cap
        self.percentage_change = self._calculate_percentage_change()
        self.price_change = self.closing_price - self.opening_price
    
    def _calculate_percentage_change(self) -> float:
        """Calculate percentage change from opening to closing price."""
        if self.opening_price == 0:
            return 0.0
        return ((self.closing_price - self.opening_price) / self.opening_price) * 100
    
    def __repr__(self):
        return f"Stock(symbol='{self.symbol}', change={self.percentage_change:.2f}%)"
    
    def __str__(self):
        return f"{self.symbol}: ${self.closing_price:.2f} ({self.percentage_change:+.2f}%)"
    
    def __lt__(self, other):
        """For max-heap (highest percentage change first)."""
        return self.percentage_change > other.percentage_change
    
    def __eq__(self, other):
        return self.symbol == other.symbol
    
    def __hash__(self):
        return hash(self.symbol)
    
    def get_performance_indicator(self) -> str:
        """Get visual indicator for stock performance."""
        if self.percentage_change > 5:
            return "🚀"
        elif self.percentage_change > 2:
            return "📈"
        elif self.percentage_change > 0:
            return "📊"
        elif self.percentage_change > -2:
            return "📉"
        elif self.percentage_change > -5:
            return "📉"
        else:
            return "💥"


class StockDataGenerator:
    """Generate realistic stock price data for testing."""
    
    def __init__(self):
        self.stock_symbols = [
            "AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "NFLX",
            "AMD", "INTC", "CRM", "ADBE", "PYPL", "UBER", "LYFT", "SPOT",
            "TWTR", "SNAP", "PINS", "ZOOM", "SQ", "ROKU", "CRWD", "OKTA",
            "ZM", "DOCU", "SNOW", "PLTR", "RBLX", "COIN", "HOOD", "SOFI",
            "JPM", "BAC", "WFC", "GS", "MS", "C", "AXP", "USB",
            "JNJ", "PFE", "UNH", "ABBV", "MRK", "TMO", "ABT", "DHR",
            "WMT", "PG", "KO", "PEP", "COST", "HD", "LOW", "TGT",
            "DIS", "NKE", "SBUX", "MCD", "YUM", "CMG", "CHIP", "DPZ"
        ]
    
    def generate_stock_data(self, num_stocks: int = 100) -> List[Stock]:
        """Generate random stock data."""
        stocks = []
        selected_symbols = random.sample(self.stock_symbols, min(num_stocks, len(self.stock_symbols)))
        
        for symbol in selected_symbols:
            # Generate realistic price ranges based on stock type
            if symbol in ["AAPL", "GOOGL", "AMZN", "TSLA"]:
                base_price = random.uniform(100, 3000)
            elif symbol in ["JPM", "BAC", "WFC", "GS"]:
                base_price = random.uniform(30, 400)
            else:
                base_price = random.uniform(10, 500)
            
            # Generate opening and closing prices with realistic daily volatility
            volatility = random.uniform(0.02, 0.15)  # 2-15% daily volatility
            price_change = random.uniform(-volatility, volatility) * base_price
            
            opening_price = base_price
            closing_price = max(0.01, opening_price + price_change)  # Ensure positive price
            
            volume = random.randint(100000, 50000000)
            market_cap = closing_price * random.randint(1000000, 1000000000)
            
            stock = Stock(symbol, opening_price, closing_price, volume, market_cap)
            stocks.append(stock)
        
        return stocks


class HeapSort:
    """Heap Sort implementation for sorting stocks by performance."""
    
    @staticmethod
    def heapify(arr: List[Stock], n: int, i: int):
        """Heapify a subtree rooted at index i."""
        largest = i  # Initialize largest as root
        left = 2 * i + 1
        right = 2 * i + 2
        
        # If left child is larger than root
        if left < n and arr[left].percentage_change > arr[largest].percentage_change:
            largest = left
        
        # If right child is larger than largest so far
        if right < n and arr[right].percentage_change > arr[largest].percentage_change:
            largest = right
        
        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            HeapSort.heapify(arr, n, largest)
    
    @staticmethod
    def heap_sort(stocks: List[Stock]) -> List[Stock]:
        """Sort stocks using heap sort algorithm."""
        arr = stocks.copy()
        n = len(arr)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(arr, n, i)
        
        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]  # Swap
            HeapSort.heapify(arr, i, 0)  # Heapify reduced heap
        
        return arr


class StockHashMap:
    """Hash Map implementation for fast stock symbol lookup."""
    
    def __init__(self, initial_capacity: int = 100):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]
    
    def _hash(self, symbol: str) -> int:
        """Simple hash function for stock symbols."""
        hash_value = 0
        for char in symbol:
            hash_value = (hash_value * 31 + ord(char)) % self.capacity
        return hash_value
    
    def insert(self, stock: Stock):
        """Insert a stock into the hash map."""
        if self.size >= self.capacity * 0.75:  # Load factor of 0.75
            self._resize()
        
        index = self._hash(stock.symbol)
        bucket = self.buckets[index]
        
        # Check if stock already exists
        for i, (existing_symbol, existing_stock) in enumerate(bucket):
            if existing_symbol == stock.symbol:
                bucket[i] = (stock.symbol, stock)
                return
        
        # Add new stock
        bucket.append((stock.symbol, stock))
        self.size += 1
    
    def _resize(self):
        """Resize the hash map when load factor is exceeded."""
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        
        # Rehash all existing stocks
        for bucket in old_buckets:
            for symbol, stock in bucket:
                self.insert(stock)
    
    def get(self, symbol: str) -> Optional[Stock]:
        """Get stock by symbol."""
        index = self._hash(symbol.upper())
        bucket = self.buckets[index]
        
        for existing_symbol, stock in bucket:
            if existing_symbol == symbol.upper():
                return stock
        
        return None
    
    def contains(self, symbol: str) -> bool:
        """Check if stock exists in hash map."""
        return self.get(symbol) is not None
    
    def get_all_stocks(self) -> List[Stock]:
        """Get all stocks from the hash map."""
        stocks = []
        for bucket in self.buckets:
            for symbol, stock in bucket:
                stocks.append(stock)
        return stocks


class FinTechAnalyzer:
    """Main class for AI-powered FinTech stock analysis."""
    
    def __init__(self):
        self.stocks: List[Stock] = []
        self.hash_map = StockHashMap()
        self.generator = StockDataGenerator()
        self.performance_stats = {}
    
    def load_stock_data(self, num_stocks: int = 100):
        """Load or generate stock data."""
        print(f"📊 Loading {num_stocks} stocks...")
        self.stocks = self.generator.generate_stock_data(num_stocks)
        
        # Build hash map
        for stock in self.stocks:
            self.hash_map.insert(stock)
        
        print(f"✅ Loaded {len(self.stocks)} stocks successfully!")
    
    def heap_sort_stocks(self) -> Tuple[List[Stock], float]:
        """Sort stocks using heap sort algorithm."""
        start_time = time.time()
        sorted_stocks = HeapSort.heap_sort(self.stocks)
        end_time = time.time()
        
        sort_time = end_time - start_time
        self.performance_stats['Heap Sort'] = sort_time
        
        return sorted_stocks, sort_time
    
    def standard_sort_stocks(self) -> Tuple[List[Stock], float]:
        """Sort stocks using Python's built-in sorted function."""
        start_time = time.time()
        sorted_stocks = sorted(self.stocks, key=lambda x: x.percentage_change, reverse=True)
        end_time = time.time()
        
        sort_time = end_time - start_time
        self.performance_stats['Standard Sort'] = sort_time
        
        return sorted_stocks, sort_time
    
    def hash_search_stock(self, symbol: str) -> Tuple[Optional[Stock], float]:
        """Search for stock using custom hash map."""
        start_time = time.time()
        stock = self.hash_map.get(symbol)
        end_time = time.time()
        
        search_time = end_time - start_time
        self.performance_stats[f'Hash Search ({symbol})'] = search_time
        
        return stock, search_time
    
    def dict_search_stock(self, symbol: str) -> Tuple[Optional[Stock], float]:
        """Search for stock using Python dictionary."""
        # Build dictionary for comparison
        stock_dict = {stock.symbol: stock for stock in self.stocks}
        
        start_time = time.time()
        stock = stock_dict.get(symbol.upper())
        end_time = time.time()
        
        search_time = end_time - start_time
        self.performance_stats[f'Dict Search ({symbol})'] = search_time
        
        return stock, search_time
    
    def linear_search_stock(self, symbol: str) -> Tuple[Optional[Stock], float]:
        """Search for stock using linear search."""
        start_time = time.time()
        stock = None
        for s in self.stocks:
            if s.symbol == symbol.upper():
                stock = s
                break
        end_time = time.time()
        
        search_time = end_time - start_time
        self.performance_stats[f'Linear Search ({symbol})'] = search_time
        
        return stock, search_time
    
    def display_sorted_stocks(self, sorted_stocks: List[Stock], title: str, limit: int = 20):
        """Display sorted stocks in a formatted table."""
        print(f"\n{title}")
        print("=" * 80)
        print(f"{'Rank':<5} {'Symbol':<8} {'Price':<10} {'Change':<10} {'% Change':<10} {'Indicator':<10}")
        print("-" * 80)
        
        for i, stock in enumerate(sorted_stocks[:limit], 1):
            indicator = stock.get_performance_indicator()
            print(f"{i:<5} {stock.symbol:<8} ${stock.closing_price:<9.2f} "
                  f"${stock.price_change:<+9.2f} {stock.percentage_change:<+9.2f}% {indicator:<10}")
        
        if len(sorted_stocks) > limit:
            print(f"... and {len(sorted_stocks) - limit} more stocks")
    
    def compare_sorting_performance(self):
        """Compare performance of different sorting algorithms."""
        print(f"\n⚡ SORTING PERFORMANCE COMPARISON ⚡")
        print("=" * 60)
        
        # Test heap sort
        heap_sorted, heap_time = self.heap_sort_stocks()
        
        # Test standard sort
        standard_sorted, standard_time = self.standard_sort_stocks()
        
        # Display results
        print(f"Heap Sort:     {heap_time:.6f} seconds")
        print(f"Standard Sort: {standard_time:.6f} seconds")
        
        if heap_time > 0:
            speed_ratio = standard_time / heap_time
            if speed_ratio > 1:
                print(f"Heap Sort is {speed_ratio:.2f}x faster than Standard Sort")
            else:
                print(f"Standard Sort is {1/speed_ratio:.2f}x faster than Heap Sort")
        
        return heap_sorted, standard_sorted
    
    def compare_search_performance(self, symbol: str):
        """Compare performance of different search algorithms."""
        print(f"\n🔍 SEARCH PERFORMANCE COMPARISON FOR '{symbol}' 🔍")
        print("=" * 70)
        
        # Test hash search
        hash_result, hash_time = self.hash_search_stock(symbol)
        
        # Test dict search
        dict_result, dict_time = self.dict_search_stock(symbol)
        
        # Test linear search
        linear_result, linear_time = self.linear_search_stock(symbol)
        
        # Display results
        print(f"Hash Search:   {hash_time:.6f} seconds")
        print(f"Dict Search:   {dict_time:.6f} seconds")
        print(f"Linear Search: {linear_time:.6f} seconds")
        
        # Find fastest
        times = [('Hash Search', hash_time), ('Dict Search', dict_time), ('Linear Search', linear_time)]
        fastest = min(times, key=lambda x: x[1])
        
        print(f"\n🏆 Fastest: {fastest[0]}")
        
        # Show results
        if hash_result:
            print(f"\n📊 Stock Found: {hash_result}")
        else:
            print(f"\n❌ Stock '{symbol}' not found")
        
        return hash_result, dict_result, linear_result
    
    def display_market_summary(self):
        """Display overall market performance summary."""
        if not self.stocks:
            print("❌ No stock data available")
            return
        
        total_stocks = len(self.stocks)
        gaining_stocks = sum(1 for stock in self.stocks if stock.percentage_change > 0)
        losing_stocks = sum(1 for stock in self.stocks if stock.percentage_change < 0)
        flat_stocks = total_stocks - gaining_stocks - losing_stocks
        
        avg_change = sum(stock.percentage_change for stock in self.stocks) / total_stocks
        max_gainer = max(self.stocks, key=lambda x: x.percentage_change)
        max_loser = min(self.stocks, key=lambda x: x.percentage_change)
        
        print(f"\n📈 MARKET SUMMARY 📈")
        print("=" * 50)
        print(f"Total Stocks: {total_stocks}")
        print(f"Gaining: {gaining_stocks} ({gaining_stocks/total_stocks*100:.1f}%)")
        print(f"Losing: {losing_stocks} ({losing_stocks/total_stocks*100:.1f}%)")
        print(f"Flat: {flat_stocks} ({flat_stocks/total_stocks*100:.1f}%)")
        print(f"Average Change: {avg_change:+.2f}%")
        print(f"Best Performer: {max_gainer}")
        print(f"Worst Performer: {max_loser}")
    
    def performance_analysis(self):
        """Analyze and display performance statistics."""
        print(f"\n📊 PERFORMANCE ANALYSIS 📊")
        print("=" * 50)
        
        if not self.performance_stats:
            print("No performance data available. Run some operations first.")
            return
        
        print("Algorithm Performance:")
        for operation, time_taken in self.performance_stats.items():
            print(f"  {operation}: {time_taken:.6f}s")
        
        # Recommendations
        print(f"\n💡 RECOMMENDATIONS:")
        print("• Use Hash Maps for frequent symbol lookups (O(1) average)")
        print("• Use Heap Sort for real-time sorting of large datasets")
        print("• Standard Python sort() is optimized and often faster for small datasets")
        print("• Consider hybrid approaches based on data size and access patterns")


def main():
    """Main function for the AI-powered FinTech Lab."""
    analyzer = FinTechAnalyzer()
    
    print("🤖 AI-POWERED FINTECH LAB - SR UNIVERSITY 🤖")
    print("=" * 60)
    print("Advanced Stock Analysis and Performance Optimization")
    
    # Load initial data
    num_stocks = input("Enter number of stocks to analyze (default 100): ").strip()
    try:
        num_stocks = int(num_stocks) if num_stocks else 100
        analyzer.load_stock_data(num_stocks)
    except ValueError:
        print("Invalid input. Using default 100 stocks.")
        analyzer.load_stock_data(100)
    
    while True:
        print(f"\n{'='*60}")
        print("📊 ANALYSIS OPTIONS:")
        print("1. Compare Sorting Algorithms")
        print("2. Search Stock by Symbol")
        print("3. Display Market Summary")
        print("4. Performance Analysis")
        print("5. Load New Dataset")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            heap_sorted, standard_sorted = analyzer.compare_sorting_performance()
            
            # Display top performers
            analyzer.display_sorted_stocks(heap_sorted, "🏆 TOP PERFORMERS (Heap Sort)", 15)
            
        elif choice == '2':
            symbol = input("Enter stock symbol to search: ").strip().upper()
            if symbol:
                hash_result, dict_result, linear_result = analyzer.compare_search_performance(symbol)
            else:
                print("❌ Please enter a valid stock symbol.")
        
        elif choice == '3':
            analyzer.display_market_summary()
        
        elif choice == '4':
            analyzer.performance_analysis()
        
        elif choice == '5':
            num_stocks = input("Enter number of stocks (default 100): ").strip()
            try:
                num_stocks = int(num_stocks) if num_stocks else 100
                analyzer.load_stock_data(num_stocks)
            except ValueError:
                print("Invalid input. Using default 100 stocks.")
                analyzer.load_stock_data(100)
        
        elif choice == '6':
            print("👋 Thank you for using AI-Powered FinTech Lab!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
