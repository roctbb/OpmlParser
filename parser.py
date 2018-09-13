import json

import opml
doc = opml.parse('graph.opml')

nodes = []
edges = []

id = 0
cluster = 0

def show(outline, level, ccluster):
    global id
    global cluster

    cur_cluster = ccluster
    if level == 2:
        cluster += 1
        cur_cluster = cluster

    try:
        cur_id = id
        print(id, level * ' ', outline.text, cur_cluster)

        nodes.append({
            'id': id,
            'name': outline.text,
            'cluster': cur_cluster,
            'level': level
        })
        if id == 0:
            nodes[-1]['root'] = True
        else:
            nodes[-1]['root'] = False
        id += 1

    except:
        pass
    for item in outline:
        nid = show(item, level + 1, cur_cluster)
        try:
            print(id, level * ' ', outline.text, cur_cluster)
            edges.append({
                'source': nid,
                'target': cur_id,
                'type': 'partOf'
            })
        except:
            pass

    return cur_id

show(doc, 0, 0)

result = {
    "nodes": nodes,
    "edges": edges
}

with open('graph.json', 'w') as f:
    f.write(json.dumps(result))

print(nodes)
print(edges)