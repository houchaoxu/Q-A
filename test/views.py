from py2neo import Graph
from django.shortcuts import render
# Create your views here.

def qands(request):
    ent = request.POST.get('ent')
    pro = request.POST.get('pro')
    if  ent == None or pro == None:
        return render(request, 'test/qands.html')
    else:
        graph = Graph("localhost:7474", username="neo4j", password="1039")
        sql = graph.run("match(e:Qands) where e.Qid=1 return e.sql").evaluate()
        sql = sql.replace('$', ent)
        sql = sql.replace('#', pro)
        df = graph.run(sql).evaluate()
        return render(request, 'test/qands.html', {'data': df})

def test(request):
    question = request.POST.get('question')
    if  question == None:
        return render(request, 'test/test.html')
    else:
        graph = Graph("localhost:7474", username="neo4j", password="1039")
        question = request.POST.get('question')
        return render(request, 'test/test.html', {'data': question})