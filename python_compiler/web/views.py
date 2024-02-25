import sys
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def run_code(request):
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