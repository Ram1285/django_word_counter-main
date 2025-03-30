from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == "POST":
        texts = request.POST.get('words')
        words = str(texts).strip()
        number_of_words = len(words.split())

        return render(request, 'index.html', {
            'n_words': number_of_words,
            'words': words,
        })

    return render(request, 'index.html')