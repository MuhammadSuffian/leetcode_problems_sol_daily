def judgeCircle():
    moves = "UD"

    pos=[]
    for i in moves:
        if pos==None:
            pos.append(i)
        else:
            if(i=="R"):
                if "L" in pos:
                    pos.remove("L")
                else:
                    pos.append(i)
            elif(i=="L"):
                if "R" in pos:
                    pos.remove("R")
                else:
                    pos.append(i)
            elif(i=="U"):
                if "D" in pos:
                    pos.remove("D")
                else:
                    pos.append(i)
            else:
                if "U" in pos:
                    pos.remove("U")
                else:
                    pos.append(i)
    if len(pos)==0:
        return True
    else: 
        return False
                    
            











print("Output: "+str(judgeCircle()))