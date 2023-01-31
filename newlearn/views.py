import openai
from django.shortcuts import render


def openai_view(request):
    if request.method == 'POST':
        lista_completa = {}
        user_input = request.POST['user_input']
        openai.api_key = "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"
        completions = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{user_input}",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text

        return render(request, 'newlearn/openai_response.html', {'raspuns': lista_completa, 'message': message, 'question': user_input})
    return render(request, 'newlearn/openai_form.html')
