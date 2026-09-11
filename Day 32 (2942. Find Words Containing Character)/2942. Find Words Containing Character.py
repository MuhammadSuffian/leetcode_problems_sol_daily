def findWordsContaining():
    words = ["abc","bcd","aaaa","cbc"]
    x = "a"
    count=[]
    for i in range(len(words)):
        if x in words[i]:
            count.append(i)
    print(count)
findWordsContaining()