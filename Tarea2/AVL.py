EddActual = AVL()
print ("Selecciona una opción")
print ("\t1 - Insertar:")
print ("\t2 - Buscar:")
print ("\t3 - Eliminar")
b = input()
if b==1:
    print ('Ingrese nombre, género, puntuacion:')
    n=input()
    g=input()
    pun=input()
    EddActual.insert(pun,n,genero)
elif b==2:
    print ('Ingrese el nombre:')
    n=input()
    EddActual.search(n)
elif b==3:
    print ('Ingrese nombre de Anime a eliminar:')
    n=input()
    delete(n)

class Anime:
    def __init__(self,puntuacion,nombre,genero,izquierdo,derecho,padre):
        self.puntuacion = puntuacion
        self.cargaUtil = valor
        self.nombre = nombre
        self.genero = genero
        self.padre = None
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.height = 0


    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo

    def reemplazarDatoDeNodo(self,puntuacion,nombre,genero,hizq,hder):
        self.puntuacion = puntuacion
        self.hijoIzquierdo = hizq
        self.hijoDerecho = hder
        self.nombre = nombre
        self.genero = genero
        if self.tieneHijoIzquierdo():
            self.hijoIzquierdo.padre = self
        if self.tieneHijoDerecho():
            self.hijoDerecho.padre = self
   
 
    def right(self):
        return self.hijoDerecho

  
    def right(self, Anime):
        if Anime is not None:
            Anime.padre = self
            self.hijoDerecho = Anime

  
    def left(self):
        return self.hijoIzquierdo

    
    def left(self, Anime):
        if Anime is not None:
            Anime.padre = self
            self.hijoIzquierdo = Anime

   
    def padre(self):
        return self.padre

    
    def padre(self, Anime):
        if Anime is not None:
            self.padre = Anime
            self.height = self.padre.height + 1
        else:
            self.height = 0

class AVL:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

        """
        Operación de inserción para agregar nuevos nodos
        al árbol.
        """
    def insert(self, puntuacion,nombre,genero):
        Anime = Anime(puntuacion,nombre genero)

        if self.raiz is None:
            self.raiz = Anime
            self.raiz.height = 0
            self.tamano = 1
        else:
            Anime.padre = None
            Anime = self.raiz

            while True:
                if Anime is not None:

                    Anime.padre = Anime

                    if Anime.puntuacion < Anime.puntuacion:
                        Anime = Anime.left
                    else:
                        Anime = Anime.right
                else:
                    Anime.height = Anime.padre.height
                    Anime.padre.height += 1
                    if Anime.puntuacion < Anime.padre.puntuacion:
                        Anime.padre.left = Anime
                    else:
                        Anime.padre.right = Anime
                    self.rebalance(Anime)
                    self.tamano += 1
                    break

        # Operación de rotación
    def rebalance(self, Anime):
        n = Anime

        while n is not None:
            heighthijoDerecho = n.height
            heighthijoIzquierdo = n.height

            if n.right is not None:
                heighthijoDerecho = n.right.height

            if n.left is not None:
                heighthijoIzquierdo = n.left.height

            if abs(heighthijoIzquierdo - heighthijoDerecho) > 1:
                if heighthijoIzquierdo > heighthijoDerecho:
                    left_child = n.left
                    if left_child is not None:
                        hhijoDerecho = (left_child.right.height
                                    if (left_child.right is not None) else 0)
                        hhijoIzquierdo = (left_child.left.height
                                    if (left_child.left is not None) else 0)
                    if (hhijoIzquierdo > hhijoDerecho):
                        self.rotatehijoIzquierdo(n)
                        break
                    else:
                        self.double_rotatehijoDerecho(n)
                        break
                else:
                    right_child = n.right
                    if right_child is not None:
                        hhijoDerecho = (right_child.right.height
                            if (right_child.right is not None) else 0)
                        hhijoIzquierdo = (right_child.left.height
                            if (right_child.left is not None) else 0)
                    if (hhijoIzquierdo > hhijoDerecho):
                        self.double_rotatehijoIzquierdo(n)
                        break
                    else:
                        self.rotatehijoDerecho(n)
                        break
            n = n.padre

    def rotatehijoIzquierdo(self, Anime):
        aux = Anime.padre
        Anime.padre = Anime
        Anime.padre.right = Anime
        Anime.padre.right.height = Anime.padre.height + 1
        Anime.padre.left = Anime.right


    def rotatehijoDerecho(self, Anime):
        aux = Anime.padre
        Anime.padre = Anime
        Anime.padre.left = Anime
        Anime.padre.left.height = Anime.padre.height + 1
        Anime.padre.right = Anime.right

    def double_rotatehijoIzquierdo(self, Anime):
        self.rotatehijoDerecho(Anime.getRight().getRight())
        self.rotatehijoIzquierdo(Anime)

    def double_rotatehijoDerecho(self, Anime):
        self.rotatehijoIzquierdo(Anime.getLeft().getLeft())
        self.rotatehijoDerecho(Anime)

    def search(self,puntuacion):
       if self.raiz:
           res = self._search(puntuacion,self.raiz)
           if res:
                  return res.nombre
           else:
                  return None
       else:
           return None

    def _seacrh(self,nombre,nodoActual):
       if not nodoActual:
           return None
       elif nodoActual.nombre == nombre:
           return nodoActual
       elif nombre < nodoActual.nombre:
           return self._search(nombre,nodoActual.hijoIzquierdo)
       else:
           return self._search(nombre,nodoActual.hijoDerecho)


    def empty(self):
        if self.raiz is None:
            return True
        return False

    def preShow(self, Anime):
        if Anime is not None:
            self.preShow(Anime.left)
            print(Anime.puntuacion, end=" ")
            self.preShow(Anime.right)

    def preorder(self, Anime):
        if Anime is not None:
            self.preShow(Anime.left)
            self.preShow(Anime.right)
            print(Anime.puntuacion, end=" ")

    def getraiz(self):
        return self.raiz
