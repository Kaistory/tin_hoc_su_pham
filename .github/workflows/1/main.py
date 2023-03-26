import math  # them thu vien math

n = int(input())

def sc(i) :
    value = math.sqrt(3) # tinh gia tri can 3
    # neu i = 1 in ra ket qua la can 3 
    if i == 1 :
         return value
    else:
        while i > 1: # tinh i - 1 lan tiep theo
            value = math.sqrt(3 + value)
            i -= 1
        return value

# math.sqrt(3) = can bac 2 cua 3
# voi i = 1 , cho value =  sqrt(3) -> sc = sqrt(3)
# voi i = 2 -> sc = sqrt(3 + sqrt(3)) = sqrt(3 + value) , gan value = sc 
# ....
    
    
def sd(i) :
    value = 1
    m = 1
    # neu i = 1 in ra ket qua la can 3 
    if i == 1 :
        return value
    else:
        while i > 1: # tinh i - 1 lan tiep theo
            value = value + value * m
            m += 1 
            i -= 1
        return value
    
# voi i = 1, cho value = m = 1 -> sd = 1
# voi i = 2, m = m + 1 = 2 -> sd = 1 + 1 * 2 = value + value * 2   = value + value * m , gan sd = value
# voi i = 3, m = m + 1 = 3 -> sd = value + value * 3 = value + value * m, gan sd = value
#....

print("%.3f" % sc(n)) # in so co 3 chu so thap phan
print("%.3f" % sd(n))