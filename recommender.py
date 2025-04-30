import json
from math import sqrt

# Load data from JSON file
with open("1000DATASET_CLEANED.json") as f:
    dataFrame = json.load(f)

def sim_distance(requirements, prefs, person1, person2):
    """
    Calculate similarity score between two persons based on skills
    Returns: 1 / (1 + Euclidean distance)
    """
    skills = ["HTML", "Python", "Java", "C", "JavaScript", "SQL"]
    
    # Calculate sum of squares of differences
    sum_of_squares = 0
    for skill in skills:
        # Handle missing skills with default value 0
        val1 = requirements[person1].get(skill, 0)
        val2 = prefs[person2].get(skill, 0)
        sum_of_squares += (val1 - val2)**2
    
    # Return similarity score
    return 1 / (1 + sqrt(sum_of_squares))

def topMatches(requirements, prefs, person, n, similarity=sim_distance):
    """
    Returns the top n matches for person from the prefs dictionary
    """
    # Calculate similarity scores
    scores = []
    for other in prefs:
        if other != person:
            try:
                score = similarity(requirements, prefs, person, other)
                scores.append((score, other))
            except Exception:
                # Skip candidates with problematic data
                continue
    
    # Sort by score in descending order
    scores.sort(reverse=True)
    
    # Return top n results
    return scores[:n]
