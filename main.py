def display_text(path):
    with open(path) as f:
        file_contents = f.read()
        print(file_contents)

def word_count(path):
    wc = 0
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        return len(words)

def char_count(path):
    with open(path) as f:
        my_string = f.read()
        occurrences = {}
        for ch in my_string:
            if ch.isalpha():
                ch = ch.lower()
                if ch in occurrences:
                    occurrences[ch] += 1
                else:
                    occurrences[ch] = 1
    return occurrences

def sort_on(dict):
    return dict["num"]

def report(path):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count(path)} words found in the document\n")
    countlist = []
    for key, value in char_count(path).items():
        countlist.append({"ch": key, "num": value})
    
    countlist.sort(reverse=True, key=sort_on)
    for item in countlist:
        print(f"The '{item["ch"]}' character was found {item["num"]} times")

def main():
    book = "./books/frankenstein.txt"
    # display_text(book)
    # print(word_count(book))
    # print(char_count(book))
    report(book)

main()
