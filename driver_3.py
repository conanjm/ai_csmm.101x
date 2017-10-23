# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 19:37:02 2017

@author: Khaliun
"""
class MoveNotPossible(Exception):

    
    def __str__(self):
        return "ulala"
    
class state(object):
    def __init__(self, l, label=None, parent=None):
        
        if len(l)==3:
            self.data = l
        else:
            z0 = l[:3]
            z1 = l[3:6]
            z2 = l[6:]
            self.data = [z0,z1,z2]           
        self.parent = parent
        self.label = label
    def __str__(self):
        
        return self.data
        
    def set_parent(self, parent):
        
        self.parent= parent
        
    def get_parent(self):
        
        return self.parent
        
    def set_label(self,label):
        
        self.label = label
        
    def get_label(self):
        
        return self.label
        
    def set_data(self, data):
        
        self.data = data
        
    def get_data(self):
        
        return self.data
        
    def move(self, move):
        
        copy = list(self.get_data())                     
        print(copy)
        print(copy is self.data)
        
        for a in range(3):
            for b in range(3):
                if copy[a][b] == 0 :
                    i = a
                    j = b
                    
                
        
        print('data', self.data)
        
        if move == 'u': 
            
            if i == 0:
                raise MoveNotPossible
            else:
                temp = copy[i-1][j]
                copy[i-1][j] = copy[i][j]
                copy[i][j] = temp
                lbl = 'Up'
                return copy, lbl
        if move == 'd':
            if i == 2:
                raise MoveNotPossible
            else:
                temp = copy[i+1][j]
                copy[i+1][j] = copy[i][j]
                copy[i][j] = temp
                lbl = 'Down'
                return copy, lbl
        if move == 'l':
            
            if j == 0:
                raise MoveNotPossible
            else:
                temp = copy[i][j-1]
                copy[i][j-1] = copy[i][j]
                copy[i][j] = temp
                lbl = 'Left'
                return copy, lbl
        if move == 'r':
            
            if j == 2:
                raise MoveNotPossible
            else:
                temp = copy[i][j+1]
                copy[i][j+1] = copy[i][j]
                copy[i][j] = temp
                lbl = 'Right'
                return copy, lbl            
                    
                            
    def is_goal(self, goal=[[0,1,2],[3,4,5],[6,7,8]]):
        if self == goal :
            return True
        else:
            return False
                        
    def generate_children(self):
        
        children = []
        
        for char in 'udlr':
            print(char)
            try :
                data, label = self.move(char)
                print('pp', data, label)
                child_state = state(data,label)
                print('child', child_state is self)
                children.append(child_state)
            except MoveNotPossible:
                pass
                       
        return children
        
def solve_bfs(first_state):
    
    to_visit = []
    visited = []
    current_state = state(first_state)
    to_visit.append(current_state)
    
    while True:
        
        children = current_state.generate_children()
                    
        for i in children:
            if i not in visited:
                to_visit.append(i)
        visited.append(current_state)
        to_visit.remove(current_state)
        current_state = to_visit[0]

        if current_state.is_goal() == True :
            break

    path_reversed = []
    while current_state != None:
        path_reversed.append(current_state)
        current_state = current_state.get_parent()
        
    path = path_reversed.reverse()
    
    return path
    
l = [1,0,2,3,4,5,6,7,8]

print(solve_bfs(l))
        
            
            
        

        
