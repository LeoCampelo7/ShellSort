from random import randint
import timeit
import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
def geralista(tam):
    lista =[]
    lista = random.sample(range(0,tam),tam)
    return lista  

def shell_sort(lista):
    contador = len(lista)//2
    while contador > 0:

      for start in range(contador):
        gapInsertionSort(lista,start,contador)

      contador = contador // 2

def gapInsertionSort(lista,start,gap):
    for i in range(start+gap,len(lista),gap):

        currentvalue = lista[i]
        pos = i

        while pos>=gap and lista[pos-gap]>currentvalue:
            lista[pos]=lista[pos-gap]
            pos = pos-gap

        lista[pos]=currentvalue


def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas", z='Tempo'):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = z)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig('teste.png', format='png')
    plt.show()



if __name__ == '__main__':
    
    z = [30000,40000,50000,60000,70000]
    lista = []
    newlista = []
    x = []
    for i in range(len(z)):
        x.append(geralista(z[i]))
    y = []
    for i in range(len(x)):
        y.append(timeit.timeit("shell_sort({})".format(x[i]), setup="from __main__ import shell_sort", number=1))

    desenhaGrafico(z,y)
