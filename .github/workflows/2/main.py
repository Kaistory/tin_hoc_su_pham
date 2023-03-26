s1  = int(input())
s2  = int(input())
s3  = int(input())
s4  = int(input())


def ucln(a, b): # tim uoc chung lon nhat
    if (b == 0):
        return a;
    return ucln(b, a % b);
 

def bcnn(a, b): # tim boi chung nho nhat
    return int((a * b) / ucln(a, b));

#tim boi chung nho nhat doi mot 
value = bcnn(s1,s2)
value = bcnn(value,s3)
value = bcnn(value,s4)

print(value)