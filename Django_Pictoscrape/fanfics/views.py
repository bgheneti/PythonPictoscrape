from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from fanfics.models import FanFic
from fanfics.forms import CreateNewForm, CreateURLForm
import my_immortal_keyword_finder
import image_return

def index(request):
    latest_fanfic_list = FanFic.objects.all().order_by('-pub_date')[:5]
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
				new_fanfic.keyword_set.create(key_word=kw) #adding new keyword

			#banti's code -- getting image url
			image_return.googlePrep('''keyword''', (1,3,1))
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
			#new_fanfic = form.save(committ=False)
			# 0 title
			# 1 summary/notes
			# 2 chapter
			'''
			Banti's code here 
			'''
			'''WANT TO REDIRECT TO DETAILS PAGE'''
			return HttpResponseRedirect('/fanfics/') # Redirect after POST
	else:
		form = CreateURLForm() # An unbound form

	return render(request, 'fanfics/createURL.html', {
        'form': form,
    })

def detail(request, fanfic_id):
    fanfic = get_object_or_404(FanFic, pk=fanfic_id)
    return render(request, 'fanfics/detail.html', {'fanfic': fanfic})