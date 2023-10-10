def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            matches.append(i)

    return matches

text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")

matches = naive_string_match(text, pattern)

if matches:
    print(f"Pattern found at positions: {matches}")
else:
    print("Pattern not found in the text.")
