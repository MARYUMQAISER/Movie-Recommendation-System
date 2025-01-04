
# Movie Recommendation System

This repository contains a Python-based movie recommendation system. The project leverages user ratings to suggest movies based on shared preferences and similar viewing patterns. By utilizing data structures such as graphs and dictionaries, the system efficiently identifies relationships between users and their rated movies.

## Features

- **Personalized Recommendations**: Suggests movies tailored to user preferences.
- **Graph-Based Analysis**: Employs network analysis techniques for identifying user-movie relationships.
- **Efficient Data Handling**: Uses dictionaries and collections to store and process ratings.

## How It Works

1. **User Data Input**: The system accepts a dataset of user-movie ratings.
2. **Similarity Calculation**: Identifies users with similar tastes based on their movie ratings.
3. **Recommendation Generation**: Suggests movies that users with similar preferences have rated highly.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python recommend.py
   ```

## Example

Given the following user ratings:
```python
user_ratings = {
    "User1": {"Inception": 5, "The Matrix": 4, "Interstellar": 5},
    "User2": {"Inception": 4, "The Prestige": 4, "The Dark Knight": 5},
    "User3": {"The Matrix": 5, "Interstellar": 4, "The Dark Knight": 4},
}

The system generates movie recommendations based on overlapping interests among users.

## Contributions

Contributions are welcome! Feel free to fork the repository and submit pull requests.


Happy coding and happy watching! 🎥🍿
