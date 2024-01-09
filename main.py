import re
import openai
import pyttsx3
import speech_recognition as sr
from dotenv import dotenv_values

api_key_dict = dotenv_values(".env")
api_key = api_key_dict.get('API_KEY')

openai.api_key = api_key


# Function to ask a question using ChatGPT
def ask_question(question):
    # Define the conversation with a system message and user question
    messages = [
        {"role": "system", "content": "You are a knowledge assistant."},
        {"role": "user", "content": question}
    ]
    # Send the messages to ChatGPT
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    # Extract and return the assistant's answer
    assistant_reply = response["choices"][0]["message"]["content"]
    return assistant_reply


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('volume', 1.0)
engine.setProperty('rate', 140)
engine.setProperty('voice', voices[1].id)


def speakAndPrint(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query = query.capitalize()
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        speakAndPrint("Say that again please...")
        return "None"
    return query


def get_first_integer(input_string):
    # Use regular expression to find the first integer in the string
    match = re.search(r'\d+', input_string)

    if match:
        # Extract and return the first integer found
        return int(match.group())
    else:
        # Return None if no integer is found
        return 0


dsa_questions = [
    "What is an array ?",
    "How do you find the length (number of elements) of an array in most programming languages?",
    "Explain the concept of a stack and provide an example of a real-world application where stacks are used.",
    "What is the difference between a queue and a stack? Provide examples of situations where each data structure is useful.",
    "Define the term 'algorithm' and provide a simple example of an algorithm you use in everyday life.",
    "Explain the concept of time complexity in algorithms. Why is it important?",
    "What is recursion in programming? Provide an example of a recursive function.",
    "What is a binary search algorithm, and how does it work?",
    "Describe the process of sorting elements in an array using the bubble sort algorithm.",
    "What is a linked list, and how is it different from an array? Provide an example of a situation where a linked list is preferred over an array."
]

speakAndPrint("try to be confident and answer your question correctly without stopping")
total_score = 0
for i in range(0, len(dsa_questions)):
    speakAndPrint(dsa_questions[i])
    query = takeCommand().lower()
    user_question = f"Question :{dsa_questions[i]} Answer :{query}. give a score out of 10 no explanation needed ."
    answer = ask_question(user_question)
    score = get_first_integer(answer)
    print("score =", score)
    total_score += score

speakAndPrint("the Final score is ")
c = total_score / 10
speakAndPrint(c)


