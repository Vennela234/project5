from backend.services.ada_eng import recommend_next_module


def recommend_next_module(user_id):
    # Placeholder logic
    user_scores = {"user123": 40, "user456": 85}
    score = user_scores.get(user_id, 70)

    if score < 50:
        return "intro-algebra"
    elif score < 80:
        return "intermediate-algebra"
    else:
        return "advanced-algebra"
