n=input("donner une chaine de caractere : ")


a=list(n)

a.reverse()
s="".join(a)


if n==s :
    print("est un palindrome")
else :
    print("non palindrome") 