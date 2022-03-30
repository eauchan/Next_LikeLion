from django.shortcuts import render

# Create your views here.
def  count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    total_len1 = 2 * total_len
    word = len(text.split(" "))
    no_blank_len = len(text.replace(' ', ''))
    no_blank_len1 = 2 * no_blank_len
    return render(request, 'result.html', {'input': text, 'total_len': total_len, 'no_blank_len': no_blank_len, 'word': word,
    'total_len1': total_len1, 'no_blank_len1': no_blank_len1})