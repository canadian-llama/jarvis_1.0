# import openai
def get_api_key():
    with open ('api.txt', "r") as file:
        api_key = file.read().strip()
        return api_key

print(get_api_key())
 
# def use_openai_api(query):
#     openai.api_key = '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'
#     engine = "davinci"
#     parameters = {
#         "prompt": query,
#         "max_tokens": 100,
#         "n": 1,
#         "stop": "\n",
#         "temperature": 0.5,
#         "frequency_penalty": 0,
#         "presence_penalty": 0,
#     }
#     open_ai_result = openai.Completion.create(engine=engine, **parameters)

#     code = open_ai_result.choices[0].text.strip()

#     # Print the generated code
#     print(code)
#     return code


# queries = input("Enter your query: ")
# output = use_openai_api(queries)
# print(output)
