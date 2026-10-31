graph= {
  
    'Zone1': ['Zone2', 'Zone3'],
    'Zone2': ['Zone1', 'Zone3', 'Zone4'],
    'Zone3': ['Zone1', 'Zone2', 'Zone4'],
    'Zone4': ['Zone2', 'Zone3']
}

colors = ['Red', 'Green', 'Blue']


assignment={}
def is_valid(region,color):
    for neighbour in graph[region]:
        if neighbour in assignment and assignment[neighbour]==color:
            return False
    return True
def map_coloring():
    if len(assignment)==len(graph):
        return True
    for region in graph:
        if region not in assignment:
            break
    for color in colors:
        if is_valid(region,color):
            assignment[region]=color
            if map_coloring():
                return True
            del assignment[region]
    return False
print("MC")
print("__")
if map_coloring():
    print("\nsolution")
    for region,color in assignment.items():
        print(region,"->",color)
else:
    print("No sol")
