import penman
import csv

gb = penman.load('data/graph_bank_filtered.txt')
print(len(gb), 'graphs imported')
with open('data/entities') as f:
    entities = [l.strip() for l in f.readlines()]


def graph2dict(graph):
    g = {}
    for triple in graph.triples:
        g.setdefault(triple[0],{})
        g[triple[0]][triple[1]] = triple[2]
    return g

def interrogate(propb_pred):
    final_triples = []
    for graph in gb:
        graph_dict = graph2dict(graph)
        instances = [t for t in graph.triples if propb_pred in t]
        triples_ = []
        for instance in instances:
            triples_ = []
            triples = graph_dict[instance[0]]
            triples.pop(':instance')
            for k, v in triples.items():
                if v.startswith('z'):# not in ['-']:
                    name = graph_dict[v].get(':instance', '')
                    wiki = graph_dict[v].get(':wiki', '')
                    if wiki != '':
                        triples_.append(' ~ '.join([propb_pred, k, wiki]))
                    elif name != '':
                        triples_.append(' ~ '.join([propb_pred, k, name]))
        if triples_ != []:
            print(triples_)
            final_triples.append([graph.metadata['page_id'], graph.metadata['nsent'], ' | '.join(triples_), graph.metadata['snt']])
            #final_triples.append(triples_)


    with open('out/' + propb_pred + '.csv', 'w') as fw:
        writer = csv.writer(fw, delimiter='\t')
        writer.writerows(final_triples)

interrogate('play-11')