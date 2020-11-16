from translate import Translator

from django.shortcuts import render



def home(request):
    ctx = {}
    if request.GET.get('raw_text'):
        rtx = request.GET.get('raw_text')
        translator = Translator(to_lang="bn")
        translation = translator.translate(rtx)
        ctx['translation'] = translation
    return render(request, 'basic.html', ctx)
