import sys
from django.shortcuts import render 
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure the generative AI model
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")


def index(request):
    return render(request, 'index.html')

def run_code(request):
    code = ""  # Initialize code and output
    output = ""
    if request.method == "POST":
        code = request.POST.get('code')
        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(code)
            sys.stdout.close()
            sys.stdout = original_stdout
            output = open('file.txt').read()
        except Exception as e:
            sys.stdout = original_stdout
            output = str(e)

    return render(request, 'index.html', {"code": code, "output": output})

def code_generation(request):
    if request.method == "POST":
        question = request.POST.get('user-input')
        answer = model.generate_content(question)
        response = answer.text
    else:
        response = ""  # Initialize response if not POST request

    return render(request, 'index.html', {"response": response})
