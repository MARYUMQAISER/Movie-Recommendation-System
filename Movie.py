import networkx as nx
from collections import defaultdict

# Sample user-movie ratings data
user_ratings = {
    "User1": {"Inception": 5, "The Matrix": 4, "Interstellar": 5},
    "User2": {"Inception": 4, "The Prestige": 4, "The Dark Knight": 5},
    "User3": {"The Matrix": 5, "Interstellar": 4, "The Dark Knight": 4},
    "User4": {"The Prestige": 5, "Inception": 3, "The Dark Knight": 4},
    "User5": {"Superbad": 3, "Step Brothers": 4, "The Hangover": 5},
    "User6": {"Schindler's List": 4, "The King's Speech": 5, "12 Years a Slave": 4},
    "User7": {"The Conjuring": 5, "It": 4, "A Quiet Place": 3},
    "User8": {"Mad Max: Fury Road": 5, "Gladiator": 4}
}

# Movie genres
genre_movies = {
    "horror": ["The Conjuring", "It", "A Quiet Place"],
    "comedy": ["Superbad", "Step Brothers", "The Hangover"],
    "history": ["Schindler's List", "The King's Speech", "12 Years a Slave"],
    "sci-fi": ["Inception", "The Matrix", "Interstellar"],
    "action": ["The Dark Knight", "Mad Max: Fury Road", "Gladiator"]
}

# Build a graph where nodes are users and movies, and edges represent ratings
graph = nx.Graph()

# Add edges based on user ratings
for user, movies in user_ratings.items():
    for movie, rating in movies.items():
        if rating is not None and isinstance(rating, (int, float)):
            graph.add_edge(user, movie, weight=rating)

# Collaborative filtering: find similar users based on common movies
def find_similar_users(target_user):
    similar_users = defaultdict(float)

    # Find movies rated by the target user
    target_movies = [n for n in graph.neighbors(target_user) if n not in user_ratings[target_user]]

    for movie in target_movies:
        for user in graph.neighbors(movie):
            if user != target_user and user in user_ratings:
                similar_users[user] += graph[target_user][movie]['weight'] * graph[user][movie]['weight']

    return sorted(similar_users.items(), key=lambda x: x[1], reverse=True)

# Graph-based recommendation: suggest movies liked by similar users
def recommend_movies(target_user, genre=None, num_recommendations=3):
    movie_scores = defaultdict(float)

    if genre:
        genre_specific_movies = genre_movies.get(genre, [])
        for movie in genre_specific_movies:
            if movie not in user_ratings[target_user]:
                for user in user_ratings:
                    if movie in user_ratings[user]:
                        movie_scores[movie] += user_ratings[user][movie]
    else:
        similar_users = find_similar_users(target_user)
        for user, similarity in similar_users:
            for movie in user_ratings[user]:
                if movie not in user_ratings[target_user]:
                    movie_scores[movie] += similarity * user_ratings[user][movie]

    # Sort movies by score and return top recommendations
    recommended_movies = sorted(movie_scores.items(), key=lambda x: x[1], reverse=True)
    return [movie for movie, score in recommended_movies[:num_recommendations]]

# Ask user for genre preference
def get_genre_preference():
    print("Which kind of movies do you like? Options: horror, comedy, history, sci-fi, action")
    genre = input("Enter your preferred genre: ").strip().lower()
    if genre not in genre_movies:
        print("Invalid genre. Showing recommendations without genre preference.")
        genre = None
    return genre

# Display all ratings for a selected movie
def display_movie_ratings(movie):
    print(f"Ratings for '{movie}':")
    for user, movies in user_ratings.items():
        if movie in movies:
            print(f"{user}: {movies[movie]}")

# Example usage
def main():
    user_to_search = "User1"
    preferred_genre = get_genre_preference()
    recommendations = recommend_movies(user_to_search, genre=preferred_genre, num_recommendations=3)

    print(f"Movies recommended for '{user_to_search}' with genre '{preferred_genre if preferred_genre else 'any'}':")
    if recommendations:
        print(recommendations)
        selected_movie = input("Select a movie from the recommendations to see its ratings: ").strip()
        if selected_movie in recommendations:
            display_movie_ratings(selected_movie)
        else:
            print("Selected movie is not in the recommendations.")
    else:
        print("No recommendations available for the selected genre.")

if __name__ == "__main__":
    main()
