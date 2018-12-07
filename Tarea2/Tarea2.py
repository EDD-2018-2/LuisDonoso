from jikanpy import Jikan
jikan = Jikan()

def main():
    if EddActual is None
        print ('Elija la Estructura de Datos que desea ocupar')
        print ('2. Arbol binario')
        print ('3. AVL')
        print ('4. Arbol 2-3')

        a = imput ()
        
        if a==1:
            EddActual = ArbolBinarioBusqueda()
        elif a==2:
            EddActual = AVL()
        elif a==3:
            EddActual = BTree()
     else:
        print ("Selecciona una opción")
        print ("\t1 - Insertar:")
        print ("\t2 - Buscar:")
        print ("\t3 - Eliminar")
        b = input()
        if a == 1:
            if b == 1:
                print ('Ingrese nombre, género, puntuacion:')
                n=input()
                g=input()
                pun=input()
                EddActual.agregar(pun,n,genero)
            elif b == 2:
                print ('Ingrese el nombre:')
                n=input()
                EddActual.buscar(n)
            elif b == 3:
                print ('Ingrese nombre de Anime a eliminar:')
                n=input()
                EddActual.eliminar(n)
        if a == 2:
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
        if a == 3:
            if b==1:
                print ('Ingrese nombre, género, puntuacion:')
                n=input()
                g=input()
                pun=input()
                EddActual.add(pun,n,genero)
            elif b==2:
                print ('Ingrese el nombre:')
                n=input()
                EddActual.find(n)
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

class ArbolBinarioBusqueda:

    def __init__(self):
        self.raiz = None
        self.tamano = 0

    def longitud(self):
        return self.tamano

    def __len__(self):
        return self.tamano

    def agregar(self,puntuacion,nombre,genero):
        if self.raiz:
            self._agregar(puntuacion,nombre,genero,self.raiz)
        else:
            self.raiz = Anime(puntuacion,nombre)
        self.tamano = self.tamano + 1

    def _agregar(self,puntuacion,nombre,genero,nodoActual):
        if puntuacion < nodoActual.puntuacion:
            if nodoActual.tieneHijoIzquierdo():
                   self._agregar(puntuacion,nombre,genero,nodoActual.hijoIzquierdo)
            else:
                   nodoActual.hijoIzquierdo = Anime(puntuacion,nombre,genero,padre=nodoActual)
        else:
            if nodoActual.tieneHijoDerecho():
                   self._agregar(puntuacion,nombre,genero,nodoActual.hijoDerecho)
            else:
                   nodoActual.hijoDerecho = Anime(puntuacion,nombre,genero,padre=nodoActual)

    def __setitem__(self,c,v,d):
       self.agregar(c,v,d)

    def buscar(self,puntuacion):
       if self.raiz:
           res = self._buscar(puntuacion,self.raiz)
           if res:
                  return res.cargaUtil
           else:
                  return None
       else:
           return None

    def _buscar(self,nombre,nodoActual):
       if not nodoActual:
           return None
       elif nodoActual.nombre == nombre:
           return nodoActual
       elif nombre < nodoActual.nombre:
           return self._buscar(nombre,nodoActual.hijoIzquierdo)
       else:
           return self._buscar(nombre,nodoActual.hijoDerecho)

    def __getitem__(self,nombre):
       return self.buscar(nombre)

    def __contains__(self,nombre):
       if self._buscar(nombre,self.raiz):
           return True
       else:
           return False

    def eliminar(self,nombre):
      if self.tamano > 1:
         nodoAEliminar = self._buscar(nombre,self.raiz)
         if nodoAEliminar:
             self.remover(nodoAEliminar)
             self.tamano = self.tamano-1
         else:
             raise KeyError('Error, la nombre no está en el árbol')
      elif self.tamano == 1 and self.raiz.nombre == nombre:
         self.raiz = None
         self.tamano = self.tamano - 1
      else:
         raise KeyError('Error, la nombre no está en el árbol')

    def __delitem__(self,nombre):
       self.eliminar(nombre)

    def empalmar(self):
       if self.esHoja():
           if self.esHijoIzquierdo():
                  self.padre.hijoIzquierdo = None
           else:
                  self.padre.hijoDerecho = None
       elif self.tieneAlgunHijo():
           if self.tieneHijoIzquierdo():
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoIzquierdo
                  else:
                     self.padre.hijoDerecho = self.hijoIzquierdo
                  self.hijoIzquierdo.padre = self.padre
           else:
                  if self.esHijoIzquierdo():
                     self.padre.hijoIzquierdo = self.hijoDerecho
                  else:
                     self.padre.hijoDerecho = self.hijoDerecho
                  self.hijoDerecho.padre = self.padre

    def encontrarSucesor(self):
      suc = None
      if self.tieneHijoDerecho():
          suc = self.hijoDerecho.encontrarMin()
      else:
          if self.padre:
                 if self.esHijoIzquierdo():
                     suc = self.padre
                 else:
                     self.padre.hijoDerecho = None
                     suc = self.padre.encontrarSucesor()
                     self.padre.hijoDerecho = self
      return suc

    def encontrarMin(self):
      actual = self
      while actual.tieneHijoIzquierdo():
          actual = actual.hijoIzquierdo
      return actual

    def remover(self,nodoActual):
         if nodoActual.esHoja(): #hoja
           if nodoActual == nodoActual.padre.hijoIzquierdo:
               nodoActual.padre.hijoIzquierdo = None
           else:
               nodoActual.padre.hijoDerecho = None
         elif nodoActual.tieneAmbosHijos(): #interior
           suc = nodoActual.encontrarSucesor()
           suc.empalmar()
           nodoActual.puntuacion = suc.puntuacion
           nodoActual.nombre = suc.nombre
           nodoActual.genero = suc.genero

         else: # este nodo tiene un (1) hijo
           if nodoActual.tieneHijoIzquierdo():
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoIzquierdo
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoIzquierdo.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoIzquierdo
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoIzquierdo.puntuacion,
                                    nodoActual.hijoIzquierdo.cargaUtil,
                                    nodoActual.hijoIzquierdo.hijoIzquierdo,
                                    nodoActual.hijoIzquierdo.hijoDerecho)
           else:
             if nodoActual.esHijoIzquierdo():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoIzquierdo = nodoActual.hijoDerecho
             elif nodoActual.esHijoDerecho():
                 nodoActual.hijoDerecho.padre = nodoActual.padre
                 nodoActual.padre.hijoDerecho = nodoActual.hijoDerecho
             else:
                 nodoActual.reemplazarDatoDeNodo(nodoActual.hijoDerecho.puntuacion,
                                    nodoActual.hijoDerecho.cargaUtil,
                                    nodoActual.hijoDerecho.hijoIzquierdo,
                                    nodoActual.hijoDerecho.hijoDerecho)


# Declaramos la clase AVL
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

class BTreeNode(object):
    """A B-Tree Node.
    
    attributes
    =====================
    leaf : boolean, determines whether this node is a leaf.
    puntuacion : list, a list of puntuacion internal to this node
    hijos : list, a list of children of this node
    """
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.anime = []
        
    def __str__(self):
        if self.leaf:
            return "Leaf BTreeNode with {0} puntuacion\n\tK:{1}\n\tC:{2}\n".format(len(self.puntuacion), self.puntuacion, self.hijos)
        else:
            return "Internal BTreeNode with {0} puntuacion, {1} children\n\tK:{2}\n\n".format(len(self.puntuacion), len(self.hijos), self.puntuacion, self.hijos)


class BTree(object):
    def __init__(self, t):
        self.root = BTreeNode(leaf=True)
        self.t    = 2
    
    def find(self, k, x=None):
        """Search the B-Tree for the key k.
        
        args
        =====================
        k : Key to search for
        x : (optional) Node at which to begin search. Can be None, in which case the entire tree is searched.
        
        """
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.anime) and k > x.anime[i].puntuacion:    # look for index of k
                i += 1
            if i < len(x.anime) and k == x.anime[i].puntuacion:       # found exact match
                return (x, i)
            elif x.leaf:                                # no match in anime, and is leaf ==> no match exists
                return None
            else:                                       # search children
                return self.find(k, x.hijos[i])
        else:                                           # no node provided, search root of tree
            return self.find(k, self.root)
        
    def add(self,puntuacion,nombre,genero):
        r = self.root
        if len(r.anime) == (2*self.t) - 1:     # anime are full, so we must split
            s         = BTreeNode()
            self.root = s
            s.hijos.add(0,puntuacion,nombre,genero)                  # former root is now 0th child of new root s
            self._split_child(s, 0)            
            self._add_nonfull(s,puntuacion,nombre,genero)
        else:
            self._add_nonfull(r,puntuacion,nombre,genero)
    
    def _add_nonfull(self,x,puntuacion,nombre,genero):
        i = len(x.anime) - 1
        if x.leaf:
            # insert a key
            x.anime.append(0)
            while i >= 0 and puntuacion < x.anime[i].puntuacion:
                x.anime[i+1] = x.anime[i]
                i -= 1
            x.anime[i+1] = Anime(puntuacion,nombre,genero)
        else:
            # insert a child
            while i >= 0 and puntuacion < x.anime[i].puntuacion:
                i -= 1
            i += 1
            if len(x.hijos) == (2*self.t) - 1:
                self._split_child(x, i)
                if k > x.anime[i]:
                    i += 1
            self._add_nonfull(x.hijos[i],puntuacion,nombre,genero)
        
    def _split_child(self, x, i):
        t = 2
        y = x.hijos[i]
        z = BTreeNode(leaf=y.leaf)
        
        # slide all children of x to the right and insert z at i+1.
        x.hijos.add(i+1, z)
        x.anime.add(i, y.anime[t-1])
        
        # anime of z are t to 2t - 1,
        # y is then 0 to t-2
        z.anime = y.anime[t:(2*t - 1)]
        y.anime = y.anime[0:(t-1)]
        
        # children of z are t to 2t els of y.hijos
        if not y.leaf:
            z.hijos = y.hijos[t:(2*t)]
            y.hijos = y.hijos[0:(t-1)]    
        
    def __str__(self):
        r = self.root
        return r.__str__() + '\n'.join([child.__str__() for child in r.hijos])  
        

if__name__== "__main__"
    EddActual = None
    while True
        main()
