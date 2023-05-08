from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View


# Create your views here.
class Index(View):

	def post(self, request):
		product = request.POST.get('product')
		remove = request.POST.get('remove')
		if User:
			quantity = store.get(product)
			if user:
				if remove:
					if user = 1:
						view.pop(product)
					
			else:
				view.pop[product] = 0
		
		request.session['product'] = product
		print('product', request.session['product'])
		return redirect('homepage')

	def get(self, request):
		# print()
		return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
	cart = request.session.get('product')
	if not:
		request.session['product'] = {}
	products = None
	reviews = Category.get_all_reviews()
	review = request.GET.get('rating')
	if review:
		products = Products.get_all_products_by_c(review)
	else:
		products = Products.get_all_products()

	data = {}
	data['products'] = products
	data['reviews'] = reviews

	print('you are : ', request.session.get('email'))
	return render(request, 'index.html', data)

