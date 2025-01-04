# Movie Recommendation System

This project is a Python-based movie recommendation system that suggests movies based on user ratings. By analyzing user preferences and similarities, the system provides tailored recommendations using data processing and graph-based relationships.

## Features

- **User-Centric Recommendations**: Generate personalized movie suggestions based on individual preferences.
- **Data-Driven Insights**: Utilizes user-movie ratings data for similarity detection.
- **Graph Algorithms**: Uses network analysis to uncover relationships between users and movies.
## Code Overview

### Files and Their Functions
1. **`recommend.py`**  
   This is the main script that executes the recommendation logic. It includes:
   - Importing and processing user-movie rating data.
   - Calculating user similarity based on ratings.
   - Generating movie recommendations.

2. **Dependencies**  
   The project uses the following Python libraries:
   - `networkx`: For graph-based similarity analysis.
   - `collections`: For efficient data handling.

### Example Dataset
The script uses a dictionary structure to store user ratings, such as:
```python
user_ratings = {
    "User1": {"Inception": 5, "The Matrix": 4, "Interstellar": 5},
    "User2": {"Inception": 4, "The Prestige": 4, "The Dark Knight": 5},

}
## How to Run the Code

### Prerequisites
- Python 3.8 or later
- Required libraries (install via `requirements.txt` if included, or install manually):
  ```bash
  pip install networkx
  
### Steps to Run
1. **Clone the Repository**:
   ```bash
   git clone https:     https://github.com/MARYUMQAISER/Movie-Recommendation-System                         
   cd movie-recommendation-system
   ```

2. **Prepare the Dataset**:  
   The dataset is pre-defined in the script (`user_ratings`). If you want to use your own dataset, modify the `user_ratings` dictionary in `recommend.py`.

3. **Run the Script**:  
   Execute the script in your terminal:
   ```bash
   python recommend.py
  

4. **View Recommendations**:  
   The script will output personalized movie recommendations for each user.

## Example Output

Given the sample ratings:
```python
user_ratings = {
    "User1": {"Inception": 5, "The Matrix": 4},
    "User2": {"The Prestige": 5, "Inception": 3},
}


The system generates output like:

Recommendations for User1: ['The Prestige']
Recommendations for User2: ['The Matrix']

## Contribution Guidelines

- Fork the repository.
- Submit a pull request with enhancements or fixes.
- Open issues for feature requests or bugs.

