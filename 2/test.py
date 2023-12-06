def replace_vietnamese(input_string, search, replace):
    return input_string.replace("ban", "thực hành")

# Example usage
original_string = "haban"
search_term = "ban"
replacement = "thực hành"

result = replace_vietnamese(original_string, search_term, replacement)
print(result)

s = "haban"
s.replace_vietnamese("ban", "thực hành")
print(s)