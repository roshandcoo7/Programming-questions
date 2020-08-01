def most_freq_ele(lst):
    return max(set(lst), key = lst.count) 

def count_dig(num,lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] == num:
            count += 1
    return count

def count_vector(chars,string):
    freq = [0]*len(chars)
    for i in range(len(chars)):
        freq[i] = count_dig(chars[i],string)
    return freq

def sherlock(freq_vec):
    most = most_freq_ele(freq_vec)
    change_freq = [ abs(i-most) for i in freq_vec ]

    if sum(change_freq) == 0:
        print('YES')

    elif sum(change_freq) == most-1 or sum(change_freq) == 1:
        print('YES')
    else:
        print('NO')


string = str(input())
chars = sorted(list(set(string)))

# print(string)
# print(chars)
freq_vec = count_vector(chars,string)
# print(freq_vec)
sherlock(freq_vec)




