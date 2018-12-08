EDDActual = ABB ()
print ("Selecciona una opción")
print ("\t1 - Insertar:")
print ("\t2 - Buscar:")
print ("\t3 - Eliminar")
b = input()
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

    def buscar(self,nombre,puntuacion):
       if self.raiz:
           res = self._buscar(nombre,puntuacion,self.raiz)
           if res:
                  return res.nombre
           else:
                  return None
       else:
           return None

    def _buscar(self,nombre,puntuacion,nodoActual):
       if not nodoActual:
           return None
       elif nodoActual.nombre == nombre:
           return nodoActual
       elif puntuacion < nodoActual.puntuacion:
           return self._buscar(nombre,puntuacion,nodoActual.hijoIzquierdo)
       else:
           return self._buscar(nombre,puntuacion,nodoActual.hijoDerecho)

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
