def is_palindrome(text):
    cleaned_text = str(text).lower()
    letters_only = ''.join(ch for ch in cleaned_text if ch.isalnum())
    return letters_only == letters_only[::-1]
