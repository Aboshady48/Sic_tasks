def bubble_chack(str1,str2):
    lit1=list(str1)
    lit2=list(str2)
    
    comp=len(lit1)

    for i in range (comp):
        for j in range(comp - i -1):
            if lit1[j]>lit1[j + 1]:
                lit1[j], lit1[j + 1] = lit1[j + 1], lit1[j]
                return True
            elif lit2[i] > lit2[j + 1]:
                lit2[j], lit2[j + 1] = lit2[j + 1], lit2[j]
                return True
    return lit1==lit2

word1=input("Enter the first word: ")
word2=input("Enter the second word: ")

print(bubble_chack(word1,word2))