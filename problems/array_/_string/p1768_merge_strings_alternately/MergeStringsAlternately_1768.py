def mergeAlternately(word1: str, word2: str) -> str:
    merged = []
    i, j = 0, 0
    len1, len2 = len(word1), len(word2)

    # 1. Check word length
    if len1 < 1 or len2 < 1:
        print("Break: word1.length or word2.length < 1")
        raise ValueError("word1.length or word2.length < 1, Length must be between 1 and 100.")
        return ""
    elif len1 > 100 or len2 > 100:
        print("Break: word1.length or word2.length > 100")
        raise ValueError("word1.length or word2.length > 100, word1.length or word2.length < 1, Length must be between 1 and 100.")
        return ""

    # 2. Check lowercase
    if not word1.islower() or not word2.islower():
        print("Break: word1 and word2 must consist of lowercase English letters.")
        raise ValueError("Strings must contain only lowercase English letters.")
        return ""

    # 3. Ensures characters are purely alphabetic (A-Z, a-z)
    if not word1.isalpha()  or not word2.isalpha():
        print("Break: Strings must contain only English letters (no numbers or special characters like !, ?, %).")
        raise ValueError("Strings must contain only lowercase English letters.")
        return ""

    # Alternate characters while both strings have remaining characters
    while i < len1 and j < len2:
        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1
    
    # Append remaining characters from word1 (if any)
    if i < len1:
        merged.append(word1[i:])
        
    # Append remaining characters from word2 (if any)
    if j < len2:
        merged.append(word2[j:])
        
    return "".join(merged)

# --- MANUAL TESTING BLOCK ---
def manual_test_wrapper(word1: str, word2: str) -> str:
    """Helper wrapper to print messages and return "" instead of crashing on error."""
    try:
        return mergeAlternately(word1, word2)
    except ValueError as e:
        print(f"Break: {e}")
        return ""


if __name__ == "__main__":
    print("--- Valid Tests ---")
    print(manual_test_wrapper("abc", "pqr"))   # Output: "apbqcr"
    print(manual_test_wrapper("ab", "pqrs"))   # Output: "apbqrs"
    print(manual_test_wrapper("abcd", "pq"))   # Output: "apbqcd"

    print("\n--- Invalid Tests (Manual handling: Returns \"\") ---")
    print(manual_test_wrapper("", "pqr"))      # Break: Length must be between 1 and 100. -> ""
    print(manual_test_wrapper("abc", ""))      # Break: Length must be between 1 and 100. -> ""
    print(manual_test_wrapper("ABC", "pqr"))   # Break: Strings must contain only lowercase English letters. -> ""
    print(manual_test_wrapper("ab!", "pqr"))   # Break: Strings must contain only lowercase English letters. -> ""
    print(manual_test_wrapper("abc!", "pq2"))  # Break: Strings must contain only lowercase English letters. -> ""