from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from graphviz import Digraph


def test(request):
    dot = Digraph(comment='The Round Table')
    dot.attr('node', shape='box')
    dot.node('A', 'King Arthur')
    dot.node('B', 'Sir Bedevere the Wise')
    dot.node('L', 'Sir Lancelot the Brave')

    dot.edges(['AB', 'AL'])
    dot.edge('B', 'L', constraint='true')
    dot.render('media/test-output/round-table.gv', view=True)
    # dot.view()
    return HttpResponse('test')
