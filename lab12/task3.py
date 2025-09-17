import json
import csv
import time
import hashlib
from typing import List, Dict, Optional, Tuple
import random
from datetime import datetime


class ResearchPaper:
    """Class to represent a research paper with title, author, and metadata."""
    
    def __init__(self, title: str, author: str, year: int = None, journal: str = None, doi: str = None):
        self.title = title
        self.author = author
        self.year = year
        self.journal = journal
        self.doi = doi
    
    def __repr__(self):
        return f"ResearchPaper(title='{self.title}', author='{self.author}', year={self.year})"
    
    def __str__(self):
        return f"{self.title} by {self.author} ({self.year})"
    
    def __eq__(self, other):
        return (self.title.lower() == other.title.lower() and 
                self.author.lower() == other.author.lower())
    
    def __lt__(self, other):
        return self.title.lower() < other.title.lower()
    
    def __hash__(self):
        return hash((self.title.lower(), self.author.lower()))


class DigitalLibrary:
    """SR University Digital Library with efficient search capabilities."""
    
    def __init__(self):
        self.papers: List[ResearchPaper] = []
        self.sorted_papers: List[ResearchPaper] = []
        self.hash_table_title: Dict[str, List[ResearchPaper]] = {}
        self.hash_table_author: Dict[str, List[ResearchPaper]] = {}
        self.is_sorted = False
        self.hash_built = False
    
    def add_paper(self, title: str, author: str, year: int = None, journal: str = None, doi: str = None):
        """Add a research paper to the library."""
        paper = ResearchPaper(title, author, year, journal, doi)
        self.papers.append(paper)
        self.is_sorted = False
        self.hash_built = False
    
    def load_from_csv(self, filename: str):
        """Load research papers from a CSV file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    year = int(row.get('year', 2023)) if row.get('year') else None
                    self.add_paper(
                        row['title'], 
                        row['author'], 
                        year,
                        row.get('journal', ''),
                        row.get('doi', '')
                    )
            print(f"✅ Loaded {len(self.papers)} research papers from {filename}")
        except FileNotFoundError:
            print(f"❌ File {filename} not found. Creating sample research papers...")
            self.create_sample_research_papers()
        except Exception as e:
            print(f"❌ Error loading CSV: {e}")
    
    def load_from_json(self, filename: str):
        """Load research papers from a JSON file."""
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for paper_data in data:
                    self.add_paper(
                        paper_data['title'], 
                        paper_data['author'],
                        paper_data.get('year'),
                        paper_data.get('journal', ''),
                        paper_data.get('doi', '')
                    )
            print(f"✅ Loaded {len(self.papers)} research papers from {filename}")
        except FileNotFoundError:
            print(f"❌ File {filename} not found. Creating sample research papers...")
            self.create_sample_research_papers()
        except Exception as e:
            print(f"❌ Error loading JSON: {e}")
    
    def create_sample_research_papers(self):
        """Create sample research papers for demonstration."""
        sample_papers = [
            ("Machine Learning Algorithms for Big Data Analysis", "Dr. Sarah Johnson", 2023, "IEEE Transactions on Knowledge and Data Engineering"),
            ("Deep Learning Applications in Computer Vision", "Prof. Michael Chen", 2023, "Nature Machine Intelligence"),
            ("Blockchain Technology in Healthcare Systems", "Dr. Emily Rodriguez", 2023, "Journal of Medical Internet Research"),
            ("Quantum Computing and Cryptography", "Dr. David Kim", 2023, "Physical Review Letters"),
            ("Artificial Intelligence in Autonomous Vehicles", "Prof. Lisa Wang", 2023, "IEEE Transactions on Intelligent Transportation Systems"),
            ("Natural Language Processing for Sentiment Analysis", "Dr. Robert Smith", 2023, "Computational Linguistics"),
            ("Cybersecurity Threats in IoT Devices", "Dr. Jennifer Brown", 2023, "IEEE Security & Privacy"),
            ("Cloud Computing Performance Optimization", "Prof. William Davis", 2023, "ACM Computing Surveys"),
            ("Data Mining Techniques for Social Networks", "Dr. Maria Garcia", 2023, "Knowledge and Information Systems"),
            ("Neural Networks for Pattern Recognition", "Dr. James Wilson", 2023, "Neural Networks"),
            ("Software Engineering Best Practices", "Prof. Patricia Miller", 2023, "IEEE Software"),
            ("Human-Computer Interaction Design", "Dr. Thomas Anderson", 2023, "ACM Transactions on Computer-Human Interaction"),
            ("Database Systems Optimization", "Dr. Linda Taylor", 2023, "ACM Transactions on Database Systems"),
            ("Computer Graphics and Visualization", "Prof. Christopher Lee", 2023, "ACM Transactions on Graphics"),
            ("Distributed Systems Architecture", "Dr. Amanda White", 2023, "ACM Transactions on Computer Systems"),
            ("Mobile Application Development", "Dr. Kevin Martinez", 2023, "IEEE Pervasive Computing"),
            ("Web Security and Privacy", "Prof. Rachel Thompson", 2023, "ACM Computing Surveys"),
            ("Computer Networks Performance", "Dr. Steven Jackson", 2023, "IEEE/ACM Transactions on Networking"),
            ("Operating Systems Design", "Dr. Nancy Harris", 2023, "ACM Transactions on Computer Systems"),
            ("Information Retrieval Systems", "Prof. Mark Clark", 2023, "Information Retrieval Journal"),
            ("Machine Learning for Healthcare", "Dr. Susan Lewis", 2023, "Journal of the American Medical Informatics Association"),
            ("Artificial Intelligence Ethics", "Dr. Daniel Walker", 2023, "AI & Society"),
            ("Computer Vision in Robotics", "Prof. Karen Hall", 2023, "International Journal of Computer Vision"),
            ("Data Science and Analytics", "Dr. Paul Allen", 2023, "Journal of Data Science"),
            ("Cryptocurrency and Blockchain", "Dr. Michelle Young", 2023, "Financial Innovation"),
            ("Virtual Reality and Augmented Reality", "Prof. Gary King", 2023, "Presence: Teleoperators and Virtual Environments"),
            ("Internet of Things Security", "Dr. Sandra Wright", 2023, "IEEE Internet of Things Journal"),
            ("Bioinformatics and Computational Biology", "Dr. Raymond Green", 2023, "Bioinformatics"),
            ("Wireless Communication Systems", "Prof. Donna Baker", 2023, "IEEE Transactions on Wireless Communications"),
            ("Computer Architecture Optimization", "Dr. Timothy Adams", 2023, "IEEE Computer Architecture Letters"),
            ("Digital Signal Processing", "Dr. Barbara Nelson", 2023, "IEEE Transactions on Signal Processing"),
            ("Software Testing and Quality Assurance", "Prof. Richard Carter", 2023, "IEEE Transactions on Software Engineering"),
            ("Computer Security and Cryptography", "Dr. Margaret Mitchell", 2023, "IEEE Transactions on Information Forensics and Security"),
            ("Parallel and Distributed Computing", "Dr. Joseph Turner", 2023, "IEEE Transactions on Parallel and Distributed Systems"),
            ("Machine Learning Optimization", "Prof. Elizabeth Phillips", 2023, "Journal of Machine Learning Research"),
            ("Human-Robot Interaction", "Dr. George Campbell", 2023, "International Journal of Social Robotics"),
            ("Cloud Security and Privacy", "Dr. Helen Parker", 2023, "IEEE Cloud Computing"),
            ("Computer Graphics Algorithms", "Prof. Ronald Evans", 2023, "Computer Graphics Forum"),
            ("Data Compression Techniques", "Dr. Cynthia Edwards", 2023, "IEEE Transactions on Information Theory"),
            ("Network Security Protocols", "Dr. Frank Collins", 2023, "Computer Networks"),
            ("Artificial Neural Networks", "Prof. Sharon Stewart", 2023, "Neural Computing and Applications"),
            ("Mobile Computing Systems", "Dr. Gregory Sanchez", 2023, "IEEE Pervasive Computing"),
            ("Computer Vision Algorithms", "Dr. Ruth Morris", 2023, "Pattern Recognition"),
            ("Database Security and Privacy", "Prof. Kenneth Rogers", 2023, "ACM Transactions on Database Systems"),
            ("Software Architecture Design", "Dr. Laura Reed", 2023, "IEEE Software"),
            ("Machine Learning in Finance", "Dr. Bruce Cook", 2023, "Journal of Financial Economics"),
            ("Cybersecurity Risk Assessment", "Prof. Janet Bell", 2023, "Risk Analysis"),
            ("Computer Networks Optimization", "Dr. Howard Murphy", 2023, "Computer Networks"),
            ("Human-Computer Interaction", "Dr. Katherine Rivera", 2023, "International Journal of Human-Computer Studies"),
            ("Data Mining and Knowledge Discovery", "Prof. Arthur Cooper", 2023, "Data Mining and Knowledge Discovery")
        ]
        
        for title, author, year, journal in sample_papers:
            self.add_paper(title, author, year, journal)
        
        print(f"✅ Created {len(sample_papers)} sample research papers")
    
    def linear_search(self, keyword: str) -> Tuple[List[ResearchPaper], float]:
        """Linear search for research papers containing the keyword."""
        start_time = time.time()
        results = []
        keyword_lower = keyword.lower()
        
        for paper in self.papers:
            if (keyword_lower in paper.title.lower() or 
                keyword_lower in paper.author.lower() or
                (paper.journal and keyword_lower in paper.journal.lower())):
                results.append(paper)
        
        end_time = time.time()
        search_time = end_time - start_time
        return results, search_time
    
    def sort_papers_by_title(self):
        """Sort papers by title alphabetically."""
        self.sorted_papers = sorted(self.papers, key=lambda paper: paper.title.lower())
        self.is_sorted = True
        return self.sorted_papers
    
    def binary_search(self, keyword: str) -> Tuple[List[ResearchPaper], float]:
        """Binary search for research papers (requires sorted data)."""
        if not self.is_sorted:
            self.sort_papers_by_title()
        
        start_time = time.time()
        results = []
        keyword_lower = keyword.lower()
        
        # Binary search for exact title matches
        left, right = 0, len(self.sorted_papers) - 1
        
        while left <= right:
            mid = (left + right) // 2
            title_lower = self.sorted_papers[mid].title.lower()
            
            if keyword_lower in title_lower:
                # Found a match, check surrounding items
                results.append(self.sorted_papers[mid])
                
                # Check items before
                i = mid - 1
                while i >= 0 and keyword_lower in self.sorted_papers[i].title.lower():
                    results.append(self.sorted_papers[i])
                    i -= 1
                
                # Check items after
                i = mid + 1
                while i < len(self.sorted_papers) and keyword_lower in self.sorted_papers[i].title.lower():
                    results.append(self.sorted_papers[i])
                    i += 1
                
                break
            elif keyword_lower < title_lower:
                right = mid - 1
            else:
                left = mid + 1
        
        # Also search in authors and journals using linear search
        for paper in self.papers:
            if ((keyword_lower in paper.author.lower() or 
                 (paper.journal and keyword_lower in paper.journal.lower())) and 
                paper not in results):
                results.append(paper)
        
        end_time = time.time()
        search_time = end_time - start_time
        return results, search_time
    
    def build_hash_tables(self):
        """Build hash tables for fast searching."""
        self.hash_table_title = {}
        self.hash_table_author = {}
        
        for paper in self.papers:
            # Create hash keys for title words
            title_words = paper.title.lower().split()
            for word in title_words:
                clean_word = ''.join(char for char in word if char.isalnum())
                if clean_word:
                    if clean_word not in self.hash_table_title:
                        self.hash_table_title[clean_word] = []
                    if paper not in self.hash_table_title[clean_word]:
                        self.hash_table_title[clean_word].append(paper)
            
            # Create hash keys for author words
            author_words = paper.author.lower().split()
            for word in author_words:
                clean_word = ''.join(char for char in word if char.isalnum())
                if clean_word:
                    if clean_word not in self.hash_table_author:
                        self.hash_table_author[clean_word] = []
                    if paper not in self.hash_table_author[clean_word]:
                        self.hash_table_author[clean_word].append(paper)
        
        self.hash_built = True
    
    def hash_search(self, keyword: str) -> Tuple[List[ResearchPaper], float]:
        """Hash table search for research papers."""
        if not self.hash_built:
            self.build_hash_tables()
        
        start_time = time.time()
        results = []
        keyword_lower = keyword.lower().strip()
        
        # Search in title hash table
        if keyword_lower in self.hash_table_title:
            results.extend(self.hash_table_title[keyword_lower])
        
        # Search in author hash table
        if keyword_lower in self.hash_table_author:
            for paper in self.hash_table_author[keyword_lower]:
                if paper not in results:
                    results.append(paper)
        
        # Partial match search
        for word in self.hash_table_title:
            if keyword_lower in word:
                for paper in self.hash_table_title[word]:
                    if paper not in results:
                        results.append(paper)
        
        for word in self.hash_table_author:
            if keyword_lower in word:
                for paper in self.hash_table_author[word]:
                    if paper not in results:
                        results.append(paper)
        
        end_time = time.time()
        search_time = end_time - start_time
        return results, search_time
    
    def search_papers(self, keyword: str) -> Dict[str, Tuple[List[ResearchPaper], float]]:
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
        print("=" * 70)
        
        results = self.search_papers(keyword)
        
        for algorithm_name, (papers, search_time) in results.items():
            print(f"\n📊 {algorithm_name.upper()}")
            print(f"   ⏱️  Search Time: {search_time:.6f} seconds")
            print(f"   📚 Found {len(papers)} paper(s)")
            
            if papers:
                for i, paper in enumerate(papers[:10], 1):  # Show first 10 results
                    print(f"      {i}. {paper}")
                    if paper.journal:
                        print(f"         Journal: {paper.journal}")
                if len(papers) > 10:
                    print(f"      ... and {len(papers) - 10} more papers")
            else:
                print("      No papers found.")
        
        # Performance comparison
        self.compare_performance(results)
    
    def compare_performance(self, results: Dict[str, Tuple[List[ResearchPaper], float]]):
        """Compare performance of different search algorithms."""
        print(f"\n⚡ PERFORMANCE COMPARISON ⚡")
        print("-" * 50)
        
        # Sort algorithms by speed
        sorted_algorithms = sorted(results.items(), key=lambda x: x[1][1])
        
        fastest_time = sorted_algorithms[0][1][1]
        
        for i, (algorithm, (papers, time_taken)) in enumerate(sorted_algorithms):
            if fastest_time > 0:
                speed_ratio = time_taken / fastest_time
                print(f"{i+1}. {algorithm}: {time_taken:.6f}s ({speed_ratio:.2f}x slower)")
            else:
                print(f"{i+1}. {algorithm}: {time_taken:.6f}s")
        
        print(f"\n🏆 Fastest: {sorted_algorithms[0][0]}")
        
        # Efficiency analysis
        print(f"\n📈 EFFICIENCY ANALYSIS:")
        print(f"   • Linear Search: O(n) - Simple but slow for large datasets")
        print(f"   • Binary Search: O(log n) - Fast but requires sorted data")
        print(f"   • Hash Search: O(1) average - Fastest for exact matches")
    
    def create_performance_test(self, num_papers: int = 10000):
        """Create a large dataset for performance testing."""
        print(f"\n🧪 Creating performance test with {num_papers} research papers...")
        
        # Clear existing papers
        self.papers = []
        self.is_sorted = False
        self.hash_built = False
        
        # Generate random research papers
        research_areas = [
            "Machine Learning", "Artificial Intelligence", "Computer Vision", "Natural Language Processing",
            "Data Science", "Cybersecurity", "Blockchain", "Quantum Computing", "IoT", "Cloud Computing",
            "Software Engineering", "Database Systems", "Computer Networks", "Human-Computer Interaction",
            "Robotics", "Bioinformatics", "Cryptography", "Distributed Systems", "Mobile Computing"
        ]
        
        authors = [
            "Dr. Sarah Johnson", "Prof. Michael Chen", "Dr. Emily Rodriguez", "Dr. David Kim",
            "Prof. Lisa Wang", "Dr. Robert Smith", "Dr. Jennifer Brown", "Prof. William Davis",
            "Dr. Maria Garcia", "Dr. James Wilson", "Prof. Patricia Miller", "Dr. Thomas Anderson",
            "Dr. Linda Taylor", "Prof. Christopher Lee", "Dr. Amanda White", "Dr. Kevin Martinez",
            "Prof. Rachel Thompson", "Dr. Steven Jackson", "Dr. Nancy Harris", "Prof. Mark Clark"
        ]
        
        for i in range(num_papers):
            area = random.choice(research_areas)
            author = random.choice(authors)
            title = f"Advanced {area} Techniques for Modern Applications {i+1}"
            year = random.randint(2020, 2024)
            journal = f"Journal of {area}"
            self.add_paper(title, author, year, journal)
        
        print(f"✅ Created {num_papers} test research papers")
    
    def display_library_stats(self):
        """Display library statistics."""
        print(f"\n📊 SR UNIVERSITY DIGITAL LIBRARY STATISTICS 📊")
        print("=" * 60)
        print(f"Total Research Papers: {len(self.papers)}")
        print(f"Sorted Status: {'Yes' if self.is_sorted else 'No'}")
        print(f"Hash Tables Built: {'Yes' if self.hash_built else 'No'}")
        
        if self.papers:
            years = [paper.year for paper in self.papers if paper.year]
            if years:
                print(f"Year Range: {min(years)} - {max(years)}")
            
            authors = set(paper.author for paper in self.papers)
            print(f"Unique Authors: {len(authors)}")
    
    def display_all_papers(self):
        """Display all research papers."""
        print(f"\n📚 ALL RESEARCH PAPERS IN SR UNIVERSITY LIBRARY 📚")
        print("=" * 70)
        
        if not self.papers:
            print("No papers available.")
            return
        
        for i, paper in enumerate(self.papers, 1):
            print(f"{i:3d}. {paper}")
            if paper.journal:
                print(f"     Journal: {paper.journal}")


def main():
    """Main function to demonstrate the SR University Digital Library."""
    library = DigitalLibrary()
    
    print("🏛️  SR UNIVERSITY DIGITAL LIBRARY SYSTEM 🏛️")
    print("=" * 60)
    print("Welcome to the advanced research paper search system!")
    
    # Try to load from files, create sample data if files don't exist
    library.load_from_csv("research_papers.csv")
    
    # Display library statistics
    library.display_library_stats()
    
    # Interactive search
    while True:
        print(f"\n{'='*70}")
        print("🔍 SEARCH OPTIONS:")
        print("1. Search by keyword")
        print("2. Performance test with large dataset")
        print("3. Display all research papers")
        print("4. Display library statistics")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            keyword = input("Enter search keyword: ").strip()
            if keyword:
                library.display_search_results(keyword)
            else:
                print("❌ Please enter a valid keyword.")
        
        elif choice == '2':
            num_papers = input("Enter number of papers for performance test (default 10000): ").strip()
            try:
                num_papers = int(num_papers) if num_papers else 10000
                library.create_performance_test(num_papers)
                
                # Test with common search terms
                test_keywords = ["Machine Learning", "Computer", "Dr.", "AI", "Security"]
                for keyword in test_keywords:
                    print(f"\n{'='*50}")
                    library.display_search_results(keyword)
            except ValueError:
                print("❌ Please enter a valid number.")
        
        elif choice == '3':
            library.display_all_papers()
        
        elif choice == '4':
            library.display_library_stats()
        
        elif choice == '5':
            print("👋 Thank you for using SR University Digital Library!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    main()
