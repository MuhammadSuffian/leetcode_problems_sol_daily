def countKeyChanges():
    s = "aAbBcC"
    if(s==None):
        return 0
    count=0
    i=0
    while(i!=len(s)-1):
        if(s[i].lower()!=s[i+1].lower()):
            count+=1
        i+=1
    print(count)

countKeyChanges()