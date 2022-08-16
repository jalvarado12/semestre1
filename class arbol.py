class Tree():
    def __init__(self, a, b):
        self.left=a
        self.right=b
        
    def numHojas(self):
        if self.left()==None:
            return 1
        else:
            return self.numHojas(self.left) + self.numHojas(self.right)
        
    def numAristas(self):
        if self==Hoja:
            return 0
        else:
            return 2+ self.right.numAristas()+self.left.numAristas() 
    
    def altura(self):
        if self==Hoja:
            return 0
        else:
           return  1 + max(self.right.altura(), self.left.altura())
      
    def numNodos(self):
        if self==Hoja:
            return 1
        else:
            return 1+ self.right.numNodos() + self.left.numNodos()
        
    def corta(self):
        if self==Hoja:
            return 0
        else:
           return  1 + min(self.right.corta(), self.left.corta())
        
Hoja=Tree(None, None)
Rama=Tree(Hoja, Hoja)
A1=Tree(Rama, Rama)
A2=Tree(Hoja, Rama)
A1=Tree(Rama, Rama)
A3=Tree(Rama, Rama)
print(A2.corta())
