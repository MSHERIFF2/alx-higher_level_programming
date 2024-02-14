#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns the key with the largest integer value in the given dictionary.

    Args:
        a_dictionary (dict): A dictionary where keys are student names and values are integers.

    Returns:
        str or None: The key with the largest integer value, or None if the dictionary is empty.
    """
    if not a_dictionary:
        return None

    max_score = float('-inf')
    best_student = None

    for student, score in a_dictionary.items():
        if isinstance(score, int) and score > max_score:
            max_score = score
            best_student = student

    return best_student
