import re

def extract_urls(text):
    
    url_pattern = r'https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?)?'
    comprehensive_pattern = r'(?:https?|ftp|mailto|file|gopher|news|nntp|telnet|wais|prospero):\/\/[^\s<>"{}|\\^`\[\]]+'
    urls = re.findall(comprehensive_pattern, text, re.IGNORECASE)
    
    return urls

def extract_urls_with_validation(text):
    # Basic URL pattern
    url_pattern = r'https?://[^\s<>"{}|\\^`\[\]]+'
    
    # Find all matches
    raw_urls = re.findall(url_pattern, text, re.IGNORECASE)
    
    # Clean and validate URLs
    cleaned_urls = []
    for url in raw_urls:
        # Remove trailing punctuation that's not part of the URL
        cleaned_url = re.sub(r'[.,;:!?]+$', '', url)
        
        # Basic validation - ensure URL has at least a domain
        if re.search(r'https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', cleaned_url):
            cleaned_urls.append(cleaned_url)
    
    return cleaned_urls

def main():
    """Main function to demonstrate URL extraction."""
    
    # Example text with various URLs
    sample_text = """
    Here are some example URLs:
    - https://www.example.com
    - http://test.org/path?param=value#section
    - https://subdomain.example.co.uk
    - ftp://ftp.example.net/files/
    - mailto:user@example.com
    - https://example.com/path/to/page.html
    
    Some invalid URLs that shouldn't be extracted:
    - www.example.com (missing protocol)
    - example.com (missing protocol)
    - https:// (incomplete URL)
    
    More valid URLs:
    - https://api.github.com/users/username
    - http://localhost:3000/app
    - https://docs.python.org/3/library/re.html
    """
    
    print("=== URL Extraction Demo ===\n")
    print("Sample text:")
    print(sample_text)
    
    print("\n=== Extracted URLs (Basic) ===")
    urls_basic = extract_urls(sample_text)
    for i, url in enumerate(urls_basic, 1):
        print(f"{i}. {url}")
    
    print("\n=== Extracted URLs (With Validation) ===")
    urls_validated = extract_urls_with_validation(sample_text)
    for i, url in enumerate(urls_validated, 1):
        print(f"{i}. {url}")
    
    # Interactive mode
    print("\n=== Interactive Mode ===")
    print("Enter your own text to extract URLs (type 'quit' to exit):")
    
    while True:
        user_input = input("\nEnter text: ").strip()
        
        if user_input.lower() == 'quit':
            break
        
        if user_input:
            found_urls = extract_urls_with_validation(user_input)
            
            if found_urls:
                print(f"\nFound {len(found_urls)} URL(s):")
                for i, url in enumerate(found_urls, 1):
                    print(f"{i}. {url}")
            else:
                print("No URLs found in the text.")
        else:
            print("Please enter some text.")

if __name__ == "__main__":
    main()
