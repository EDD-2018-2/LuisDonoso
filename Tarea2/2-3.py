if EddActual is None
    EddActual = BTree()
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
    EddActual.add(pun,n,genero)
elif b==2:
    print ('Ingrese el nombre:')
    n=input()
    EddActual.find(n)
elif b==3:
    print ('Ingrese nombre de Anime a eliminar:')
    n=input()
    delete(n)

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
        
