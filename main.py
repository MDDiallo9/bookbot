with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    """ print(len(file_contents.split())) """
    result = {}
    for char in file_contents.lower():
        if char in result and char.isalpha() :
            result[char] += 1
        else:
            result[char] = 0
            result[char] += 1
    print(f"{len(file_contents.split())} words found in this document")
    for char in result:
        print(f"{char} character was found {result[char]} times")
    print("--- END REPORT ---")