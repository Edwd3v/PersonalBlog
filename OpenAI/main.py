
import openai
import config

openai.api_key = config.api_key

# Llamamos a OpenAI y pasamos los dos paramnetros model y 
response = openai.ChatCompletion.create(model='text-davinci-003', 
                             messages=[{'role':'user', 'content':"Cual es la mision de OpenAI"}])
print(response)