# I have created this file - Tauqeer Sajid
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    try:
        # get the text
        djtext = request.POST.get('text', 'default')

        # check the check box values
        removepunc = request.POST.get('removepunc', 'off')
        fullcaps = request.POST.get('fullcaps', 'off')
        newlineremover = request.POST.get('newlineremover', 'off')
        extraspaceremover = request.POST.get('extraspaceremover', 'off')
        charcounter = request.POST.get('charcounter', 'off')
        analyzed = ''

        # check the checkbox is on and do the required action
        if removepunc == 'on':
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char

            params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
            djtext = analyzed

        if fullcaps == 'on':
            analyzed = djtext.upper()

            params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
            djtext = analyzed

        if newlineremover == 'on':
            analyzed = djtext.replace('\n', '')

            params = {'purpose': 'New Line Removes', 'analyzed_text': analyzed}
            djtext = analyzed

        if extraspaceremover == 'on':
            analyzed = djtext.strip()

            params = {'purpose': 'Extra Space Remove', 'analyzed_text': analyzed}
            djtext = analyzed

        if charcounter == 'on':
            analyzed = len(djtext)

            params = {'purpose': 'Count the Characters', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)
    except:
        return HttpResponse('Error')