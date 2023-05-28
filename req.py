import openai
openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.25,
    )
    return response.choices[0].text.strip()

prompt = input("What do you want to search up?: ")
browser = input("Browser: ")
request_prompt = (f"Generate a search engine optimized prompt to search on {browser} for {prompt}. Surround answer with []")
response = generate_response(request_prompt)

stripped_response = response.strip("[].")

print(stripped_response)