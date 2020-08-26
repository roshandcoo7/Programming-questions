a = [1,2,3]
current = set()
def rec(available,current):
    if available:
        print(current)
    else:
        for i in available:
            temp_ava = available.remove(i)
            temp_curr = current.add(i)
            rec(temp_ava,temp_curr)
            rec(temp_ava,current)

rec(a,current)