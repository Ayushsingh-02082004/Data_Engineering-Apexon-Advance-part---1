sentence = "Hey i am learning python tommorrow is my review and i will get good track score than last time . "

word = sentence.split()
word_count = len(word)
longest_word = max(word , key=len)


print(f"word count is {word_count}  Longest word is {longest_word} .")