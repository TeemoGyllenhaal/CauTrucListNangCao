import random
random.seed(101)
def list_ngau_nhien():
    n = nhap_do_dai_list()
    y = [random.randint(-5, 5) for i in range (n)]
    print (y)
    return y
def nhap_do_dai_list():
    n = int(input("Nhập n: "))
    return n
def tim_kiem(x,y):
    z= []
    for i in range(len(y)):
        if x == y[i]:
            z.append(i)
    return z
def lon_hon_x(x,y):
    print("Giá trị lớn hơn x là: ",'\n')
    for i in range (len(y)):
        if x < y[i]:
            print("     -   Chỉ số: ",i,", Phần tử: ",y[i])
            print('\n')
def nho_hon_x(x,y):
    print("Giá trị nhỏ hơn x là: ",'\n')
    for i in range (len(y)):
        if x > y[i]:
            print("     -   Chỉ số: ",i,", Phần tử: ",y[i])
            print('\n')
def main():
    y = list_ngau_nhien()
    x = int(input("Nhập giá trị nguyên dương x: "))
    vitri = tim_kiem(x,y)
    if len(vitri) == 0:
        print("Không có phần tử xuất hiện")
    else:
        print("Các vị trí xuất hiện là: ", vitri)
    lon_hon_x(x,y)
    nho_hon_x(x,y)         
if __name__=="__main__":
    main()
