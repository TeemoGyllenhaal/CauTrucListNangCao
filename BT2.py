import random
random.seed(102)
def list_ngau_nhien():
    n = nhap_do_dai_list()
    x = [random.randint(-5, 5) for i in range (n)]
    print (x)
    return x
def nhap_do_dai_list():
    n = int(input("Nhập n: "))
    return n
def cong_don(x):
    S = 0
    for i in range(len(x)):
        S = S + x[i]
    print ("Tổng cộng dồn: ",S)
    return S
def nhan_don(x):
    P = 1
    for i in range(len(x)):
        P = P * x[i]
    print ("Tích nhân dồn: ",P)
    return P
def main():
    x = list_ngau_nhien()
    cong_don(x)
    nhan_don(x)
if __name__=="__main__":
    main()