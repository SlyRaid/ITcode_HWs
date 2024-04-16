def format_name(full_name):
    parts = full_name.split()
    last_name = parts[0]
    initials = ' '.join([f"{name[0]}." for name in parts[1:]])
    result = f"{last_name} {initials}"
    return result


input_name = "Степанов Алексей Иванович"
output_name = format_name(input_name)
print(output_name)
