class No(object):
    def __init__(self,ponteiro,valor,esquerda=None,direita=None):
        self.ponteiro = ponteiro
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
    

class Arvore(object):
    def __init__(self,valor):
        self.maior_indice = 0
        no_raiz = No(0,valor)
        self.no_raiz = no_raiz
        

    def insere_no(self, no_raiz, valor):
        if(valor > no_raiz.valor):
            if(no_raiz.direita == None):
                no_raiz.direita = No(self.maior_indice+1, valor)
                self.maior_indice = self.maior_indice + 1
            else:
                self.insere_no(no_raiz.direita, valor)
        else:
            if(no_raiz.esquerda == None):
                no_raiz.esquerda = No(self.maior_indice+1, valor)
                self.maior_indice = self.maior_indice + 1
            else:
                self.insere_no(no_raiz.esquerda, valor)     
            

    def imprime_arvore(self):
        print(self.no_raiz.valor)
        lista_impressao = []
        lista_impressao.append(self.no_raiz)
        total = 7
        self.imprime_no(lista_impressao,0,total)
    
    def imprime_no(self,lista_impressao,cursor,total):

        # parou aqui
        appends = 0
        if(lista_impressao[cursor].esquerda != None):
            lista_impressao.append(lista_impressao[cursor].esquerda)
            print(lista_impressao[cursor].esquerda.valor)
            appends = appends + 1
           
        else:
            print("N")
        
        if(lista_impressao[cursor].direita != None):
            lista_impressao.append(lista_impressao[cursor].direita)
            print(lista_impressao[cursor].direita.valor)
            appends = appends + 1
           
        else:
            print("N")
        
        self.imprime_no(lista_impressao, cursor + appends,total)

        
    
    # def imprime_no(self, no):
    #     if(no.esquerda != None):
    #         print(no.esquerda.valor)
    #     else:
    #         print("N")

    #     if(no.direita != None):
    #         print(no.direita.valor)
    #     else:
    #         print("N")
            
    #     if(no.esquerda != None):
    #         self.imprime_no(no.esquerda)
        
    #     if(no.direita != None):
    #         self.imprime_no(no.direita)


# arvore = Arvore(10)
# arvore.insere_no(arvore.no_raiz,12)
# arvore.insere_no(arvore.no_raiz,134)
# arvore.insere_no(arvore.no_raiz,20)
# arvore.insere_no(arvore.no_raiz,23)
# arvore.insere_no(arvore.no_raiz,8)
# arvore.insere_no(arvore.no_raiz,1)
# arvore.imprime_arvore()


arvore = Arvore(10)
arvore.insere_no(arvore.no_raiz,5)
arvore.insere_no(arvore.no_raiz,20)
arvore.insere_no(arvore.no_raiz,2)
arvore.insere_no(arvore.no_raiz,15)
arvore.insere_no(arvore.no_raiz,21)
arvore.insere_no(arvore.no_raiz,1)
arvore.imprime_arvore()


