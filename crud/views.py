from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import Employee
from .models import User
from django.views.generic.base import TemplateView,View,RedirectView
from django.views import View

# def index(request):
#     if request.method=='POST':
#         fm=Employee(request.POST)
#         if fm.is_valid():
#             new=fm.save()
#             new.save()
#             return redirect('/')
#     else:
#         fm=Employee()
#     data=User.objects.all()
#     return render(request,'index.html',{'form':fm,'data':data})
    
# class Index(View):
#     def get(self,request):
#         form = Employee()
#         data=User.objects.all()
#         return render(request,'index.html',{'form':form,'data':data})
#     def post(self,request):
#         form = Employee(request.POST)
#         if form.is_valid():
#             form.save()    
#         return redirect('/')

class Index(TemplateView):
    template_name='index.html'
    def get_context_data(self,*args,**kwargs):
        super().get_context_data(**kwargs)
        form=Employee()
        data=User.objects.all()
        context={'data':data,'form':form}
        return context
    def post(self,request):
        request.method="POST"
        form=Employee(request.POST)
        if form.is_valid():
            form.save()
        return  HttpResponseRedirect('/') 
    
#  ################################################################

# def update(request,id):
#     if request.method=='POST':
#         pi=User.objects.get(pk=id)
#         fm=Employee(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#         return redirect('/')
#     else:    
#         pi=User.objects.get(pk=id)
#         fm=Employee(instance=pi)
#         return render(request,'update.html',{'form':fm})

# class Update(View):
#     def get(self,request,id):
#         pi=User.objects.get(pk=id)
#         fm=Employee(instance=pi)
#         return render(request,'update.html',{'form':fm})
#     def post(self,request,id):
#         if request.method=='POST':
#             pi=User.objects.get(pk=id)
#         fm=Employee(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#         return redirect('/')

class Update_View(View):
    def get(self,request,id):
        pi=User.objects.get(pk=id)
        fm=Employee(instance=pi)
        return render(request,'index.html',{'form':fm})
    def post(self,request,id):
        pi=User.objects.get(pk=id)
        fm=Employee(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')

    
# ###################################################################

# def delete_data(request,id):
#     # if request.method=='POST':
#     pi=User.objects.get(pk=id)
#     pi.delete()
#     return redirect('/')

# class Delete(View):
#     def get(self,request,id):
#         pi=User.objects.get(pk=id)
#         pi.delete()
#         return redirect('/')
    
class Delete_View(RedirectView):
    url='/'
    def get_redirect_url(self, *args, **kwargs):
        del_id=kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
    

