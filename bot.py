import random
import re

# Expanded book data with more genres
book_data = {
    "fiction": [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "description": "A novel set in the Roaring Twenties that explores themes of wealth, society, and the American Dream."},
        {"title": "1984", "author": "George Orwell", "description": "A dystopian novel about a totalitarian regime that uses surveillance, censorship, and propaganda to control its citizens."},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "description": "A novel that deals with serious issues like racial injustice and moral growth through the eyes of a young girl in the South."}
    ],
    "non-fiction": [
        {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "description": "An exploration of the history and impact of the human species from the Stone Age to the modern age."},
        {"title": "Educated", "author": "Tara Westover", "description": "A memoir about a woman who grows up in a strict and abusive household in rural Idaho and eventually escapes to learn about the wider world through education."},
        {"title": "Becoming", "author": "Michelle Obama", "description": "The memoir of the former First Lady of the United States, detailing her experiences growing up, her time in the White House, and her public life."}
    ],
    "mystery": [
        {"title": "Gone Girl", "author": "Gillian Flynn", "description": "A thriller about a woman's mysterious disappearance and the dark secrets that are revealed as her husband becomes the prime suspect."},
        {"title": "The Girl with the Dragon Tattoo", "author": "Stieg Larsson", "description": "A gripping mystery involving a journalist and a hacker who investigate a wealthy family's dark secrets."},
        {"title": "Big Little Lies", "author": "Liane Moriarty", "description": "A novel about a group of women whose seemingly perfect lives unravel to reveal hidden secrets and a tragic crime."}
    ],
    "fantasy": [
        {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "description": "The first book in the Harry Potter series, following a young wizard's adventures at Hogwarts School of Witchcraft and Wizardry."},
        {"title": "The Name of the Wind", "author": "Patrick Rothfuss", "description": "A fantasy novel that tells the story of a young man who grows up to become a legendary figure known as Kvothe."},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "description": "A classic fantasy adventure about a hobbit named Bilbo Baggins who embarks on a quest to help a group of dwarves reclaim their homeland."}
    ],
    "science fiction": [
        {"title": "Dune", "author": "Frank Herbert", "description": "A science fiction epic set in a distant future where noble families vie for control of the desert planet Arrakis and its valuable resource, spice."},
        {"title": "Neuromancer", "author": "William Gibson", "description": "A seminal cyberpunk novel that follows a washed-up computer hacker hired to pull off the ultimate hack."},
        {"title": "Ender's Game", "author": "Orson Scott Card", "description": "A novel about a young boy trained in a military school to fight off an alien invasion."}
    ],
    "romance": [
        {"title": "Pride and Prejudice", "author": "Jane Austen", "description": "A classic romance novel that explores the issues of class, marriage, and morality in early 19th-century England."},
        {"title": "The Notebook", "author": "Nicholas Sparks", "description": "A love story that spans decades, focusing on a couple whose love story is tested by life's challenges."},
        {"title": "Me Before You", "author": "Jojo Moyes", "description": "A contemporary romance about a young woman who becomes the caregiver for a man with a debilitating injury, leading to an unexpected relationship."}
    ],
    "historical fiction": [
        {"title": "The Book Thief", "author": "Markus Zusak", "description": "A story set in Nazi Germany, narrated by Death, about a young girl who steals books and shares them with others during the war."},
        {"title": "All the Light We Cannot See", "author": "Anthony Doerr", "description": "A novel about a blind French girl and a German boy whose lives intersect during World War II."},
        {"title": "The Nightingale", "author": "Kristin Hannah", "description": "A story about two sisters in France during World War II and their struggle to survive and resist the German occupation."}
    ]
}

def get_book_recommendations(genre):
    genre = genre.lower()
    if genre in book_data:
        recommendations = random.choice(book_data[genre])
        return f"Title: {recommendations['title']}\nAuthor: {recommendations['author']}\nDescription: {recommendations['description']}"
    else:
        return f"Sorry, I don't have recommendations for the genre '{genre}'. Please try another genre. Available genres are: {list_genres()}."

def list_genres():
    return ", ".join(book_data.keys())

def list_books(genre):
    genre = genre.lower()
    if genre in book_data:
        books = book_data[genre]
        book_list = "\n\n".join([f"Title: {book['title']}\nAuthor: {book['author']}\nDescription: {book['description']}" for book in books])
        return f"Here is a list of books in the genre '{genre}':\n\n{book_list}"
    else:
        return f"Sorry, I don't have information about the genre '{genre}'. Please try another genre. Available genres are: {list_genres()}."

def list_all_books():
    all_books = []
    for genre, books in book_data.items():
        all_books.extend([f"Genre: {genre}\nTitle: {book['title']}\nAuthor: {book['author']}\nDescription: {book['description']}" for book in books])
    return "Here is a complete list of all books:\n\n" + "\n\n".join(all_books)

def handle_query(user_input, user_name):
    user_input = user_input.lower().strip()
    
    # Using regex to find genre for recommendations
    genre_match = re.search(r'suggest books for (?:genre )?(\w+)', user_input)
    if genre_match:
        genre = genre_match.group(1).lower()
        return f"{user_name}, here are some book recommendations for the genre '{genre}':\n" + get_book_recommendations(genre)
    
    # Using regex to list books for a genre
    if re.search(r'list all books in (?:genre )?(\w+)', user_input):
        genre_match = re.search(r'list all books in (?:genre )?(\w+)', user_input)
        if genre_match:
            genre = genre_match.group(1).lower()
            return list_books(genre)
    
    # Handle request for a complete list of all books
    if "list all books" in user_input or "complete list of books" in user_input:
        return list_all_books()
    
    # Handle requests for genre information
    if re.search(r'tell me about\s+(\w+)', user_input):
        genre_match = re.search(r'tell me about\s+(\w+)', user_input)
        if genre_match:
            genre = genre_match.group(1).lower()
            return f"{user_name}, I can provide book recommendations for the following genres: {list_genres()}."
    
    # Handle request for list of genres
    if "genres" in user_input:
        return f"{user_name}, available genres are: {list_genres()}."
    
    return f"{user_name}, sorry, I didn't understand that. Try asking for book recommendations by specifying a genre, information about genres, a list of available genres, or a complete list of books."

def chatbot():
    print("Welcome to the Book Recommendation Chatbot!")
    user_name = input("Before we begin, what's your name? ").strip()
    
    if not user_name:
        user_name = "Reader"
    
    print(f"Hello, {user_name}! I can recommend books based on your genre preferences or provide information about different genres.")

    while True:
        user_input = input("\nYou: ").strip().lower()
        
        if user_input in ["exit", "quit", "bye"]:
            print(f"Goodbye, {user_name}! Happy reading!")
            break
        
        response = handle_query(user_input, user_name)
        print(response)

if __name__ == "__main__":
    chatbot()
