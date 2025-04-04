def split_and_join(line):
    # Split the line into a list of words
    words = line.split(" ")
    # Join the list into a single string with hyphens
    return "-".join(words)

# Sample input reading
line = input()
result = split_and_join(line)
print(result)
