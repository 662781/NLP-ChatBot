import spacy
from matplotlib import pyplot as plt
import networkx as nx
from networkx.readwrite import json_graph
import pandas as pd
import textacy
import wikipediaapi
import json
import os

class KGGenerator:

    def __init__(self) -> None:
        self.nlp = spacy.load('en_core_web_sm')
        self.nlp.add_pipe('coreferee')
        wiki_wiki = wikipediaapi.Wikipedia('en')
        page_py = wiki_wiki.page('Mahatma_Gandhi')
        self.txt = page_py.text

    def create_kg(self, most_common_index=0):
        if os.path.exists("data/knowledge_graph.json"):
            return
        
        doc = self.nlp(self.txt)
        # From text to a list of sentences
        lst_docs = [sent for sent in self.nlp(self.txt).sents]
        # print("total sentences:", len(lst_docs))

        # Extract entities and relations
        dic = {"id": [], "text":[], "entity":[], "relation":[], "object":[]}

        def coref(parts):
            for part in parts:
                subj_ref = doc._.coref_chains.resolve(part)
                if subj_ref:
                    for x in subj_ref:
                        yield x
                else:
                    yield part

        for i, sentence in enumerate(lst_docs):
            for sent in textacy.extract.subject_verb_object_triples(sentence):
                subj = " ".join(map(str, coref(sent.subject)))
                obj  = " ".join(map(str, coref(sent.object)))
                relation = " ".join(map(str, sent.verb))
                
                dic["id"].append(i)
                dic["text"].append(sentence.text)
                dic["entity"].append(subj)
                dic["object"].append(obj)
                dic["relation"].append(relation)
        
        # Create dataframe
        df = pd.DataFrame(dic)

        # Filter
        f = df["entity"].value_counts().head().index[most_common_index]
        tmp = df[(df["entity"]==f) | (df["object"]==f)]

        # Create small knowledge graph
        kg = nx.from_pandas_edgelist(tmp, source="entity", target="object", 
                                    edge_attr="relation", 
                                    create_using=nx.DiGraph())
        self._graph_to_json(kg)
        
    def _graph_to_json(self, kg):
        data = json_graph.node_link_data(kg)
        # Save the JSON data to a file
        with open('data/knowledge_graph.json', 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def get_kg_from_json(file = 'data/knowledge_graph.json') -> dict:
        with open(file, 'r') as file:
            return json.load(file)