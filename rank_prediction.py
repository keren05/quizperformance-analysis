import numpy as np

def predict_neet_rank(analysis_results):
    if "better_than" not in analysis_results or "total_questions" not in analysis_results:
        return "Insufficient data for prediction."

    better_than = analysis_results["better_than"]
    total_students = 2000000  # Assumed number of NEET candidates

    estimated_rank = total_students - ((better_than / 100) * total_students)
    return int(estimated_rank)
