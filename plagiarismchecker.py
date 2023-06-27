import Levenshtein

def calculate_similarity(text1, text2):
    distance = Levenshtein.distance(text1, text2)
    max_length = max(len(text1), len(text2))
    similarity = 1 - (distance / max_length)
    return similarity

def check_plagiarism(text1, text2, threshold=0.8):
    similarity = calculate_similarity(text1, text2)
    if similarity >= threshold:
        return f"Plagiarism detected! Similarity: {similarity}"
    else:
        return "No plagiarism detected."
#This is the original text.
# Example usage:
original_text = "hey this is adi."
suspicious_text = "hey this is not adi."

result = check_plagiarism(original_text, suspicious_text)
print(result)






