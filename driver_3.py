# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 19:37:02 2017

@author: Khaliun
"""
import numpy
import sys
import time
import os
import psutil

class MoveNotPossible(Exception):

    
    def __str__(self):
        return "ulala"
    
class state(object):
    def __init__(self,depth, l, label, parent = 'NoParent'):
        
        self.data = list(l)
        self.parent = parent
        self.label = label
        self.depth = depth
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
        #print(copy)
        #print(copy is self.data)
        
        for a in range(len(copy)):
            if copy[a] == 0 :
                    i = a
                                 
        
        #print('data', self.data)
        
        if move == 'u': 
            
            if i < 3:
                raise MoveNotPossible
            else:
                temp = copy[i-3]
                copy[i-3] = copy[i]
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
            #print(char)
            try :
                data, label = self.move(char)
                #print('pp', data, label)
                child_state = state((self.depth+1),data,label,parent = self)
                children.append(child_state)
            except MoveNotPossible:
                pass
        #print(children, 'children')               
        return children

class solver(object):
    def __init__(self, start_list, method):
        
        self.start = state(0,start_list, 'first')
        self.method = method
        self.visited =  set()
        self.all_state_set = set()
        self.to_visit = []
        self.max_search_depth = 0
        self.running_time = 0   #the total running time of the search instance, reported in seconds
        self.max_ram_usage = 0

           
    def solve_bfs(self):

        """ Breadth First Search """
        current_state = self.start
        self.all_state_set.add(str(current_state.data))       
        while True:
            self.visited.add(str(current_state.data))
            if current_state.is_goal() == True :  
                break            
            else:
                
                children = current_state.generate_children()
                     
                for i in children:                    
                    if str(i.data) not in self.all_state_set:
                        self.to_visit.append(i)
                        self.all_state_set.add(str(i.data))
                        self.max_search_depth = max(self.max_search_depth, i.depth)

                        
                    
                current_state = self.to_visit.pop(0)
        return current_state
        
    def solve_dfs(self):
        """Depth First Search"""
        current_state = self.start
        self.all_state_set.add(str(current_state.data))
        while True:
            #if not len(self.visited)%1000:
                #print (len(self.visited))
            self.visited.add(str(current_state.data))
                        
            if current_state.is_goal() == True :  
                

                break            
            else:
                children = current_state.generate_children()
                children.reverse()
                 
                for i in children:
                    
                    if str(i.data) not in self.all_state_set:
                        self.to_visit.append(i)
                        self.all_state_set.add(str(i.data))
                        self.max_search_depth = max(self.max_search_depth, i.depth)
                                        
                current_state = self.to_visit.pop()
        return current_state
        
    def find_path(self, c_state):
        """ finds the path from the start state to the given state."""
        path = []
        while c_state.get_parent() != 'NoParent':
            path.append(c_state.get_label())
            c_state = c_state.get_parent()
                
        path.reverse()   
        return path

    def solve(self):
        s = time.time()
        if self.method == 'bfs':
            state = self.solve_bfs()

        if self.method == 'dfs':
            state = self.solve_dfs()

        path = self.find_path(state)
        self.running_time = time.time() - s
        self.max_ram_usage = psutil.Process(os.getpid()).memory_info().rss/(1024*1024)

        f = open("output.txt","w")
        f.write("path_to_goal: " + str(path) + "\n")
        f.write("cost_of_path: " + str(len(path)) + "\n")
        f.write("nodes_expanded: " + str(len(self.visited)-1) + "\n")
        f.write("search_depth: " + str(state.depth) + "\n") # again
        f.write("max_search_depth: " + str(self.max_search_depth) + "\n")
        f.write("running_time: "+ "%.8f" %self.running_time + "\n") 
        f.write("max_ram_usage: " + "%.8f" %self.max_ram_usage + "\n")
        f.close() 

def main(script, *args):

    state_list = []
    for j, item in enumerate(args[1]):
        if j%2==0:
            state_list.append(int(item))
    #print(len(state_list), state_list)

    method = str(args[0])

    g = solver(state_list,method)
    g.solve()

if __name__ == '__main__':
    import sys
    main(*sys.argv)     
            
            
        

        
