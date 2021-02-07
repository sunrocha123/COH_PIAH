import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    Tot_valores = 0
    for j in range(len(as_a)):
        calculo = abs(as_a[j] - as_b[j])
        Tot_valores += calculo
    return Tot_valores/6

    pass

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    lista_calcula = []
    Tot_unicas = 0
    Tot_diferentes = 0
    Tot_palavras = 0
    Tot_frases = 0
    Tot_sentencas = 0
    Tot_tamanho_palavras = 0
    palavras = []

    sentencas = separa_sentencas(texto)
    Tot_sentencas += len(sentencas)
    for i in range(len(sentencas)):
        frases = separa_frases(sentencas[i])
        Tot_frases += len(frases)
        for k in range(len(frases)):
            palavras += separa_palavras(frases[k])
    Tot_unicas += n_palavras_unicas(palavras)
    Tot_diferentes += n_palavras_diferentes(palavras)
    Tot_palavras += len(palavras)
    for t in range(len(palavras)):
        Tot_tamanho_palavras += len(palavras[t])

    lista_calcula.append(Tot_tamanho_palavras/Tot_palavras)
    lista_calcula.append(Tot_diferentes/Tot_palavras)
    lista_calcula.append(Tot_unicas/Tot_palavras)
    lista_calcula.append(Tot_palavras/Tot_sentencas)
    lista_calcula.append(Tot_frases/Tot_sentencas)
    lista_calcula.append(Tot_palavras/Tot_frases)

    return lista_calcula

    pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_assinaturas = []

    for i in range(len(textos)):
        dados_texto = (calcula_assinatura(textos[i]))
        lista_assinaturas.append(compara_assinatura(dados_texto, ass_cp))

    valor_cp = lista_assinaturas[0]
    texto_cp = 0
    for a in range(len(lista_assinaturas)):
        if lista_assinaturas[a] < valor_cp:
            texto_cp = lista_assinaturas.index(lista_assinaturas[a])
            pass
    
    return texto_cp
    pass

def executa():

    assinatura = le_assinatura()
    textos = le_textos()
    print("O autor do texto", avalia_textos(textos, assinatura), "está infectado com COH-PIAH")

executa()
    