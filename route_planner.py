import math

def shortest_path(M,start,goal):
    print("shortest path called")
    explored = [[],[],[],[],[]]
    frontier = [[start],[[]],[0],[0],[0]]
    if start == goal:
        return [start]
    else:
        frontier_expansion(M, goal, explored, frontier)
        return explored[1][len(explored[1])-1]

def distance(start,end):
    distance = math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)
    return distance

def frontier_expansion(M, goal, explored, frontier):
    pathList = []
    while len(frontier[0]) > 0 and goal not in explored[0]:
        for road in M.roads[frontier[0][frontier[4].index(min(frontier[4]))]]:
            if road not in explored[0]:
                frontier[0].append(road)
                for path in frontier[1][frontier[4].index(min(frontier[4]))]:
                    pathList.append(path)
                if frontier[0][frontier[4].index(min(frontier[4]))] not in frontier[1][frontier[4].index(min(frontier[4]))]:
                    pathList.append(frontier[0][frontier[4].index(min(frontier[4]))])
                pathList.append(road)
                frontier[1].append(pathList)
                pathList = []
                distanceTraveled = frontier[2][frontier[4].index(min(frontier[4]))] + distance(M.intersections[frontier[0][frontier[4].index(min(frontier[4]))]],M.intersections[road])
                frontier[2].append(distanceTraveled)
                frontier[3].append(distance(M.intersections[road],M.intersections[goal]))
                frontier[4].append(distanceTraveled + distance(M.intersections[road],M.intersections[goal]))
        explored[0].append(frontier[0].pop(frontier[4].index(min(frontier[4]))))
        explored[1].append(frontier[1].pop(frontier[4].index(min(frontier[4]))))
        explored[2].append(frontier[2].pop(frontier[4].index(min(frontier[4]))))
        explored[3].append(frontier[3].pop(frontier[4].index(min(frontier[4]))))
        explored[4].append(frontier[4].pop(frontier[4].index(min(frontier[4]))))
        frontier_expansion(M, goal, explored, frontier)
