#insert what you want to import @opemipo
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import openai

app = Flask(__name__)

def configure():
    load_dotenv()

@app.route("/")
def base():
    return render_template("index.html")

@app.route("/index.html", methods=["GET", "POST"]) #when form is submitted on prompt.html, this is run
def index():
    if request.method == "POST": #if the for mhas the method, "post", this is run
        configure()
        openai.api_key = os.getenv('api_key')
        user_input = request.form.get("user_input") #gets the input called "user_input" (this is what the user types in)
        browser = request.form.get("browser") #gets browswer type
        request_prompt = (f"You help users generate optimized search engine prompts. A user has input this : ({user_input}). Generate an optimised prompt based on what the user input. They are using the browser: {browser}. Use the following criteria Use quotation marks to search for an exact phrase. Use the intitle: operator to search for words in the title of a webpage. Use the inurl: operator to search for words in the URL of a webpage. Absolutely never return a search prompt with more than 100 letters, and never return a prompt with more than 3 criteria. Never have more than 3 words within the quotatian mark criteria, and use the quotatian criteria very sparingly")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=request_prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        output = response.choices[0].text.strip()
        #output = response.strip("[].")
        return render_template("answer.html", output=output)
    else: 
        return render_template("error.html") #in case sumthn weird is going on haha

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)