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
def phan_tu_can_hoan_vi():
    a = int(input("Nhập chỉ số phần tử thứ nhất: "))
    b = int(input("Nhập chỉ số phần tử thứ hai: "))
    return a,b
def hoan_vi(x,a,b):
    x[a],x[b] = x[b],x[a]
    print("list sau khi đã hoán vị: ",x)
    return x
def main():
    x = list_ngau_nhien()
    a,b = phan_tu_can_hoan_vi()
    hoan_vi(x,a,b)
if __name__=="__main__":
    main()   