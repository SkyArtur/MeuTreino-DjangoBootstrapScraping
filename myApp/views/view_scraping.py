from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from myApp.functions import scraper
from myApp.objects import Scraper


@login_required(redirect_field_name='login')
def view_scraping(request):
    if request.method != 'POST':
        return redirect('index')
    for content in request.POST.values():
        if content is None or not content:
            return redirect('index')
    try:
        # scrap_text = scraping('https://pt.wikipedia.org/wiki/' + request.POST['url_scraping'])
        target = Scraper('https://pt.wikipedia.org/wiki/' + request.POST['url_scraping'])
        context = {'context': target.scraping_text_in_p_tag}
        return render(request, 'pages/index.html', context)
    except:
        return redirect('index')
