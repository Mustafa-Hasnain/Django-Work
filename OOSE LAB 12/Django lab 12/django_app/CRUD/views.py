from cgitb import reset
from django.shortcuts import redirect, render
from CRUD.models import Students, Project
from .form import std

# Create your views here.
def index(request):
    return render(request,"CRUD/index.html")

#Here we will also give an extra attribute id for editing purpose
#We are setting default id=0
def std_form(request, id=0):
    #Post method will be used after pressing submit button
    #Get Method will fetch the data
    if request.method == 'GET':
        if id == 0:
            #Here we have to display form and render page
            form = std()
            return render(request, 'CRUD/addData.html', {'form': form})
            #GET method through EDIT button
        else:
            #EDIT button work
            #Getting the object = id from table as Primary key (it is auto created by django) 
            students = Students.objects.get(pk=id) 
            form = std(instance = students) #We are giving instance as students to get the particular data
            return render(request, 'CRUD/addData.html', {'form': form})
        #Here we will transfer our data to form in the form of dictionary
    else:
        #Since there is no 0 in id so we are using it as default for the Add student function
        if id == 0:
            form = std(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/CRUD/show')
        #Here we will save the Edited value if the specific id 
        else:
            students = Students.objects.get(pk=id)
            form = std(request.POST, instance= students)
            if form.is_valid():
                form.save()
            return redirect('/CRUD/show')


#Getting the added results in show
def show(request):
    #This hsow function is doing two work
    #Here it will return all the records
    if request.method == 'GET':
        std_list = Students.objects.all().order_by('std_name')
        return render(request, 'CRUD/show.html', {'std_list':std_list})
    #and here it will return the searched record using search bar
    else:
        std_list = Students.objects.filter(std_name__startswith = request.POST['text'])
        return render(request, 'CRUD/show.html', {'std_list':std_list})


def delete(request, id):
    student = Students.objects.get(pk=id)
    student.delete()
    return redirect('/CRUD/show')