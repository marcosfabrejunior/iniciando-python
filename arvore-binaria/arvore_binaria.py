# NO
class No(object):
    def __init__(self,ponteiro,valor,esquerda=None,direita=None):
        self.ponteiro = ponteiro
        self.valor = valor
        self.esquerda = esquerda
        self.direita = direita
    
# ARVORE
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
            
    # IMPRIMIR ARVORE
    def imprime_arvore(self):
        print(self.no_raiz.valor)
        lista_impressao = []
        lista_impressao.append(self.no_raiz)
        total = 7
        self.imprime_no(lista_impressao,0,total)
    
    # IMPRIMIR NO
    def imprime_no(self,lista_impressao,cursor,total):
        if(len(lista_impressao) == cursor):
            return   

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
        
        self.imprime_no(lista_impressao, cursor + 1,total)

    # BUSCA VALOR EM UMA ARVORE
    def busca(self, valor,no_raiz=None, no_pai=None):
        
        if(no_raiz == None):
            no_raiz = self.no_raiz      

        if(no_raiz.valor == valor):
            print("Achei")
            return no_raiz
        elif(valor < no_raiz.valor and no_raiz.esquerda != None):
            self.busca(valor,no_raiz.esquerda,no_pai)
        elif(valor > no_raiz.valor and no_raiz.direita != None):
            self.busca(valor, no_raiz.direita, no_pai)
        else:
            print("Não foi possível achar o valor na árvore")
            return None

    def atribui_no(self,no_pai,no, valor):
        if(no_pai.esquerda.valor == no_remove.valor):
            no_pai.esquerda = no
        elif no_pai.direita.valor == no_remove.valor:
            no_pai.direita = no


    def remove(self, valor,no_raiz=None, no_pai=None):
        if(no_raiz == None):
            no_raiz = self.no_raiz
        
        no_remove = self.busca(valor)

        # se é uma folha
        if(no_remove.esquerda == None and no_remove.direita == None):
            self.atribui_no(no_pai, None, valor)
            
        # se tem um filho apenas, e na direita
        elif(no_remove.esquerda == None and no_remove.direita != None):
            self.atribui_no(no_pai, no_remove.direita, valor)

         # se tem um filho apenas, e na esquerda
        elif(no_remove.direita == None and no_remove.esquerda != None):
            self.atribui_no(no_pai, no_remove.esquerda, valor)
            


    def remove_no(self, no, no_pai):
        if(no_pai.esquerda.valor == no.valor):
            no_pai.esquerda = None
        elif no_pai.direita.valor == no.valor:
            no_pai.direita = None
        else:
            print("erro")
    


        





arvore = Arvore(10)
arvore.insere_no(arvore.no_raiz,12)
arvore.insere_no(arvore.no_raiz,134)
arvore.insere_no(arvore.no_raiz,20)
arvore.insere_no(arvore.no_raiz,23)
arvore.insere_no(arvore.no_raiz,8)
arvore.insere_no(arvore.no_raiz,1)
arvore.imprime_arvore()
print("")
arvore.busca(134)
print("")
arvore.imprime_arvore()

# arvore = Arvore(10)
# arvore.insere_no(arvore.no_raiz,5)
# arvore.insere_no(arvore.no_raiz,20)
# arvore.insere_no(arvore.no_raiz,2)
# arvore.insere_no(arvore.no_raiz,15)
# arvore.insere_no(arvore.no_raiz,21)
# arvore.insere_no(arvore.no_raiz,1)
# arvore.imprime_arvore()


