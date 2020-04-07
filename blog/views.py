import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Article, Bug


def hello_world(request):
    return HttpResponse("Hello World")


def article_content(request):
    article = Article.objects.all()[0]
    title = article.title
    content = article.content
    article_id = article.artile_id
    date = article.date
    return_str = 'title: %s,content: %s,article_id: %s,date: %s' % (title, content, article_id, date)
    return HttpResponse(return_str)


def bug_content(request):
    bug = Bug.objects.all()[0]
    title = bug.title
    content = bug.content
    bug_id = bug.bug_id
    date = bug.date
    state = bug.state
    owner = bug.owner
    return_str = 'bug_id: %s,title: %s,content: %s,state: %s,owner: %s,date: %s' % \
                 (bug_id, title, content, state, owner, date)
    return HttpResponse(return_str)


def get_index_page(request):
    all_bug = Bug.objects.all()
    q1 = Bug.objects.filter(headline__startswith='WHAT')
    q2 = q1.exclude(pub_date__gte=datetime.now())
    q3 = q1.filter(pub_date__gte=datetime.now())
    Q4 = Bug.objects.filter(state=1)
    num_posts = Count('post')
    return render(request, 'g2.html',
                  {
                      'bug_list': all_bug
                  })


def domain_list(request):
    data = [1, 2, 3, 4, 5, 6]
    json = []
    return render(request, 'g2.html', locals())


def domain_list_js(request):
    data = ['hello', 'world', '!']
    data = json.dumps(data) #data必须是一个list
    return render(request, 'g2.html', locals())
