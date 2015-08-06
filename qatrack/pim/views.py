from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.template import RequestContext
from django.core.mail import send_mail
from qatrack.pim.models import practice_improvementForm, practice_improvement
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test


# Custom Decorators #

def can_add_pim(user):
    if user.is_superuser:
        return True
    elif user:
        return user.has_perm("pim.change_practice_improvement")
    return False

#####################################################################

# Form Submission View #

def index(request):
    return render(request,"home/home.html")

@login_required()
@permission_required("pim.add_practice_improvement")
def pimform(request):
    if request.method == 'POST':
        form = practice_improvementForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.submitter = request.user
            if 'pim_image' in request.FILES:
                pim_image = practice_improvement(pim_image = request.FILES['pim_image'])
            obj.save()
            message = form.cleaned_data['comment']
            send_mail( 
                'Practice Improvement form has been submitted',
                message, 'sharif.elguindi@gmail.com',
                ['sharif.elguindi@gmail.com','sharife@email.arizona.edu','elguindi.sharif@mayo.edu'],
            )
            return HttpResponseRedirect('/pracimprov/thanks')
    else:
        form = practice_improvementForm()
    return render(request, 'form.html', {'form': form})

def thanks(request):
    return render(request,"submitted.html")

####################################################################

# Review Submission Forms #

@user_passes_test(lambda u: u.is_superuser, login_url='/login/')
def pimreview_table(request):
    
    query_results = practice_improvement.objects.all()
    return render(request, 'review_table.html', {'list': query_results})

@user_passes_test(lambda u: u.is_superuser, login_url='/login/')
def pimreview_table_dept(request, dept):
    
    query_results = practice_improvement.objects.filter(department=dept)
    return render(request, 'review_table_test.html', {'list': query_results, 'dept': dept})

@user_passes_test(lambda u: u.is_superuser, login_url='/login/')
def pimreview_bar(request):
    
   query_name = 'department'
   query_results = practice_improvement.objects.values(query_name).annotate(count=Count(query_name))
   return render(request, 'review_bar.html', {'query_results': query_results, 'query_name': query_name})
