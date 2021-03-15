# zad1
# a=[1-x for x in range(1,11,1)]
# print(a)
# b=[4**i for i in range(8)]
# print(b)
# lista_c=[1,2,3,4,5,6,7,8,9,10]
# c=[x for x in lista_c if x % 2 == 0]
# print(c)
# zad2
# lista=[]
# for i in range(10):
#     liczba=int(input("Podaj elementy: \n"))
#     lista.append(liczba)
# print(lista)
# a=[x for x in lista if x % 2 == 0]
# print(a)
# zad3
# slownik={"frytki":"kg","keczup":"sztuki","ziemniaki":"kg","jajka":"sztuki"}
# a = {key: value for key, value in slownik.items() if value in "sztuki"}
# print(a)
# zad4
# def trpr(a, b, c):
#     if ((a**2)+(b**2)==(c**2)):
#         print("Jest to trojkat prostokatny")
#     else:
#         print("Nie jest to trojkat prostokatny")
#
# trpr(3, 4, 6)
# trpr(3, 4, 5)
# zad5
# def pole(a=2, b=4, h=5):
#     pole=((a+b)*h)/2
#     print(pole)
#
# pole(6, 9, 5)
# zad6
# def ciag(a=1, b=4, ile=3):
#     for i in range(ile):
#         a*=b
#         print(a)
#
# ciag()