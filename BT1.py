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
def vong_lap_list(x):
    for i in range (len(x)):
        print("Chỉ số: ",i,"Phần tử: ",x[i])
        print('\n')
def main():
    x = list_ngau_nhien()
    vong_lap_list(x)
if __name__=="__main__":
    main()
    