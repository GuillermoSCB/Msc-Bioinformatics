from bioinformatica import contar, PalabrasFrecuentes

#Parte 1
texto='ACAACTATGCATACTATCGGGAACTATCCT'
patron='ACTAT'
print(contar(texto, patron))


#Parte 2
texto1='ACGTTGCATGTCGCATGATGCATGAGAGCT'
k=4
print(PalabrasFrecuentes(texto1, k))