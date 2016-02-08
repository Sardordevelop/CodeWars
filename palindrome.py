def longest_palindrome(text):
    text = text.lower()
    results = []

    for i in range(len(text)):
        for j in range(0, i):
            chunk = text[j:i + 1]

            if chunk == chunk[::-1]:
                results.append(chunk)


    return 1 if (len(results) == 0) else len(max(results, key=len))


print(longest_palindrome("abcdefghba"))