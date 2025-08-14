def recommend_books_by_genre(preferred_genre, num_recommendations=5):
    """
    Recommend books based on user's preferred genre using few-shot prompting.
    
    Args:
        preferred_genre (str): The user's preferred genre (e.g., 'mystery', 'fantasy', 'romance')
        num_recommendations (int): Number of books to recommend (default: 5)
    
    Returns:
        list: List of recommended books with titles and authors
    """
    
    # Few-shot examples for different genres
    genre_examples = {
        'mystery': [
            {'title': 'The Girl with the Dragon Tattoo', 'author': 'Stieg Larsson'},
            {'title': 'Gone Girl', 'author': 'Gillian Flynn'},
            {'title': 'The Silent Patient', 'author': 'Alex Michaelides'},
            {'title': 'Big Little Lies', 'author': 'Liane Moriarty'},
            {'title': 'The Woman in the Window', 'author': 'A.J. Finn'}
        ],
        'fantasy': [
            {'title': 'The Name of the Wind', 'author': 'Patrick Rothfuss'},
            {'title': 'Mistborn: The Final Empire', 'author': 'Brandon Sanderson'},
            {'title': 'The Way of Kings', 'author': 'Brandon Sanderson'},
            {'title': 'A Game of Thrones', 'author': 'George R.R. Martin'},
            {'title': 'The Lies of Locke Lamora', 'author': 'Scott Lynch'}
        ],
        'romance': [
            {'title': 'The Hating Game', 'author': 'Sally Thorne'},
            {'title': 'Beach Read', 'author': 'Emily Henry'},
            {'title': 'The Love Hypothesis', 'author': 'Ali Hazelwood'},
            {'title': 'Red, White & Royal Blue', 'author': 'Casey McQuiston'},
            {'title': 'The Spanish Love Deception', 'author': 'Elena Armas'}
        ],
        'science_fiction': [
            {'title': 'Dune', 'author': 'Frank Herbert'},
            {'title': 'The Martian', 'author': 'Andy Weir'},
            {'title': 'Project Hail Mary', 'author': 'Andy Weir'},
            {'title': 'The Three-Body Problem', 'author': 'Liu Cixin'},
            {'title': 'Neuromancer', 'author': 'William Gibson'}
        ],
        'thriller': [
            {'title': 'The Da Vinci Code', 'author': 'Dan Brown'},
            {'title': 'The Reversal', 'author': 'Michael Connelly'},
            {'title': 'The Last Thing He Told Me', 'author': 'Laura Dave'},
            {'title': 'Verity', 'author': 'Colleen Hoover'},
            {'title': 'The Guest List', 'author': 'Lucy Foley'}
        ],
        'historical_fiction': [
            {'title': 'The Book Thief', 'author': 'Markus Zusak'},
            {'title': 'All the Light We Cannot See', 'author': 'Anthony Doerr'},
            {'title': 'The Nightingale', 'author': 'Kristin Hannah'},
            {'title': 'The Tattooist of Auschwitz', 'author': 'Heather Morris'},
            {'title': 'The Alice Network', 'author': 'Kate Quinn'}
        ]
    }
    
    # Convert genre to lowercase for case-insensitive matching
    preferred_genre = preferred_genre.lower()
    
    # Check if the genre exists in our examples
    if preferred_genre in genre_examples:
        # Return the requested number of recommendations
        return genre_examples[preferred_genre][:num_recommendations]
    else:
        # If genre not found, provide a general recommendation
        general_recommendations = [
            {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
            {'title': '1984', 'author': 'George Orwell'},
            {'title': 'Pride and Prejudice', 'author': 'Jane Austen'},
            {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
            {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger'}
        ]
        return general_recommendations[:num_recommendations]

def display_recommendations(genre, recommendations):
    """
    Display book recommendations in a formatted way.
    
    Args:
        genre (str): The genre requested
        recommendations (list): List of book recommendations
    """
    print(f"\n📚 Book Recommendations for '{genre.title()}' Genre:")
    print("=" * 50)
    
    for i, book in enumerate(recommendations, 1):
        print(f"{i}. '{book['title']}' by {book['author']}")
    
    print("=" * 50)

# Example usage and demonstration
if __name__ == "__main__":
    # Test the function with different genres
    test_genres = ['mystery', 'fantasy', 'romance', 'science_fiction', 'thriller', 'historical_fiction']
    
    print("🎯 Book Recommendation System using Few-Shot Prompting")
    print("=" * 60)
    
    for genre in test_genres:
        recommendations = recommend_books_by_genre(genre, 3)
        display_recommendations(genre, recommendations)
    
    # Interactive example
    print("\n🔍 Interactive Example:")
    user_genre = input("Enter your preferred genre: ")
    user_recommendations = recommend_books_by_genre(user_genre, 5)
    display_recommendations(user_genre, user_recommendations)
