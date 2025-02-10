import pandas as pd

def analyze_performance(submission_data, historical_data):
    # Ensure data is in DataFrame format
    if isinstance(submission_data, dict):
        submission_data = pd.DataFrame([submission_data])
    if isinstance(historical_data, dict):
        historical_data = pd.DataFrame([historical_data])

    if submission_data.empty or historical_data.empty:
        return {"error": "Invalid data"}

    user_performance = submission_data.iloc[0]  # Take first entry

    insights = {
        "user_id": user_performance.get("user_id"),
        "score": user_performance.get("score"),
        "accuracy": user_performance.get("accuracy"),
        "speed": user_performance.get("speed"),
        "rank_text": user_performance.get("rank_text"),
        "better_than": user_performance.get("better_than"),
        "total_questions": user_performance.get("total_questions"),
        "correct_answers": user_performance.get("correct_answers"),
        "incorrect_answers": user_performance.get("incorrect_answers"),
    }

    return insights
