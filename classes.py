# -*- coding:Utf-8 -*

#The MIT License (MIT)

#Copyright (c) 2011 Benjamin Dauphin

#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
#the Software, and to permit persons to whom the Software is furnished to do so,
#subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
#COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
#IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
#CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


#Nombre de Colonnes et de Lignes.
colonnes = 10
lignes = 22

table = (colonnes+3)*[0]
for i in range(colonnes):
    table[i] = lignes*[0] + [99,99,99,99]
table[colonnes] = (lignes+4)*[99]
table[colonnes+1] = (lignes+4)*[99]
table[colonnes+2] = (lignes+4)*[99]

class Piece(object):
    """Définie les fonctions de base des Pièces"""
    # def __init__(self):
        # self.ocp = 'h'
    def deplace(self, direction):
        if direction == 'droite' and not(\
           table[self.x + self.ocp[0][0]+1][self.y + self.ocp[0][1]]//10 or\
           table[self.x + self.ocp[1][0]+1][self.y + self.ocp[1][1]]//10 or\
           table[self.x + self.ocp[2][0]+1][self.y + self.ocp[2][1]]//10 or\
           table[self.x + self.ocp[3][0]+1][self.y + self.ocp[3][1]]//10 ):
            
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.x+=1
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
            
        elif direction == 'gauche' and not(\
             table[self.x + self.ocp[0][0]-1][self.y + self.ocp[0][1]]//10 or\
             table[self.x + self.ocp[1][0]-1][self.y + self.ocp[1][1]]//10 or\
             table[self.x + self.ocp[2][0]-1][self.y + self.ocp[2][1]]//10 or\
             table[self.x + self.ocp[3][0]-1][self.y + self.ocp[3][1]]//10 ):
            
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.x-=1
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
            
        elif direction == 'bas' and not(\
             table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]+1]//10 or\
             table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]+1]//10 or\
             table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]+1]//10 or\
             table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]+1]//10 ):
            
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.y+=1
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
            return True
        elif direction == 'bas':
            return False
            
        elif direction == 'chute':
            while self.deplace('bas'):
                continue
            return False
        
    def remonte(self):
        if not(\
         table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]-1]//10 or\
         table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]-1]//10 or\
         table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]-1]//10 or\
         table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]-1]//10 ):
         
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.y-=1
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
    
    def tourneHoraire(self):
        if self.sens == 'h' and not(\
           table[self.x + self.ocpD[0][0]][self.y + self.ocpD[0][1]]//10 or\
           table[self.x + self.ocpD[1][0]][self.y + self.ocpD[1][1]]//10 or\
           table[self.x + self.ocpD[2][0]][self.y + self.ocpD[2][1]]//10 or\
           table[self.x + self.ocpD[3][0]][self.y + self.ocpD[3][1]]//10 ):
            
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.sens='d'
            self.ocp=self.ocpD
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
        
        elif self.sens == 'd' and not(\
             table[self.x + self.ocpB[0][0]][self.y + self.ocpB[0][1]]//10 or\
             table[self.x + self.ocpB[1][0]][self.y + self.ocpB[1][1]]//10 or\
             table[self.x + self.ocpB[2][0]][self.y + self.ocpB[2][1]]//10 or\
             table[self.x + self.ocpB[3][0]][self.y + self.ocpB[3][1]]//10 ):
            
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.sens='b'
            self.ocp=self.ocpB
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
        
        elif self.sens == 'b' and not(\
             table[self.x + self.ocpG[0][0]][self.y + self.ocpG[0][1]]//10 or\
             table[self.x + self.ocpG[1][0]][self.y + self.ocpG[1][1]]//10 or\
             table[self.x + self.ocpG[2][0]][self.y + self.ocpG[2][1]]//10 or\
             table[self.x + self.ocpG[3][0]][self.y + self.ocpG[3][1]]//10 ):
            
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.sens='g'
            self.ocp=self.ocpG
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
        
        elif self.sens == 'g' and not(\
             table[self.x + self.ocpH[0][0]][self.y + self.ocpH[0][1]]//10 or\
             table[self.x + self.ocpH[1][0]][self.y + self.ocpH[1][1]]//10 or\
             table[self.x + self.ocpH[2][0]][self.y + self.ocpH[2][1]]//10 or\
             table[self.x + self.ocpH[3][0]][self.y + self.ocpH[3][1]]//10 ):
            
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.sens='h'
            self.ocp=self.ocpH
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
        
    def tourneAntiHoraire(self):
        if self.sens == 'b' and not(\
           table[self.x + self.ocpD[0][0]][self.y + self.ocpD[0][1]]//10 or\
           table[self.x + self.ocpD[1][0]][self.y + self.ocpD[1][1]]//10 or\
           table[self.x + self.ocpD[2][0]][self.y + self.ocpD[2][1]]//10 or\
           table[self.x + self.ocpD[3][0]][self.y + self.ocpD[3][1]]//10 ):
            
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.sens='d'
            self.ocp=self.ocpD
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
        
        elif self.sens == 'g' and not(\
             table[self.x + self.ocpB[0][0]][self.y + self.ocpB[0][1]]//10 or\
             table[self.x + self.ocpB[1][0]][self.y + self.ocpB[1][1]]//10 or\
             table[self.x + self.ocpB[2][0]][self.y + self.ocpB[2][1]]//10 or\
             table[self.x + self.ocpB[3][0]][self.y + self.ocpB[3][1]]//10 ):
            
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.sens='b'
            self.ocp=self.ocpB
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
        
        elif self.sens == 'h' and not(\
             table[self.x + self.ocpG[0][0]][self.y + self.ocpG[0][1]]//10 or\
             table[self.x + self.ocpG[1][0]][self.y + self.ocpG[1][1]]//10 or\
             table[self.x + self.ocpG[2][0]][self.y + self.ocpG[2][1]]//10 or\
             table[self.x + self.ocpG[3][0]][self.y + self.ocpG[3][1]]//10 ):
            
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.sens='g'
            self.ocp=self.ocpG
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
        
        elif self.sens == 'd' and not(\
             table[self.x + self.ocpH[0][0]][self.y + self.ocpH[0][1]]//10 or\
             table[self.x + self.ocpH[1][0]][self.y + self.ocpH[1][1]]//10 or\
             table[self.x + self.ocpH[2][0]][self.y + self.ocpH[2][1]]//10 or\
             table[self.x + self.ocpH[3][0]][self.y + self.ocpH[3][1]]//10 ):
            
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = 0
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = 0
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = 0
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = 0
            self.sens='h'
            self.ocp=self.ocpH
            table[self.x + self.ocp[0][0]][self.y + self.ocp[0][1]] = self.num
            table[self.x + self.ocp[1][0]][self.y + self.ocp[1][1]] = self.num
            table[self.x + self.ocp[2][0]][self.y + self.ocp[2][1]] = self.num
            table[self.x + self.ocp[3][0]][self.y + self.ocp[3][1]] = self.num
    

class I(Piece):
    """Définie la barre"""
    def __init__(self):
        self.ocpH = ((0,0),(0,1),(0,2),(0,3))
        self.ocpD = ((0,0),(1,0),(2,0),(3,0))
        self.ocpB = self.ocpH
        self.ocpG = self.ocpD
        self.x = 3
        self.y = 0
        self.num = 1
        self.sens = 'd'
        self.ocp = self.ocpD
        #Piece.__init__(self)

class O(Piece):
    """Définie le bloc"""
    def __init__(self):
        self.ocpH = ((0,0),(0,1),(1,0),(1,1))
        self.ocpD = self.ocpH
        self.ocpB = self.ocpH
        self.ocpG = self.ocpH
        self.x = 4
        self.y = 0
        self.num = 2
        self.sens = 'd'
        self.ocp = self.ocpD
        #Piece.__init__(self)

class T(Piece):
    """Définie le T"""
    def __init__(self):
        self.ocpH = ((0,0),(1,0),(2,0),(1,1))
        self.ocpD = ((0,1),(1,0),(1,1),(1,2))
        self.ocpB = ((1,0),(0,1),(1,1),(2,1))
        self.ocpG = ((0,0),(0,1),(0,2),(1,1))
        self.x = 3
        self.y = 0
        self.num = 3
        self.sens = 'h'
        self.ocp = self.ocpH
        #Piece.__init__(self)

class L(Piece):
    """Définie le L"""
    def __init__(self):
        self.ocpH = ((0,0),(1,0),(2,0),(0,1))
        self.ocpD = ((0,0),(1,0),(1,1),(1,2))
        self.ocpB = ((2,0),(0,1),(1,1),(2,1))
        self.ocpG = ((0,0),(0,1),(0,2),(1,2))
        self.x = 3
        self.y = 0
        self.num = 4
        self.sens = 'h'
        self.ocp = self.ocpH
        #Piece.__init__(self)

class J(Piece):
    """Définie le L inversé"""
    def __init__(self):
        self.ocpH = ((0,0),(0,1),(0,2),(1,0))
        self.ocpD = ((0,0),(1,0),(2,0),(2,1))
        self.ocpB = ((1,0),(1,1),(1,2),(0,2))
        self.ocpG = ((0,0),(0,1),(1,1),(2,1))
        self.x = 3
        self.y = 0
        self.num = 5
        self.sens = 'd'
        self.ocp = self.ocpD
        #Piece.__init__(self)

class Z(Piece):
    """Définie le biais"""
    def __init__(self):
        self.ocpH = ((0,0),(1,0),(1,1),(2,1))
        self.ocpD = ((1,0),(1,1),(0,1),(0,2))
        self.ocpB = self.ocpH
        self.ocpG = self.ocpD
        self.x = 3
        self.y = 0
        self.num = 6
        self.sens = 'h'
        self.ocp = self.ocpH
        #Piece.__init__(self)

class S(Piece):
    """Définie le biais inversé"""
    def __init__(self):
        self.ocpH = ((0,1),(1,1),(1,0),(2,0))
        self.ocpD = ((0,0),(0,1),(1,1),(1,2))
        self.ocpB = self.ocpH
        self.ocpG = self.ocpD
        self.x = 3
        self.y = 0
        self.num = 7
        self.sens = 'h'
        self.ocp = self.ocpH
        #Piece.__init__(self)
