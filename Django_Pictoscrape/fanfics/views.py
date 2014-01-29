from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from fanfics.models import FanFic
from fanfics.forms import CreateNewForm, CreateURLForm

def index(request):
    latest_fanfic_list = FanFic.objects.all().order_by('-pub_date')[:5]
    context = {'latest_fanfic_list': latest_fanfic_list}
    return render(request, 'fanfics/index.html', context)

def createNew(request):
	if request.method == 'POST': 
		form = CreateNewForm(request.POST)
		if form.is_valid():
			new_fanfic = form.save()
			
			'''
			Alyssa's code here perhaps 
			'''
			'''WANT TO REDIRECT TO DETAILS PAGE'''
			return HttpResponseRedirect('/fanfics/' + str(new_fanfic.id)) # Redirect after POST
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