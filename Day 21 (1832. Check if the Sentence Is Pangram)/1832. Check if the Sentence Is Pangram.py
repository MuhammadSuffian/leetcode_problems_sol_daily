def checkIfPangram():
    sentence="thequickbrownfoxjumpsoverthelazydog"
    for a in range(ord('a'), ord('z')+1):
        if chr(a) not in sentence:
            return False
        
    return True

print("Pangram: "+str(checkIfPangram()))