"""Programa para calcular la potencia
X^y"""

print("----------------------------------------------")
print("--------- POTENCIA X ^ y ---------------------")
print("----------------------------------------------")

# input
X=input("Digite el valor de X: ")
X=int (X)
y=input("Digite el valor de y: ")
y=int (y)

# processing
Z=X**y

# output 
print(str(X) + " elevado a la " +str(y)+ " es igual a " +str(Z))