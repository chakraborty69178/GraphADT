# %%
"""
# GRAPH 

                                A--->B
                               ↑|   /| 
                               ||  / |  
                               |↓↙   ↓   
                                C--->D--->I--->J
                                \    |   ↗/
                                 \   |  //
                                  ↘  ↓ /↙
                                     F
                                    

"""

# %%

graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D','F','A'],
             'D': ['F','I'],
             'F': ['I'],
             'I':['J','F']}
        

# %%
def edgeDetect(graph,key,value):
    if key in graph and (value in graph[key]):
        print("There is a edge present in between",key,"and",value)
        return True
    else:
        print("No edge between",key,"and",value)
        return False
edgeDetect(graph,'B','F')
edgeDetect(graph,'B','D')

# %%
def addNewEdge(graph,key,value):
    if key in graph:
        print(key," Node is present")
        if value in graph[key]:
            print(key,value,"Edge is already there")
        else:
            graph[key].append(value)
            print(key,graph[key],"edge attached") 
    else:        
        print(key," Node not found")
        graph[key]=[]
        print("New node created",key)
        graph[key].append(value)
        print(key,"is connected with",value)
addNewEdge(graph,'M','N')
addNewEdge(graph,'I','J')
graph

# %%
def deleteEdge(graph,key,value):
    if key in graph and (value in graph[key]):
        print(value ,"from",key,graph[key], "deleted")
        graph[key].remove(value)        
        print(key,graph[key])
    else:
        print(key,value," Edge not found")
    
deleteEdge(graph,'G','H')
deleteEdge(graph,'I','J')
graph

# %%
def degree(graph,key):
    if key in graph:
        print(key, "Node is present")
        print("Degree of",key,"is",len(graph[key]))
    else:
        print(key,"Node not found")
degree(graph,'J')
degree(graph,'A')

# %%
def adjacent(graph,key):
    if key in graph:
        print(key,"Node is present")
        print("Vertices adjacent to vertex",key,"is",(graph[key]))
    else:
        print(key," Node not found")
adjacent(graph,'K')
adjacent(graph,'A')

# %%
"""
2. Using the Graph ADT, write a program – in any language of your choice to
implement the following:
a) Compute the degree distribution p(d) for any given graph.
b) Count the number of triangles in any given graph. 
"""

# %%
def triangles(graph):
    triangle=[]
    for node1 in graph.keys(): #A,B,C,D,F    #A
        for value1 in graph[node1]:  #B
            if value1 in graph.keys():
                for value2 in graph[value1]:#C,D
                    if value2 in graph[node1]: #C
                        tr = ' '.join(sorted(node1+value1+value2))
                        if tr not in triangle:
                            triangle.append(tr)
    print(triangle)
    print("Number of triangles in the graph :",len(triangle))
triangles(graph)

# %%
"""
 a) Run your program to output the degree distribution and triangle count on your
graph.
 b) Measure the time taken for each of the two computations under each of the
three representations.
c) Plot the degree distribution curve and do curve fitting to a power-law
distribution and determine the constant. You may use any tool to do curve
fitting.
"""

# %%
def measureTime(func):
    import time 
    begin = time.time() 
    func
    time.sleep(1) 
    end = time.time() 
    return(f"Total runtime of the program is {end - begin}") 
measureTime(triangles(graph))

# %%
"""
Go to the subfolder named large within the datasets Google folder. Choose one of the
large datasets from the large subfolder. Add and entry in the spreadsheet with folder 
chosen and your BITS ID.
"""

# %%
import pandas as pd
import numpy as np


# %%
header_names = ["FromNodeId","ToNodeId"]
filename = "roadNet-CA.txt"
df = pd.read_csv(filename, na_values={},names = header_names,sep='\t',skiprows=4)
df.head(10)

# %%
dfArray = np.array(df)
for record in dfArray:
    if(addNewEdge(graph,record[0],record[1])):
            print("Graph Created")

