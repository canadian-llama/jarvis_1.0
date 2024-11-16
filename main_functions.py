"""
import all necessary modules that will be used in the file
"""
import openai
import random
import time
from datetime import datetime
import secondary_functions as sf
import word_list as wl

"""
this is a function to get api_key from a .txt file to avoid error whilst pushing to github
"""
def get_api_key():
    with open ('api.txt', "r") as file:
        api_key = file.read().strip()
        return api_key

"""
this function takes user query and tokenizes it thereby returning a list.
"""


def tokenize_user_query(query):
    user_query = query.lower().strip()
    tokenized_query = sf.input_tokenizer(user_query)
    return tokenized_query


"""
This function takes a list and randomly choose a greeting from the list then returns it.
"""


def greet_user():
    greetings = random.choice(wl.greet_users)
    return greetings


"""
This function returns the current time
"""


def tell_time():
    current_time = time.strftime('%H : %M : %S')
    return current_time


"""
This function returns the current date
"""


def tell_date():
    date = datetime.now()
    current_date = str(date.date())
    return current_date


"""
This uses the openai key to perform other functions.
"""


def use_openai_api(query):
    openai.api_key = get_api_key()
    completion = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{
        'role': 'user', 'content': query
    }])
    open_ai_result = completion.choices[0].message.content
    return open_ai_result


"""This function addresses various possible outcome of a query and returns the expected output."""

def determine_output(query):
    query = tokenize_user_query(query)
    print(query)
    output = ""

    if sf.input_comparison(query, wl.jarvis_introductions):
        output = greet_user()

    elif sf.input_comparison(query, wl.ask_for_time):
        output = f"The time is: {tell_time()}"

    elif sf.input_comparison(query, wl.ask_for_date):
        output = f"The date is: {tell_date()}"
    else:
        try:
            output = use_openai_api(query)
        except ConnectionAbortedError:
            output = "NO! internet connection"
        except ConnectionError:
            output = "NO! internet connection"
        except Exception:
           output = "NO! internet connection"
    return output
