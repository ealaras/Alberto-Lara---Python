import nltk
import re
from nltk.chat.util import Chat, reflections

# Definir pares de preguntas y respuestas
pairs = [
    ["¿Cómo te llamas?", ["Me llamo Chatbot."]],
    ["¿Cuál es tu color favorito?", ["Mi color favorito es el azul."]],
    ["¿Qué es Python?", ["Python es un lenguaje de programación interpretado."]],
    ["¿Cómo estás?", ["Estoy bien, gracias."]],
    ["¿Qué puedes hacer?", ["Puedo responder preguntas básicas."]],
    ["Adiós", ["¡Adiós! Que tengas un buen día."]],
]

# Crear un chatbot
chatbot = Chat(pairs, reflections)

def tokenize_input(user_input):
    # Tokenizar la entrada del usuario en palabras utilizando una expresión regular
    tokens = re.findall(r'\b\w+\b', user_input)
    return tokens

def chat():
    print("¡Hola! Soy un chatbot. Puedes hacerme algunas preguntas. Para salir, escribe 'adiós'.")
    while True:
        user_input = input("Tú: ")
        tokens = tokenize_input(user_input)
        response = []
        for token in tokens:
            response.append(chatbot.respond(token))
        print("Chatbot:", ' '.join(response))
        if user_input.lower() == "adiós":
            break

if __name__ == "__main__":
    nltk.download("punkt")
    nltk.download("averaged_perceptron_tagger")
    chat()
