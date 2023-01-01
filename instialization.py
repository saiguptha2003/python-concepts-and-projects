import pickle
import math

#nodes={1:{'cords':[0,0], 'energy':50, 'depth':3}}

def create_node(r_s):
    d=int(((2**0.5)*r_s)/2)
    print(d)

    id=0
    for xp in range(0,length,d):
        for yp in range(0,-breadth,-d):
            if (xp == yp == 0):
                node = {}
                node['cords'] = [xp, yp]
                nodes[0] = node
            else:
                node = {}
                id += 1
                node['cords'] = [xp, yp]
                nodes[id] = node
    for xp in range(-d,-length,-d):
        for yp in range(-d,-breadth,-d):
            node = {}
            id+=1
            node['cords']=[xp,yp]
            nodes[id]=node
    for xp in range(0,-length,-d):
        for yp in range(0,breadth,d):
            if(xp==yp==0):
                node = {}
                node['cords'] = [xp, yp]
                nodes[0] = node
            else:
                node = {}
                id+=1
                node['cords']=[xp,yp]
                nodes[id]=node
    for xp in range(d,length,d):
        for yp in range(d,breadth,d):
            node = {}
            id+=1
            node['cords']=[xp,yp]
            nodes[id]=node
    return id



if __name__ == '__main__':

    nodes={}
    r_s=72
    length=breadth=1001
    cn=0
    neighbour_nodes=[]
    x=0
    y=0
    cycle=0
    nodes_count=1+create_node(r_s)
    print(nodes)
    # energy consumption parameters
    #nodes={}
    #nodes[i]['']
    #nodeid=0 : [energy:5,x:0,y:0]
    #nodeid=1
    #nodeid=2

    for i in range(0,nodes_count):
        nodes[i]['energy']=0.5
        #nodes[i]['fp'] = 0
        nodes[i]['status']=1
        nodes[i]['packets_transmitted']=0
        nodes[i]['packets_received'] = 0



    #neighbour node matrix determination
    for j in range(0,nodes_count):
        init_cords=nodes[j]['cords']
        temp = []
        for k in range(0,nodes_count):

            oth_cords=nodes[k]['cords']
            dist=math.dist(init_cords,oth_cords)
            #print(j, " ", k, "  ", dist)
            if(dist<r_s and j!=k):
                #print("work")
                #print(j, " ", k, "  ", dist)
                temp.append(1)

            else:
                temp.append(0)

        nodes[j]['neighbours']=temp
        #print("NEIGHBOURING NODES " ,neighbour_nodes)
    print(nodes)


    #depth calculation
    depth={}
    for i in range(1,nodes_count):
        distance=math.dist([x,y],nodes[i]['cords'])
        if(distance<r_s):
            depth[i]=1

    for i in range(1,nodes_count):
        #print("progress :  ",(i/nodes_count)*100)
        for key in list(depth):
            #print("progress : inner loop 2: ",(key/nodes_count)*100)
            for i in range(1,nodes_count):
                #print("progress : inner loop 3  ",(i/nodes_count)*100)
                if(key!=i):
                    distance=math.dist(nodes[key]['cords'],nodes[i]['cords'])
                    if(distance<r_s and i not in depth):
                        depth[i]=depth[key]+1

    for i in range(1,nodes_count):
        if i not in depth:
            depth[i]=0

    nodes[0]['depth']=0
    for i in depth:
        nodes[i]['depth']=depth[i]


    rows=cols=len(nodes[0]['neighbours'])
    print(nodes)


    afile = open(r'network_data.pkl', 'wb')
    pickle.dump(nodes, afile)
    afile.close()