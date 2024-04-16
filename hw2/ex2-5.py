def format_words(two_words):
    parts = two_words.split()
    first_word = parts[0]
    second_word = parts[1]
    return f"{second_word} {first_word}"


input_name = "Степанов Алексей"
output_name = format_words(input_name)
print(output_name)
