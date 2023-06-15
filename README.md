# Simple Ghandi Chatbot
## NLP, Big Data & AI
Created by Bas Hulskamp, 662781   
Made in Python 3.10.10

<hr>

## Explanation
The chatbot works by:
- Getting data from Wikipedia using the API (the Ghandi article)
- Creating a knowledge graph (kg) from that data
- Reading the user input (question)
- Comparing the keywords from the user input to the knowledge graph
- Generating a full sentence response, based on the found relations in the knowledge graph