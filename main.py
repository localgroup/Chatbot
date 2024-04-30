import nltk
from nltk.chat.util import Chat
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from general_responses import pairs
import random

# Download NLTK resources if not already downloaded!!!
nltk.download('punkt')

# Initialize SpaCy
nlp = spacy.load("en_core_web_md")  # You can also download "en_core_web_lg" or "en_core_web_sm"


class Chatbot(Chat):
    def __init__(self, pairs):
        super().__init__(pairs)
        self.responses = [pair[1][0] for pair in pairs]
        self.response_inputs = [pair[0] for pair in pairs]
        self.all_texts = self.responses + self.response_inputs
        self.tfidf_matrix, self.tfidf_vectorizer = self.calculate_tfidf_cosine()

    def calculate_tfidf_cosine(self):
        """
        Custom tokenizer function.
        :return:
        """
        def custom_tokenizer(text):
            tokens = nltk.word_tokenize(text.lower())
            return tokens

        tfidf_vectorizer = TfidfVectorizer(tokenizer=custom_tokenizer, lowercase=True)
        tfidf_matrix = tfidf_vectorizer.fit_transform(self.all_texts)
        return tfidf_matrix, tfidf_vectorizer

    def _wildcards(self, response, match):  # (nltk.chat.util) method for processing wildcard placeholders.
        """
        Process wildcard placeholders in the response string based on the matched groups in the user's input.

        :type response: str
        :param response: The response string with wildcard placeholders
        :type match: re.Match
        :param match: The match object containing matched groups from the user's input
        :rtype: str
        """
        pos = response.find("%")
        while pos >= 0:
            num = int(response[pos + 1: pos + 2])
            response = (
                    response[:pos]
                    + super()._substitute(match.group(num))  # Substitute words in the string (nltk.chat.util).
                    + response[pos + 2:]
            )
            pos = response.find("%")

        return response

    def respond(self, input_text):
        """
        Defines the logic to provide a response to the user on likelihood...
        :param input_text:
        :return:
        """
        # Check if the input matches any of the patterns in pairs...
        try:
            for pattern, responses in self._pairs[:-1]:  # Exclude the last pair. (self._pairs... of class Chat.)
                match = pattern.match(input_text)
                if match:
                    # Check if the response from _wildcards matches any of the responses...
                    wildcards_response = self._wildcards(responses[0], match)
                    if wildcards_response in responses:
                        return wildcards_response

        except:
            pass

        # Calculate response based on cosine similarity score.
        input_text = input_text.lower()
        similarities = cosine_similarity(self.tfidf_matrix, self.tfidf_vectorizer.transform([input_text])).flatten()
        max_similarity_index = similarities[:-len(self.responses)].argmax()

        doc = nlp(input_text)  # Spacy pipeline...
        entities = [ent.text for ent in doc.ents]
        if "date" in entities:
            response = "Sure, what date are you interested in?"
        else:
            if similarities[max_similarity_index] > 0.2:
                response = self.responses[max_similarity_index]
            else:
                response = "I'm sorry, I don't understand."

        return response


def chatbot():
    """
    Interact with Boson.
    :return:
    """
    print("Hi, I'm Boson! How can I assist you today?")
    chatbot_ = Chatbot(pairs)
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Goodbye! Have a great day!")
            break
        else:
            response = chatbot_.respond(user_input)
            print("Bot:", response)


if __name__ == "__main__":
    chatbot()
