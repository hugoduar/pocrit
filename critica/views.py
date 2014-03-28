from django.shortcuts import render_to_response

from critica.models import Category, Thing
# Create your views here.

def category_list(request):
	categories = Category.objects.all()
	things = Thing.objects.all()
	return render_to_response('index.html',{'categories':categories, 'things':things})