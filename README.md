# Simple Ghandi Chatbot
## NLP, Big Data & AI
Created by Bas Hulskamp, 662781   
Made in Python 3.10.10

<hr>

## Explanation
The chatbot works by:
- Getting data from Wikipedia using the API.
- Creating a knowledge graph (kg) from that data.
- Reading the user's question about the data (input).
- Comparing the question to the sentences build from the relations, sources and targets of the links in the knowledge graph.
- Generating a full sentence response (output).
  - Gets the answer to the question if the question matches any sentence from the sentences dictionary. `{sentence: answer, }` This uses fuzzy matching with a minimum similarity value of 80. 
  - Alternatively responds with a negative response (e.g. "I don't know."), when no match is found or the similarity is too low.
