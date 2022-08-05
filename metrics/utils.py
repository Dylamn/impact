def calculate_note(score: int) -> str:
    """Transform a given score into a note (e.g. A, B, C, etc...)"""
    if score > 80:
        note = 'A'
    elif score > 40:
        note = 'B'
    else:
        note = 'C'

    return note


def calculate_metric_score(
        value: int, good_threshold: int, bad_threshold: int
) -> int:
    """Calculate the score for a given value on 100."""
    score = round(
        (bad_threshold - value) * 100 / (bad_threshold - good_threshold)
    )

    if score > 100:
        score = 100
    elif score < 0:
        score = 0

    return score
