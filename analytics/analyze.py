# analytics/analyze.py

def analyze_transcript(transcript_path):
    with open(transcript_path, 'r', encoding='utf-8') as f:
        text = f.read()

    word_count = len(text.split())
    line_count = len(text.strip().split('\n'))

    return {
        "word_count": word_count,
        "line_count": line_count
    }
