def get_word_count(book_contents):
    word_count = len(book_contents.split())
    return word_count

def get_char_count(book_contents):
    book_dict = {}
    for chr in book_contents:
        low_chr = chr.lower()
        if low_chr not in book_dict:
            book_dict[low_chr] = 1
        else:
            book_dict[low_chr] += 1
    return book_dict

def sort_on(items):
    return items["count"]

def sorted_dict_list(book_dict):
    dict_list = []
    for key in book_dict:
        alpha_dict = {}
        if key.isalpha():
            alpha_dict["char"] = key
            alpha_dict["count"] = book_dict[key]
            dict_list.append(alpha_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
            
    

