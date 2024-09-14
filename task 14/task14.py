def staircase(n,m=None):
    #memorizion case in dp this case i hade shearch to know it
    if m == None :
        m={}
    #base case
    if n <=1:
        return 1
    #recrusive case
    if n not in m:
        m [n] = staircase(n-1,m) + staircase(n-2,m)
    return m[n]

print(staircase(500))

#time complixty o(2^n) mybea