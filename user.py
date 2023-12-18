# Sample user-item preferences
user_preferences = {
    'User1': {'Action': 5, 'Drama': 4, 'Comedy': 2, 'Sci-Fi': 3},
    'User2': {'Action': 3, 'Drama': 5, 'Comedy': 4, 'Sci-Fi': 2},
    'User3': {'Action': 2, 'Drama': 3, 'Comedy': 5, 'Sci-Fi': 4},
}

# Sample item features
item_features = {
    'Movie1': {'Action': 4, 'Drama': 5, 'Comedy': 2, 'Sci-Fi': 3},
    'Movie2': {'Action': 3, 'Drama': 4, 'Comedy': 5, 'Sci-Fi': 2},
    'Movie3': {'Action': 5, 'Drama': 2, 'Comedy': 3, 'Sci-Fi': 4},
}

# Function to calculate the similarity between two preferences
def calculate_similarity(user_prefs, item_feats):
    common_features = set(user_prefs.keys()) & set(item_feats.keys())
    if not common_features:
        return 0  # No common features

    numerator = sum(user_prefs[feature] * item_feats[feature] for feature in common_features)
    user_norm = sum(val ** 2 for val in user_prefs.values()) ** 0.5
    item_norm = sum(val ** 2 for val in item_feats.values()) ** 0.5

    similarity = numerator / (user_norm * item_norm)
    return similarity

# Function to recommend items to a user based on preferences
def recommend_items(user_id, user_prefs, all_items):
    recommendations = []

    for item_id, item_feats in all_items.items():
        if item_id not in user_prefs:
            similarity = calculate_similarity(user_prefs, item_feats)
            recommendations.append((item_id, similarity))

    # Sort recommendations by similarity in descending order
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations

# Example: Recommend items for 'User1'
user_id_to_recommend = 'User1'
all_items_to_recommend = item_features

user_recommendations = recommend_items(user_id_to_recommend, user_preferences[user_id_to_recommend], all_items_to_recommend)

# Print top 5 recommendations
top_recommendations = user_recommendations[:5]
print(f"Top 5 recommendations for {user_id_to_recommend}: {top_recommendations}")


