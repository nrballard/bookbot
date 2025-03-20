def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    c_dict = {}
    for c in text:
        if c.lower() in c_dict:
            c_dict[c.lower()] += 1
        else:
            c_dict[c.lower()] = 1
    return c_dict

def sort_on(dict):
    return dict["num"]

def sort_ccount(ccount):
    char_list = []
    for item in ccount:
        cdict = {}
        cdict["char"] = item
        cdict["num"] = ccount[item]
        char_list.append(cdict)
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list