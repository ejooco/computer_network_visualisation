import pandas as pd

data = pd.read_csv('test_large1.csv')

#Convert Source and Destination Columns into lists
source = data.Source.tolist()
destination = data.Destination.tolist()

#nodes is a list of all the endpoints within the pcap | this will represent the circles in the final product
#the nodes portion of the resulting json file will use this value
#I am doing a quick list->dictionary->list conversion to remove duplications
nodes = source + destination
nodes = list(dict.fromkeys(nodes))

#the json file has 2 distinct sections, nodes and links
#the nodes are created with the above list
#however the links are not created with nodes, they are created with the 'index' position of the node within the nodes list
#the node_positions list is created to simplify the code, it will always start at 0 and end in len(nodes)
#it is helpful, but not essential
node_positions = [i for i in range(len(nodes))]

#Here we are matching index positions for source and destination IPs
#Essentially each pair will represent a link on the chart
pairs = []
i = 0
while i < len(source):
    pairs.append([source[i], destination[i]])
    i+=1

#Weights are going to represent how often 2 nodes have communicated with each other.
#Essentially in graphical terms, this will determine the thickness of the line that links 2 nodes
weights = []
for i in pairs:
    weights.append(pairs.count(i))

#Here we are adding the previously calculate weight to the pairs lists
#Remember pairs is a nested list. The inner lists look as below
#   ['1.1.1.1', '2.2.2.2', 8]
#    source^     dest^     ^weight
count = 0
for i in pairs:
    i.append(weights[count])
    count += 1

#Here we are creating a list from the pairs list, however without any duplications, as the duplications are now
#represented by the weight.
#This will be used next
unique = []
c=0
while c < len(source):
    if pairs[c] not in unique:
        unique.append(pairs[c])
    else: 
        pass
    c+=1

#the 'unique' list is dict-zipped with the node_postions here
#{0: ['220.175.8.56', '80.171.48.1', 1]},
# 1: ['222.136.251.117', '80.171.48.1', 2], etc}
# ^index    ^source         ^target     ^weight
links = dict(zip(node_positions,unique))

### BAD CODE ALERT ###
# creating a list to iterate through, using string concatenation to display what I want the json file to represent
node_list = []
for i in nodes:
    text = "{\"name\": " +"\"" + i +"\"" + "}"
    node_list.append(text)

#Same as above but for the links list
link_list = []
for key, value in links.items():
    source=str(key)
    target=str(nodes.index(value[1]))
    weight=str(value[2])
    text = "{\"source\":" + source + ",\"target\":" + target + ",\"weight\":" + weight + "}"
    link_list.append(text)

with open('./working-too-much-force/test.json', 'w') as test:
    test.writelines("{\"nodes\":[")
    z = 0
    while z < (len(node_list)-1):
        test.writelines(node_list[z] + ",")
        z+=1
    test.write(node_list[-1])
    test.write("],\"links\":[")
    z = 0
    while z < (len(link_list)-1):
        test.writelines(link_list[z] + ",")
        z+=1
    test.write(link_list[-1])
    test.write("]}")
