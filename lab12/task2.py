import json
import csv
import time
import hashlib
from typing import List, Dict, Optional, Tuple
import random
import string


class Book:
    """Class to represent a book with title and author."""
    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title.lower() == other.title.lower() and self.author.lower() == other.author.lower()
    
    def __lt__(self, other):
        return self.author.lower() < other.author.lower()


class LibraryManager:
    """Library management system with sorting and search capabilities."""
    
    def __init__(self):
        self.books: List[Book] = []
        self.sorted_books: List[Book] = []
        self.hash_table: Dict[str, List[Book]] = {}
        self.is_sorted = False
    
    def add_book(self, title: str, author: str):
        """Add a book to the library."""
        book = Book(title, author)
        self.books.append(book)
        self.is_sorted = False  # Mark as unsorted when new book is added
    
    def load_from_csv(self, filename: str):
        """Load books from a CSV file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.add_book(row['title'], row['author'])
            print(f"✅ Loaded {len(self.books)} books from {filename}")
        except FileNotFoundError:
            print(f"❌ File {filename} not found. Creating sample data...")
            self.create_sample_data()
        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
    
    def load_from_json(self, filename: str):
        """Load books from a JSON file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for book_data in data:
                    self.add_book(book_data['title'], book_data['author'])
            print(f"✅ Loaded {len(self.books)} books from {filename}")
        except FileNotFoundError:
            print(f"❌ File {filename} not found. Creating sample data...")
            self.create_sample_data()
        except Exception as e:
            print(f"❌ Error loading JSON: {e}")
    
    def create_sample_data(self):
        """Create sample book data for demonstration."""
        sample_books = [
            ("To Kill a Mockingbird", "Harper Lee"),
            ("1984", "George Orwell"),
            ("Pride and Prejudice", "Jane Austen"),
            ("The Great Gatsby", "F. Scott Fitzgerald"),
            ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
            ("The Catcher in the Rye", "J.D. Salinger"),
            ("Lord of the Flies", "William Golding"),
            ("Animal Farm", "George Orwell"),
            ("Brave New World", "Aldous Huxley"),
            ("The Chronicles of Narnia", "C.S. Lewis"),
            ("The Hobbit", "J.R.R. Tolkien"),
            ("The Lord of the Rings", "J.R.R. Tolkien"),
            ("Jane Eyre", "Charlotte Brontë"),
            ("Wuthering Heights", "Emily Brontë"),
            ("Moby Dick", "Herman Melville"),
            ("War and Peace", "Leo Tolstoy"),
            ("The Odyssey", "Homer"),
            ("Hamlet", "William Shakespeare"),
            ("Romeo and Juliet", "William Shakespeare"),
            ("Macbeth", "William Shakespeare"),
            ("The Scarlet Letter", "Nathaniel Hawthorne"),
            ("Frankenstein", "Mary Shelley"),
            ("Dracula", "Bram Stoker"),
            ("The Picture of Dorian Gray", "Oscar Wilde"),
            ("Alice's Adventures in Wonderland", "Lewis Carroll"),
            ("The Adventures of Tom Sawyer", "Mark Twain"),
            ("Adventures of Huckleberry Finn", "Mark Twain"),
            ("Little Women", "Louisa May Alcott"),
            ("Anne of Green Gables", "L.M. Montgomery"),
            ("The Secret Garden", "Frances Hodgson Burnett")
        ]
        
        for title, author in sample_books:
            self.add_book(title, author)
        
        print(f"✅ Created {len(sample_books)} sample books")
    
    def sort_books_by_author(self) -> List[Book]:
        """Sort books by author name alphabetically."""
        self.sorted_books = sorted(self.books, key=lambda book: book.author.lower())
        self.is_sorted = True
        return self.sorted_books
    
    def display_sorted_books(self):
        """Display all books sorted by author."""
        if not self.is_sorted:
            self.sort_books_by_author()
        
        print("\n📚 BOOKS SORTED BY AUTHOR 📚")
        print("=" * 60)
        for i, book in enumerate(self.sorted_books, 1):
            print(f"{i:3d}. {book}")
    
    def linear_search(self, keyword: str) -> Tuple[List[Book], float]:
        """Linear search for books containing the keyword."""
        start_time = time.time()
        results = []
        keyword_lower = keyword.lower()
        
        for book in self.books:
            if (keyword_lower in book.title.lower() or 
                keyword_lower in book.author.lower()):
                results.append(book)
        
        end_time = time.time()
        search_time = end_time - start_time
        return results, search_time
    
    def binary_search(self, keyword: str) -> Tuple[List[Book], float]:
        """Binary search for books (requires sorted data)."""
        if not self.is_sorted:
            self.sort_books_by_author()
        
        start_time = time.time()
        results = []
        keyword_lower = keyword.lower()
        
        # Binary search for exact author matches
        left, right = 0, len(self.sorted_books) - 1
        
        while left <= right:
            mid = (left + right) // 2
            author_lower = self.sorted_books[mid].author.lower()
            
            if keyword_lower in author_lower:
                # Found a match, check surrounding items
                results.append(self.sorted_books[mid])
                
                # Check items before
                i = mid - 1
                while i >= 0 and keyword_lower in self.sorted_books[i].author.lower():
                    results.append(self.sorted_books[i])
                    i -= 1
                
                # Check items after
                i = mid + 1
                while i < len(self.sorted_books) and keyword_lower in self.sorted_books[i].author.lower():
                    results.append(self.sorted_books[i])
                    i += 1
                
                break
            elif keyword_lower < author_lower:
                right = mid - 1
            else:
                left = mid + 1
        
        # Also search in titles using linear search
        for book in self.books:
            if keyword_lower in book.title.lower() and book not in results:
                results.append(book)
        
        end_time = time.time()
        search_time = end_time - start_time
        return results, search_time
    
    def build_hash_table(self):
        """Build hash table for fast searching."""
        self.hash_table = {}
        
        for book in self.books:
            # Create hash keys for both title and author
            title_words = book.title.lower().split()
            author_words = book.author.lower().split()
            
            for word in title_words + author_words:
                # Clean word (remove punctuation)
                clean_word = ''.join(char for char in word if char.isalnum())
                if clean_word:
                    if clean_word not in self.hash_table:
                        self.hash_table[clean_word] = []
                    if book not in self.hash_table[clean_word]:
                        self.hash_table[clean_word].append(book)
    
    def hash_search(self, keyword: str) -> Tuple[List[Book], float]:
        """Hash table search for books."""
        if not self.hash_table:
            self.build_hash_table()
        
        start_time = time.time()
        results = []
        keyword_lower = keyword.lower().strip()
        
        # Direct hash lookup
        if keyword_lower in self.hash_table:
            results = self.hash_table[keyword_lower].copy()
        else:
            # Partial match search
            for word in self.hash_table:
                if keyword_lower in word:
                    for book in self.hash_table[word]:
                        if book not in results:
                            results.append(book)
        
        end_time = time.time()
        search_time = end_time - start_time
        return results, search_time
    
    def search_books(self, keyword: str) -> Dict[str, Tuple[List[Book], float]]:
        """Perform all three search algorithms and return results."""
        results = {}
        
        # Linear search
        linear_results, linear_time = self.linear_search(keyword)
        results['Linear Search'] = (linear_results, linear_time)
        
        # Binary search
        binary_results, binary_time = self.binary_search(keyword)
        results['Binary Search'] = (binary_results, binary_time)
        
        # Hash search
        hash_results, hash_time = self.hash_search(keyword)
        results['Hash Search'] = (hash_results, hash_time)
        
        return results
    
    def display_search_results(self, keyword: str):
        """Display search results from all algorithms."""
        print(f"\n🔍 SEARCH RESULTS FOR: '{keyword}' 🔍")
        print("=" * 60)
        
        results = self.search_books(keyword)
        
        for algorithm_name, (books, search_time) in results.items():
            print(f"\n📊 {algorithm_name.upper()}")
            print(f"   ⏱️  Search Time: {search_time:.6f} seconds")
            print(f"   📚 Found {len(books)} book(s)")
            
            if books:
                for i, book in enumerate(books[:10], 1):  # Show first 10 results
                    print(f"      {i}. {book}")
                if len(books) > 10:
                    print(f"      ... and {len(books) - 10} more")
            else:
                print("      No books found.")
        
        # Performance comparison
        self.compare_performance(results)
    
    def compare_performance(self, results: Dict[str, Tuple[List[Book], float]]):
        """Compare performance of different search algorithms."""
        print(f"\n⚡ PERFORMANCE COMPARISON ⚡")
        print("-" * 40)
        
        # Sort algorithms by speed
        sorted_algorithms = sorted(results.items(), key=lambda x: x[1][1])
        
        fastest_time = sorted_algorithms[0][1][1]
        
        for i, (algorithm, (books, time_taken)) in enumerate(sorted_algorithms):
            if fastest_time > 0:
                speed_ratio = time_taken / fastest_time
                print(f"{i+1}. {algorithm}: {time_taken:.6f}s ({speed_ratio:.2f}x slower)")
            else:
                print(f"{i+1}. {algorithm}: {time_taken:.6f}s")
        
        print(f"\n🏆 Fastest: {sorted_algorithms[0][0]}")
    
    def create_performance_test(self, num_books: int = 1000):
        """Create a large dataset for performance testing."""
        print(f"\n🧪 Creating performance test with {num_books} books...")
        
        # Clear existing books
        self.books = []
        self.is_sorted = False
        
        # Generate random books
        authors = [
            "John Smith", "Jane Doe", "Robert Johnson", "Emily Davis", "Michael Brown",
            "Sarah Wilson", "David Miller", "Lisa Garcia", "James Martinez", "Jennifer Anderson",
            "William Taylor", "Ashley Thomas", "Christopher Jackson", "Amanda White", "Matthew Harris",
            "Jessica Martin", "Daniel Thompson", "Michelle Garcia", "Anthony Martinez", "Stephanie Robinson"
        ]
        
        genres = ["Mystery", "Romance", "Science Fiction", "Fantasy", "Thriller", 
                 "Historical Fiction", "Biography", "Self-Help", "Philosophy", "Poetry"]
        
        for i in range(num_books):
            author = random.choice(authors)
            title = f"{random.choice(genres)} Book {i+1}"
            self.add_book(title, author)
        
        print(f"✅ Created {num_books} test books")


def main():
    """Main function to demonstrate the library management system."""
    library = LibraryManager()
    
    print("🏛️  LIBRARY BOOK MANAGEMENT SYSTEM 🏛️")
    print("=" * 50)
    
    # Try to load from files, create sample data if files don't exist
    library.load_from_csv("books.csv")
    
    # Display sorted books
    library.display_sorted_books()
    
    # Interactive search
    while True:
        print(f"\n{'='*60}")
        print("🔍 SEARCH OPTIONS:")
        print("1. Search by keyword")
        print("2. Performance test")
        print("3. Display all books")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            keyword = input("Enter search keyword: ").strip()
            if keyword:
                library.display_search_results(keyword)
            else:
                print("❌ Please enter a valid keyword.")
        
        elif choice == '2':
            num_books = input("Enter number of books for performance test (default 1000): ").strip()
            try:
                num_books = int(num_books) if num_books else 1000
                library.create_performance_test(num_books)
                
                # Test with common search terms
                test_keywords = ["Smith", "Book", "John", "Mystery"]
                for keyword in test_keywords:
                    library.display_search_results(keyword)
            except ValueError:
                print("❌ Please enter a valid number.")
        
        elif choice == '3':
            library.display_sorted_books()
        
        elif choice == '4':
            print("👋 Thank you for using the Library Management System!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
