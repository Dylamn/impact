def calculate_note(score: int) -> str:
    """Transform a given score into a note (e.g. A, B, C, etc...)"""
    if score > 80:
        note = 'A'
    elif score > 40:
        note = 'B'
    else:
        note = 'C'

    return note
