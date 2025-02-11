def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    words = file_contents.split()
    words_dict = {}

    for f in file_contents:
        if f.isupper():
            f = f.lower()
        if f in words_dict:
            words_dict[f] += 1
        else:
            words_dict[f] = 1

    def compare(k, v, i):
        while i >= 3:
            if ordered[i] > ordered[i-2]:
                temp = []
                temp.append(k)
                temp.append(v)
                ordered[i] = ordered[i-2]
                ordered[i-1] = ordered[i-3]
                ordered[i-2] = temp[1]
                ordered[i-3] = temp[0]
                i -= 2
            else:
                i -= 2

    ordered = []
    counter = 0
    for w in words_dict:
        if w.isalpha():
            ordered.append(w)
            ordered.append(words_dict[w])
            if counter == 0:
                counter = 1
            else:
                counter += 2
            if len(ordered) > 2:
                compare(w, words_dict[w], counter)
    
    for i in range(len(ordered)):
        if not i % 2:
            print(f"The '{ordered[i]}' character was found {ordered[i+1]} times")

main()