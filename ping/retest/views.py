from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login 

def login(request):
	return render(request,'retest/login.html')
	if request.method == 'POST':
		form = login(request.POST)

		if form.is_valid():
			form.save()
			return redirect('retest/report.html')
		else :
			return render(request,'retest/login.html')	
		
def report(request):
	return render(request,'retest/report.html')
	if request.method=='POST':
			form= login(request.POST)

			if form.is_valid():
				form.save()
				return redirect('retest/enviar.html')
			else:
				return render(request,'retest/report.html')

def enviar(request):
	return render(request,'retest/enviar.html')








