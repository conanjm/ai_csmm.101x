# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 19:37:02 2017

@author: Khaliun
"""
import numpy
class MoveNotPossible(Exception):

    
    def __str__(self):
        return "ulala"
    
class state(object):
    def __init__(self, l, label, parent):
        
        self.data = list(l)
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
        copy =list(self.get_data())                            
        print(copy)
        print(copy is self.data)
        
        for a in range(len(copy)):
            if copy[a] == 0 :
                    i = a
                                 
        
        print('data', self.data)
        
        if move == 'u': 
            
            if i < 3:
                raise MoveNotPossible
            else:
                temp = copy[i-2*3]
                copy[i-2*3] = copy[i]
                copy[i] = temp
            lbl = 'Up'
            return copy, lbl

        if move == 'd':
            if i > 5:
                raise MoveNotPossible
            else:
                temp = copy[i+3]
                copy[i+3] = copy[i]
                copy[i] = temp
            lbl = 'Down'
            return copy, lbl

        if move == 'l':            
            if i in [0,3,6]:
                raise MoveNotPossible
            else:
                temp = copy[i-1]
                copy[i-1] = copy[i]
                copy[i] = temp
            lbl = 'Left'
            return copy, lbl

        if move == 'r':
            
            if i in [2,5,8]:
                raise MoveNotPossible
            else:
                temp = copy[i+1]
                copy[i+1] = copy[i]
                copy[i] = temp
            lbl = 'Right'
            return copy, lbl            
                    
                            
    def is_goal(self, goal=[0,1,2,3,4,5,6,7,8]):
        if self.get_data() == goal :
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
                child_state = state(data,label,parent = self)
                children.append(child_state)
            except MoveNotPossible:
                pass
        print(children, 'children')               
        return children
        
def solve_bfs(first_state):
    
    to_visit = []
    visited = []
    current_state = state(first_state, 'first', 'NoParent' )
    to_visit.append(current_state)
    
    while True:
        
        if current_state.is_goal() == True :

            visited.append(current_state)
            to_visit.remove(current_state)
            break            
        else:
            children = current_state.generate_children()
                    
            for i in children:
                if i.get_data() not in visited:
                    to_visit.append(i)
            visited.append(current_state)
            to_visit.remove(current_state)
            print(i.get_data() in to_visit)
            current_state = to_visit[0]

    path_reversed = []
    while current_state.get_parent() != 'NoParent':
        path_reversed.append(current_state.get_label())
        current_state = current_state.get_parent()
        print(path_reversed, 'path_reversed ')
    print(path_reversed.reverse(), 'path_reversed after')    
    
    
    
    return path_reversed.reverse()
    
l = [1,2,0,3,4,5,6,7,8]

print(solve_bfs(l), 'path')
        
            
            
        

        
