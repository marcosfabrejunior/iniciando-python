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
            retorno = []
            retorno.append(no_raiz)
            retorno.append(no_pai)
            return retorno
        elif(valor < no_raiz.valor and no_raiz.esquerda != None):
            return self.busca(valor,no_raiz.esquerda,no_pai)
        elif(valor > no_raiz.valor and no_raiz.direita != None):
            return self.busca(valor, no_raiz.direita, no_pai)
        else:
            print("Não foi possível achar o valor na árvore")
            return None
    
    #BUSCA O MENOR NO DA SUBARVORE
    def busca_menor(self, no_raiz, no_pai = None):
        if(no_raiz.esquerda != None):
            return no_raiz
        else:
            return self.busca_menor(no_raiz.esquerda, no_raiz)
        
    

    def remove(self, valor):
        no_remove = self.busca(valor)
        
        # verifica se é folha
        if(no_remove[0].direita == None and no_remove[0].esquerda == None):
            #se o valor do filho é maior que o do pai
            if(no_remove[0].valor > no_remove[1].valor):
                no_remove[1].direita = None
            else:
                no_remove[1].esquerda = None
        
        # se tem um filho a direita
        if(no_remove[0].direita != None and no_remove[0].esquerda == None):
            #se o valor do filho é maior que o do pai
            if(no_remove[0].valor > no_remove[1].valor):
                no_remove[1].direita = no_remove[0].direita
            else:
                no_remove[1].esquerda = no_remove[0].direita
        
        # se tem um filho a esquerda
        if(no_remove[0].direita == None and no_remove[0].esquerda != None):
            #se o valor do filho é maior que o do pai
            if(no_remove[0].valor > no_remove[1].valor):
                no_remove[1].direita = no_remove[0].esquerda
            else:
                no_remove[1].esquerda = no_remove[0].esquerda
        

        # se tem dois filhos
        if(no_remove[0].direita != None and no_remove[0].esquerda != None):
            menor = self.busca_menor(no_remove[0].direita, no_remove[0])
            print(menor.valor)

        

        

        





arvore = Arvore(10)
arvore.insere_no(arvore.no_raiz,12)
arvore.insere_no(arvore.no_raiz,134)
arvore.insere_no(arvore.no_raiz,20)
arvore.insere_no(arvore.no_raiz,23)
arvore.insere_no(arvore.no_raiz,8)
arvore.insere_no(arvore.no_raiz,1)
# arvore.imprime_arvore()
print("")
# arvore.busca(134)
arvore.remove(1)
print("")
# arvore.imprime_arvore()

# arvore = Arvore(10)
# arvore.insere_no(arvore.no_raiz,5)
# arvore.insere_no(arvore.no_raiz,20)
# arvore.insere_no(arvore.no_raiz,2)
# arvore.insere_no(arvore.no_raiz,15)
# arvore.insere_no(arvore.no_raiz,21)
# arvore.insere_no(arvore.no_raiz,1)
# arvore.imprime_arvore()


