# ------------------ #
# Note this is a very simple evaluation, and is meant to have a human manually review the results,
# due to the nature of numerical answers.
# ------------------ #

import openai
import json

openai.api_key = "(INSERT-YOUR-KEY-HERE)"

with open('eval.json') as f:
    data = json.load(f)

# Loop over all questions, keep score of each model
scores = {
    "text-davinci-003": 0,
    "gpt-3.5-turbo": 0
}

models = ["text-davinci-003","gpt-3.5-turbo"]

for question in data:
    print(question["question"])
    print(question["answer"])
    for model in models:
        print(model)

        # Chat completion versus text completion
        if(model == "gpt-3.5-turbo"):
            completion = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": question["question"]}])
            print(completion.choices[0].message.content)
            answer = completion.choices[0].message.content.strip()
        else:
            completion = openai.Completion.create(model=model, prompt=question["question"])
            print(completion.choices[0].text)
            answer = completion.choices[0].text.strip()

        if answer == question["answer"]:
            scores[model] += 1
            print("Correct!")
        else:
            print("Incorrect!")
    print("")

print(scores)





