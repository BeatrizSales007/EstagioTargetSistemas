# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

string = input("Digite alguma string: ")

def inverte_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

print(inverte_string(string))