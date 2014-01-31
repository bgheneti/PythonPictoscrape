from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from fanfics.models import FanFic
from fanfics.forms import CreateNewForm, CreateURLForm
import my_immortal_keyword_finder
import image_return
import scraper

def index(request):
    latest_fanfic_list = FanFic.objects.all().order_by('-pub_date')[:7]
    context = {'latest_fanfic_list': latest_fanfic_list}
    return render(request, 'fanfics/index.html', context)

def createNew(request):
	if request.method == 'POST': 
		form = CreateNewForm(request.POST)
		if form.is_valid():
			new_fanfic = form.save()
			#alyssa's code -- getting keywords
			kwlist = my_immortal_keyword_finder.getwords(new_fanfic.text)
			for kw in kwlist:
				kw = kw.strip()
				#banti's code -- getting image urls 
				try:
					new_fanfic.keyword_set.create(key_word=kw, image_url=str(image_return.googlePrep(kw)))
				except:
					print kw + "is fucked"
			return HttpResponseRedirect('/fanfics/' + str(new_fanfic.id)) # Redirect to details page after POST
	else:
		form = CreateNewForm() # An unbound form

	return render(request, 'fanfics/createNew.html', {
        'form': form,
    })

def createURL(request):
	if request.method == 'POST': 
		form = CreateURLForm(request.POST)
		if form.is_valid():
			new_fanfic = form.save(commit=False)
			#banti's code -- scraping from url
			d = scraper.scrape(form.cleaned_data['url'])
			new_fanfic.title = d['title']
			new_fanfic.author = d['author']
			new_fanfic.text = d['text']
			new_fanfic.fandom = d['fandom']
			if d['text'] == '':
				new_fanfic.text = d['summary']
			else:
				new_fanfic.text = d['text']
			print "text of fanfic: " + new_fanfic.text
			new_fanfic.save()
			#alyssa's code -- getting keywords
			kwlist = my_immortal_keyword_finder.getwords(new_fanfic.text)
			if(kwlist==[]):
				new_fanfic.text = d['summary']
				kwlist = my_immortal_keyword_finder.getwords(new_fanfic.text)
			try:
				new_fanfic.profile=str(image_return.googlePrep(d['fandom']))
			except:
				print "FUCK the profile picture"
			new_fanfic.save()
			for kw in kwlist:
				kw = kw.strip()
				#banti's code -- getting image urls 
				try:
					new_fanfic.keyword_set.create(key_word=kw, image_url=str(image_return.googlePrep(kw)))
				except:
					print kw + "is fucked"
			return HttpResponseRedirect('/fanfics/'+ str(new_fanfic.id)) # Redirect after POST
	else:
		form = CreateURLForm() # An unbound form

	return render(request, 'fanfics/createURL.html', {
        'form': form,
    })

def detail(request, fanfic_id):
    fanfic = get_object_or_404(FanFic, pk=fanfic_id)
    return render(request, 'fanfics/detail.html', {'fanfic': fanfic})
