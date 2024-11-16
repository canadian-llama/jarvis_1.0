# import openai
def get_api_key():
    with open ('api.txt', "r") as file:
        api_key = file.read().strip()
        return api_key

print(get_api_key())
 
