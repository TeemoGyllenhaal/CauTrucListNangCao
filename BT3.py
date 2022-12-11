import random
random.seed(101)
def list_ngau_nhien():
    n = nhap_do_dai_list()
    x = [random.randint(-5, 5) for i in range (n)]
    print (x)
    return x
def nhap_do_dai_list():
    n = int(input("Nhập n: "))
    return n
def trai_sang_phai(x):
    y = []
    for i in range(len(x)):
        y.append(x[i])
    print (y)
    return y
def phai_sang_trai(x):
    z = []
    for i in reversed(range(len(x))):
        z.append(x[i])
    print (z)
    return z
def main():
    x = list_ngau_nhien()
    trai_sang_phai(x)
    phai_sang_trai(x)
if __name__=="__main__":
    main()