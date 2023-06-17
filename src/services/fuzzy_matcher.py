from fuzzywuzzy import fuzz
from fuzzywuzzy import process

from services.kggenerator import KGGenerator

class FuzzyMatcher:

    def __init__(self) -> None:
        self.q_kg: dict = self.create_question_dict()

    def find_answer(self, user_question: str):
        """ Finds the correct answer by comparing the user's question to the sentences from the knowledge graph and then returning the assiociated answer."""
        answer = None
        max_similarity = 0.2

        for question in self.q_kg:
            similarity = fuzz.ratio(user_question, question)
            if similarity > max_similarity:
                max_similarity = similarity
                print(max_similarity)
                answer = self.q_kg[question]

        return answer
    
    def create_question_dict(self):
        # kg = KGGenerator.get_kg_from_json()
        # question_dict = {}

        # for link in kg['links']:
        #     relation = link['relation']
        #     source = link['source']
        #     target = link['target']

        #     # Create the question by combining the relation, source, and target
        #     question = f"What {relation} {source} {target}?"

        #     # Add the question and answer to the dictionary
        #     question_dict[question] = None

        # return question_dict
        return {
            "Hi!": "Hello, ask me anything about Gandhi",
            "What inspired Gandhi movements?": "Gandhi's movements were inspired by various factors, including his personal experiences with discrimination and injustice, his study of religious texts and philosophies, and the influence of other social and political reformers.",
            "What moved Gandhi to represent an Indian merchant in a lawsuit?": "Gandhi was moved to represent an Indian merchant in a lawsuit when he witnessed the racial discrimination faced by the Indian community and felt compelled to fight for their rights and dignity.",
            "What raised Gandhi resistance?": "Gandhi's resistance was raised by the oppressive policies of the British colonial government, the discrimination faced by Indians, and the desire to achieve justice and freedom for his fellow countrymen.",
            "What campaigns did Gandhi lead?": "Gandhi led various campaigns and movements, such as the non-cooperation movement, salt march, and civil disobedience movement, to challenge British rule, advocate for the rights of Indians, and achieve independence for India.",
            "Why did Gandhi adopt short dhoti?": "Gandhi adopted the short dhoti as a symbol of simplicity and to promote self-reliance among Indians.",
            "What began Gandhi to live in a self-sufficient residential community, to eat simple food, and undertake long fasts as a means of both introspection and political protest?": "Gandhi began to live in a self-sufficient residential community, eat simple food, and undertake long fasts as a means of practicing self-discipline, promoting self-reliance, and drawing attention to social and political issues.",
            "What urged Gandhi Indians?": "Gandhi urged Indians to unite, resist British oppression, and strive for independence through nonviolent means.",
            "What areas did Gandhi visit?": "Gandhi visited various regions in India and other parts of the world to understand the issues faced by different communities, mobilize support for his causes, and spread his message of nonviolence and social justice.",
            "What undertook Gandhi hunger strikes?": "Gandhi undertook hunger strikes as a form of nonviolent protest to draw attention to various issues and to pressure the British government and Indian leaders to address those concerns.",
            "What had Gandhi education?": "Gandhi received his education in law from the Inner Temple, London, and studied various subjects including philosophy, history, and literature.",
            "What was described Gandhi sister?": "Gandhi's sister was described as a compassionate and supportive family member who played an important role in his life.",
            "What was influenced Gandhi mother?": "Gandhi's mother had a strong influence on his upbringing, instilling in him moral values, religious teachings, and a sense of social responsibility.",
            "When did Gandhi enter school?": "Gandhi entered school at a young age and received his early education in Porbandar and later in Rajkot, where he developed a keen interest in various subjects and exhibited his leadership qualities.",
            "What studied Gandhi rudiments?": "Gandhi studied the rudiments of arithmetic, history, geography, and languages during his early education.",
            "What joined Gandhi High School?": "Gandhi joined high school in Rajkot, where he continued his education and further developed his intellectual and leadership abilities.",
            "Why did Gandhi leave his wife and family?": "Leaving his wife and family, Gandhi embarked on a journey to London to pursue his higher education and study law.",
            "Where did Gandhi want to go?": "Gandhi wanted to go to London to study law and gain knowledge that would help him fight for justice and serve his country.",
            "What informed Gandhi ways?": "Gandhi's ways were informed by his deep study of religious and philosophical texts, including Hindu scriptures, the Bible, and the teachings of various spiritual leaders and philosophers.",
            "What made Gandhi accept challenges?": "Gandhi accepted challenges as part of his commitment to truth, justice, and the pursuit of a better society. He believed in leading by example and was willing to make personal sacrifices for his principles.",
            "What university college did Gandhi attend?": "Gandhi attended University College London to study law and further his understanding of the legal system."
        }
