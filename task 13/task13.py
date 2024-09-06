'''
change=float(input("enter change: "))
korean_coins = [500, 100, 50, 10]
count = 0
for coin in korean_coins:
        count += change // coin
        change %= coin
print(change)
'''
def chan(change,arr_of_coin):
    
    #base case
    if change==0:
        return 0
    #recrusive case
    max_val=arr_of_coin[0]
    result_num=change%max_val
    num=change//max_val
    return num * chan(result_num,arr_of_coin[1:])
    
korean_coins=[500,100,50,10]
money=float(input("Enter your change: "))
answer=chan(money,korean_coins)
print(answer)
