import nltk
from nltk.chat.util import Chat,reflections

pairs=[
    (r'Hello|Hi',['Hello,How are you Today']),
    (r'(.*)I am Fine',['Glad to know that,How can i help you']),
    (r'What do you call yourself?',['I am just a simple ChatBot']),
    (r'(.*)Your Name?', ['My name is Chitti']),
    
    (r'(.*)age(.*)?',['I am just a computer program, I do not have age']),
    (r'Thanks(.*)',['YOu are Welcome']),
    (r'(.*)bye(.*)',['It was great please chatting with you,Please visit again'])
]


print("Welcome to the NTLK Chatbhot")

chatbot =Chat(pairs)
chatbot.converse()

#to stop the chatbhot Type Quit