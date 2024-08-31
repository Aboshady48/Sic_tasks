with open('main.html', 'r') as file:
    hmCont = file.read()
hm_Str=str(hmCont)

def chck (hm_Str):
    sta=[]
    for tag in hm_Str.split():
        if tag.startswith("</"):
            if not sta:
                print(f"unclosing the tag {tag}")
        else:
            sta.append(tag)
            
        print("Your tags", sta)

chck(hm_Str)