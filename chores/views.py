from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import  ChoreList
from django.template import RequestContext,loader

def index(request):
    # 04-01 simple page
    # return HttpResponse("You are at the ChoreList index.")

    #read all chorelist data to view and show:
    lists = ChoreList.objects.all()
    # template=loader.get_template('chores/index.html')
    # context=RequestContext(request,{
    #     'chorelists':lists
    # })
    # output = ', '.join([cl.name for cl in lists])
    # return HttpResponse(template.render(context))
    context= {  'chorelists':lists }
    return render(request,'chores/index.html',context)

def detail(request, chorelist_id):
    # return HttpResponse("You are looking at ChoreList #%s ." % chorelist_id)
    lists = ChoreList.objects.get(pk=chorelist_id)
    # template=loader.get_template('chores/index.html')
    # context=RequestContext(request,{
    #     'chorelists':lists
    # })
    # output = ', '.join([cl.name for cl in lists])
    # return HttpResponse(template.render(context))
    context= {  'chorelist':lists }
    return render(request,'chores/detail.html',{'chorelist': lists})

def chores(request, chorelist_id):
    return HttpResponse("You are looking at Chores from ChoreList #%s ." % chorelist_id)

def choredetail(request, chorelist_id, chore_id):
    return HttpResponse("You are looking at Chores #%s from ChoreList #%s ." % (chore_id,chorelist_id))

