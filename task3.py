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

''' below are the few question to ask this chatbot 
1.hello
2.I am Fine
3.What do you call yoursel
4.what is your Name
5.what is your age
6.thanks chitti
7.bye chitti

'''
