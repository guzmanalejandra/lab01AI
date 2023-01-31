import matrimage as matriximage
import bfs as bfs
import dfs as dfs
import A_star as astar
import path as linepath
import render as render
import os 



def main():

    print("Bienvenido al laboratorio, por favor escoja una opcion: ")
    print("\n1. BFS")
    print("\n2. DFS")
    print("\n3. A* Manhattan")
    print("\n4. Salir")
    
    option = int(input("Que opcion desea ejecutar?"))
    file = os.path.abspath("mazes/prueba2.bmp")
    matriximage.matrimage(file)
    matrix = matriximage.matrimage("mazes/renderizada2.bmp")
    path = []
    
    if option == 1:
        bfsPath = bfs.bfs(matrix) 
        path = bfsPath.path
        
        if path == None:
            print("\nNo se encontro un camino >:(")
        else:
            print("\n El camino mejor conlleva: ", len(path)-1, "pasos")
            
    elif option == 2:
            dfsPath = dfs.dfs(matrix)
            path = dfsPath.path
            
            del dfsPath

            if path == None:
                print("\nDFS: No se encontro un camino")
            else:
                print("\nDFS: El camino más corto es: ", len(path)-1, " pasos.")     
    elif option == 3:
            #astar
            astarPath = astar.astar(matrix, 'Manhattan')
            path = astarPath.path   
    elif option == 4:
        print("Gracias por usar el programa")
        
    else:
        print("Opcion no valida")

    if path != None:
        linepath.pathlineart("mazes/renderizada2.bmp",path)

        
    
if __name__ == "__main__":
    main()