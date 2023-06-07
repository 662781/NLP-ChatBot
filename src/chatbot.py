import spacy
from matplotlib import pyplot as plt
import networkx as nx
import pandas as pd
import textacy
import wikipediaapi

class ChatBot:

    def __init__(self) -> None:
        self.knowledge_graph = {
            "apple": "A fruit that is red or green in color and grows on trees.",
            "banana": "A fruit that is yellow and grows on trees.",
            "orange": "A citrus fruit that is typically orange in color.",
            "watermelon": "A large fruit with green skin and red flesh."
        }
        self.nlp = spacy.load('en_core_web_sm')

    def process_input(self, user_input: str):
        doc = self.nlp(user_input)
        return [token.text for token in doc]
    
    def get_information(self, tokens):
        # Search the knowledge graph based on the keywords
        for token in tokens:
            if token in self.knowledge_graph:
                return self.knowledge_graph[token]
        
        # If no relevant information is found
        return None

    def generate_response(self, user_input):
        processed_input = self.process_input(user_input)
        information = self.get_information(processed_input)

        if information:
            return information
        else:
            return "I don't know."
        
    def draw_kg_for_most_common(self, txt, most_common_index=0):
        txt = "Although he was very busy with his work, Peter had had enough of it." \
            + " He and his wife decided they needed a holiday." \
            + " They travelled to Spain because they loved the country very much."

        doc = self.nlp(txt)
        # from text to a list of sentences
        lst_docs = [sent for sent in self.nlp(txt).sents]
        print("total sentences:", len(lst_docs))

        ## extract entities and relations
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
        
        ## create dataframe
        dtf = pd.DataFrame(dic)

        ## filter
        f = dtf["entity"].value_counts().head().index[most_common_index]
        tmp = dtf[(dtf["entity"]==f) | (dtf["object"]==f)]


        ## create small graph
        G = nx.from_pandas_edgelist(tmp, source="entity", target="object", 
                                    edge_attr="relation", 
                                    create_using=nx.DiGraph())

        ## plot
        plt.figure(figsize=(15,10))
        pos = nx.spring_layout(G, k=1)

        node_color = ["red" if node==f else "skyblue" for node in G.nodes]
        edge_color = ["red" if edge[0]==f else "black" for edge in G.edges]

        nx.draw(G, pos=pos, with_labels=True, node_color=node_color, 
                edge_color=edge_color,
                node_size=2000, node_shape="o")

        nx.draw_networkx_edge_labels(G, pos=pos, label_pos=0.5, 
                                edge_labels=nx.get_edge_attributes(G,'relation'),
                                font_size=12, font_color='black', alpha=0.6)
        plt.show()
