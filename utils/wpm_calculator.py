import re


FILLER_WORDS = {
    "um", "uh", "hmm", "ah", "er", "like"
}


def clean_words(transcript):
    words = re.findall(r"\b[\w']+\b", transcript.lower())

    valid_words = [
        word for word in words
        if word not in FILLER_WORDS
    ]

    return valid_words


def calculate_wpm(transcript, speaking_duration_seconds):
    valid_words = clean_words(transcript)

    word_count = len(valid_words)

    if speaking_duration_seconds <= 0:
        return 0

    duration_minutes = speaking_duration_seconds / 60

    return round(word_count / duration_minutes)
