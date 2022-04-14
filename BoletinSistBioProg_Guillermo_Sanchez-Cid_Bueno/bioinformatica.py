def ejercicio1(numBases, numGenes):
    ''' (int, int) -> float
    Calcula el número promedio de bases por gen
        Entrada: Número de bases y número de genes
        Salida: ratio del número de bases por gen
    '''
    result = numBases / numGenes
    return result


def ejercicio2(chain1, chain2):
    ''' (str, str) -> str
    Une dos cadenas de ADN y devuelve el producto
        Entrada: dos strings que representan cadenas de ADN
        Salida: cadena formada por la unión de dos cadenas
    '''
    return chain1 + chain2


def ejercicio3(dna):
    ''' str -> str
    Sustituye el caracter T por U en una cadena
        Entrada: string que representa una cadena de ADN
        Salida: string que representa una cadena de ARN
    '''
    chain = ''
    for base in dna:
        if base == 'T':
            chain += 'U'
        else:
            chain += base
    return chain


def ejercicio4(DNA):
    ''' str -> str
    Calcula la cadena complementaria a una cadena de ADN
        Entrada: string que representa una cadena de ADN
        Salida: string que representa una cadena de ADN complementaria a la del input
    '''
    comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    compDNA = ''
    for base in DNA:
        compDNA += comp[base]
    return compDNA


def ejercicio5(num1, num2):
    ''' (int, int) -> int
    Calcula cuál es el mayor de dos número
        Entrada: dos números enteros
        Salida: el mayor de los dos números introducidos
    '''
    if num1 > num2:
        return num1
    else:
        return num2


def ejercicio6(num1, num2, num3):
    ''' (int, int, int) -> int
    Ordena tres números de menor a mayor
        Entrada: tres números enteros
        Salida: lista de tres números ordenados de menor a mayor
    '''
    return sorted([num1, num2, num3])


def ejercicio7(codon):
    ''' str -> str
    Muestra el aminoácido que corresponde al codón introducido
        Entrada: string que representa un codón del código genético
        Salida: aminoácido correspondiente al codón una vez traducido
        '''
    if codon == 'UUU':
        print("Fenilalanina")
    elif codon == 'UUC':
        print("Fenilalanina")
    elif codon == 'UUA':
        print("Leucina")
    elif codon == 'UUG':
        print("Leucina")
    elif codon == 'UCA':
        print("Serina")
    elif codon == 'UCC':
        print("Serina")
    elif codon == 'UCG':
        print("Serina")
    elif codon == 'UCU':
        print("Serina")
    elif codon == 'UAU':
        print("Tirosina")
    elif codon == 'UAC':
        print("Tirosina")
    elif codon == 'UAA':
        print("STOP")
    elif codon == 'UAG':
        print("STOP")
    elif codon == 'UGU':
        print("Cisteína")
    elif codon == 'UGC':
        print("Cisteína")
    elif codon == 'UGA':
        print("STOP")
    elif codon == 'UGG':
        print("Triptófano")
    elif codon == 'CUA':
        print("Leucina")
    elif codon == 'CUC':
        print("Leucina")
    elif codon == 'CUG':
        print("Leucina")
    elif codon == 'CUU':
        print("Leucina")
    elif codon == 'CCA':
        print("Prolina")
    elif codon == 'CCC':
        print("Prolina")
    elif codon == 'CCG':
        print("Prolina")
    elif codon == 'CCU':
        print("Prolina")
    elif codon == 'CAU':
        print("Histidina")
    elif codon == 'CAC':
        print("Histidina")
    elif codon == 'CAA':
        print("Glutamina")
    elif codon == 'CAG':
        print("Glutamina")
    elif codon == 'AUA':
        print("Isoleucina")
    elif codon == 'AUC':
        print("Isoleucina")
    elif codon == 'AUU':
        print("Isoleucina")
    elif codon == 'AUG':
        print("Metionina")
    elif codon == 'ACA':
        print("Treonina")
    elif codon == 'ACC':
        print("Treonina")
    elif codon == 'ACG':
        print("Treonina")
    elif codon == 'ACU':
        print("Treonina")
    elif codon == 'AAC':
        print("Aparagina")
    elif codon == 'AAU':
        print("Aparagina")
    elif codon == 'AAA':
        print("Lisina")
    elif codon == 'AAU':
        print("Lisina")
    elif codon == 'AAU':
        print("Lisina")
    elif codon == 'AGU':
        print("Serina")
    elif codon == 'AGC':
        print("Serina")
    elif codon == 'AGA':
        print("Arginina")
    elif codon == 'AGG':
        print("Arginina")
    elif codon == 'GUA':
        print("Valina")
    elif codon == 'GUC':
        print("Valina")
    elif codon == 'GUG':
        print("Valina")
    elif codon == 'GUU':
        print("Valina")
    elif codon == 'GGA':
        print("Alanina")
    elif codon == 'GGC':
        print("Alanina")
    elif codon == 'GGG':
        print("Alanina")
    elif codon == 'GGU':
        print("Alanina")
    elif codon == 'GAA':
        print("Ácido Aspártico")
    elif codon == 'GAC':
        print("Ácido Aspártico")
    elif codon == 'GAG':
        print("Ácido Aspártico")
    elif codon == 'GAU':
        print("Ácido Aspártico")
    elif codon == 'GGA':
        print("Glicina")
    elif codon == 'GGC':
        print("Glicina")
    elif codon == 'GGG':
        print("Glicina")
    elif codon == 'GGU':
        print("Glicina")
    else:
        print('El codón que has introducido no existe en el código genético')


genetic_code = {
    '''
    Diccionario que representa el código genético
    '''
    "UUU": "Fenilalanina",
    "UUC": "Fenilalanina",
    "UUA": "Leucina",
    "UUG": "Leucina",
    "UCU": "Serina",
    "UCC": "Serina",
    "UCA": "Serina",
    "UCG": "Serina",
    "UAU": "Tirosina",
    "UAC": "Tirosina",
    "UAA": "Codón de terminacion Ocre",
    "UAG": "Codon de terminacion Ambar",
    "UGU": "Cisteina",
    "UGC": "Cisteina",
    "UGA": "Codon de terminacion Opalo",
    "UGG": "Triptofano",
    "CUU": "Leucina",
    "CUC": "Leucina",
    "CUA": "Leucina",
    "CUG": "Leucina",
    "CCU": "Prolina",
    "CCC": "Prolina",
    "CCA": "Prolina",
    "CCG": "Prolina",
    "CAU": "Histidina",
    "CAC": "Histidina",
    "CAA": "Glutamina",
    "CAG": "Glutamina",
    "CGU": "Arginina",
    "CGC": "Arginina",
    "CGA": "Arginina",
    "CGG": "Arginina",
    "AUU": "Isoleucina",
    "AUC": "Isoleucina",
    "AUA": "Isoleucina",
    "AUG": "Metionina",
    "ACU": "Treonina",
    "ACC": "Treonina",
    "ACA": "Treonina",
    "ACG": "Treonina",
    "AAU": "Asparagina",
    "AAC": "Asparagina",
    "AAA": "Lisina",
    "AAG": "Lisina",
    "AGU": "Serina",
    "AGC": "Serina",
    "AGA": "Arginina",
    "AGG": "Arginina",
    "GUU": "Valina",
    "GUC": "Valina",
    "GUA": "Valina",
    "GUG": "Valina",
    "GCU": "Alanina",
    "GCC": "Alanina",
    "GCA": "Alanina",
    "GCG": "Alanina",
    "GAU": "acido aspartico",
    "GAC": "acido aspartico",
    "GAA": "acido glutamico",
    "GAG": "acido glutamico",
    "GGU": "Glicina",
    "GGC": "Glicina",
    "GGA": "Glicina",
    "GGG": "Glicina"}


def traductor_codon(codon):
    ''' str -> str
    Traduce el codon a aminoácido
        Entrada: string que representa el codon
        Salida: string que representa el aminoácido
    '''
    if codon in genetic_code:
        return (genetic_code[codon])
    else:
        print("No se encuentra")


import re


def ejercicio9(codon):
    ''' str -> str
    Traduce el codon a aminoácido
        Entrada: string que representa el codon
        Salida: string que representa el aminoácido
    '''
    if re.match('UU[UC]', codon):
        print("Fenilalanina")
    elif re.match('UU[AG]', codon):
        print("Leucina")
    elif re.match('UC[ACGU]', codon):
        print("Serina")
    elif re.match('UA[UC]', codon):
        print("Tirosina")
    elif re.match('UA[AG]', codon):
        print("STOP")
    elif re.match('UG[UC]', codon):
        print("Cisteína")
    elif re.match('UGA', codon):
        print("STOP")
    elif re.match('UGG', codon):
        print("Triptófano")
    elif re.match('CU[ACGU]', codon):
        print("Leucina")
    elif re.match('CC[ACGU]', codon):
        print("Prolina")
    elif re.match('CA[CU]', codon):
        print("Histidina")
    elif re.match('CA[AG]', codon):
        print("Glutamina")
    elif re.match('AU[ACU]', codon):
        print("Isoleucina")
    elif re.match('AUG', codon):
        print("Metionina")
    elif re.match('AC[ACGU]', codon):
        print("Treonina")
    elif re.match('AA[UC]', codon):
        print("Aparagina")
    elif re.match('AA[AG]', codon):
        print("Lisina")
    elif re.match('AG[UC]', codon):
        print("Serina")
    elif re.match('AG[AG]', codon):
        print("Arginina")
    elif re.match('GU[ACGU]', codon):
        print("Valina")
    elif re.match('GC[ACGU]', codon):
        print("Alanina")
    elif re.match('GA[ACGU]', codon):
        print("Ácido Aspártico")
    elif re.match('GG[ACGU]', codon):
        print("Glicina")
    else:
        print('El codón que has introducido no existe en el código genético')


def DistanciaHamming(p, q):
    '''(str, str) -> int
    Calcula distancia hamming entre dos cadenas de ADN e indica en qué posiciones no hya coincidencia
        input: dos strings que representan dos cadenas de ADN
        output: int que representa índice de distancia hamming
    '''
    result = 0
    if len(p) != len(q):
        print("Chains are \not equals")
    else:
        for x, (i, j) in enumerate(zip(p, q), 1):
            if i != j:
                print(f'Unmatching bases {i, j} in position {x}')
                result += 1
        return result


def Vecinas1(patron):
    ''' str -> list(str, str...)
    Encontrar las cadenas del mismo tamaño que patron con una distancia de
    Hamming menor o igual que 1.
        Entrada: una cadena patron de tamaño n.
        Salida: un conjunto (o lista) con las cadenas de tamaño n cuya distancia de
        Hamming respecto a patron sea menor o igual que 1
    '''
    vecinas = {patron}
    bases = ['A', 'T', 'G', 'C']
    for i in range(len(patron)):
        sim = patron[i]
        for k in bases:
            if k != sim:
                vecina = patron[:i]+k+patron[i+1:]
                vecinas.add(vecina)
    return vecinas


def Vecinas(patron, d):
    ''' (str, int) -> list(str, str...)
    Encontrar las cadenas del mismo tamaño que patron con una distancia de
    Hamming menor o igual que d.
        input: string que representa una cadena de ADN
        output: lista de cadenas de ADN
    '''
    vecinas = {patron}
    bases=["A","C","G","T"]
    for i in range(d):
        for vecina in vecinas:
            vecinas = Vecinas1(vecina).union(vecinas)
    print(sorted(vecinas))


def contar(texto, patron):
    ''' (str, str) -> int
    Encontrar los k-meros más frecuentes en una cadena.
        Entrada: una cadena texto y un entero k.
        Salida: una lista con los k-meros más frecuentes en texto
    '''
    cont=0
    for i in range(0, len(texto) - len(patron) + 1):
        if texto[i:i+len(patron)]==patron:
           cont+=1
    return(cont)


def PalabrasFrecuentes(texto1, k):
    ''' (str, int) -> list(str, str...)
    Encontrar todas las ocurrencias de un patrón en un texto. Nótese que el
    patrón puede solaparse.
        Entrada: cadenas patrón y texto.
        Salida: lista con todas las posiciones iniciales de patrón en texto. Nótese que las
        cadenas se indexan desde 0.
    '''
    kmers = []
    tabla_hash = {}
    max_apariciones = 0
    for i in range(0, len(texto1) - k + 1):
        motif = texto1[i:i+k]
        pos = texto1.find(motif)
        if pos >= 0:
            tabla_hash[motif] = 1
            pos = texto1.find(motif, pos+len(motif))
            while pos >= 0:
                tabla_hash[motif] += 1
                pos = texto1.find(motif, pos+len(motif))
    max_apariciones = max(tabla_hash.values())
    kmers = [clave for clave, valor in tabla_hash.items() if valor == max_apariciones]
    return kmers


def BusquedaPatron(texto, patron):
    ''' (str, str) -> list(int, int...)
    Encontrar todas las ocurrencias de un patrón en un texto. Nótese que el
    patrón puede solaparse.
        Entrada: cadenas patrón y texto.
        Salida: lista con todas las posiciones iniciales de patrón en texto. Nótese que las
        cadenas se indexan desde 0.
    '''
    match_pos = []
    for i in range(0, len(texto) - len(patron) + 1):
        if texto[i:i+len(patron)] == patron:
            match_pos.append(i)
    return match_pos


def BusquedaAproximadaPatron(patron, texto, d):
    '''(str, str, int) -> list(int, int...)
    Encontrar las ocurrencias aproximadas de un patrón en un texto.
         Entrada: cadenas patrón, texto y entero d que representa el número
         máximo de discrepancias.
         Salida: lista con todas las posiciones iniciales de patrón en texto con d
         discrepancias como máximo
    '''
    motifs = []
    match_pos = []
    for i in range(0, len(texto) - len(patron) + 1):
        motif = texto[i:i+len(patron)]
        hamming = 0
        for x, (j, k) in enumerate(zip(patron, motif), 1):
            if j != k:
                hamming += 1
        if hamming <= d:
            motifs.append(motif)
            match_pos.append(i)
    return match_pos


def PalabrasFrecuentesDiscrepancias(texto, k, d):
    '''(str, int, int) -> list(str, str...)
    Encontrar las palabras frecuentes en un texto con hasta un número máximo
    de discrepancias.
        Entrada: una cadena texto, un entero k con la longitud de la palabra y un
        entero d con el número máximo de discrepancias.
        Salida: una lista con los k-meros más frecuentes en texto con hasta d
        discrepancias.
    '''
    kmers_appearences = {}
    kmers = []
    max_apariciones = 0
    for i in range(0, len(texto) - k + 1):
        motif = texto[i:i+k]
        kmers_appearences[motif] = 1
        for j in range(0, len(texto) - k + 1):
            hamming = 0
            candidato = texto[j:j+k]
            for x, (l, m) in enumerate(zip(candidato, motif), 1):
                if l != m:
                    hamming += 1
            if hamming <= d:
                kmers_appearences[motif] += 1
    max_apariciones = max(kmers_appearences.values())
    kmers = [clave for clave, valor in kmers_appearences.items() if valor == max_apariciones]
    return kmers


def main():
    print('Boletín Sis.Bio')
    if __name__ == "__main__":
        main()
