def calPoints():
    ops = ["5","2","C","D","+"]

    score=[]
    for i in ops:
        if i=="+":
            score.append(score[len(score)-2]+score[len(score)-1])
        elif i=="D":
            score.append(score[len(score)-1]*2)
        elif i=="C":
            score.pop(len(score)-1)
        else:
            score.append(int(i))
    return(sum(score))




print("Output: "+str(calPoints()))