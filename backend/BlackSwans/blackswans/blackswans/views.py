from .Models.Journal import Journal
from .Models.Author import Author
from .Models.Article import Article
from django.http import JsonResponse


def top10_papers_by_pagerank_by_cites(request):

    url = "bolt://34.201.126.190:7687"
    user = "neo4j"
    password = "loaf-alcohol-theory"

    connect = Article(url, user, password)
    papers_by_pagerank_by_cites = connect.get_top10_papers_by_pagerank_by_cites()
    result = {"nodes": papers_by_pagerank_by_cites}

    return JsonResponse(result)


def top10_papers_by_pagerank_by_journal(request):

    url = "bolt://34.201.126.190:7687"
    user = "neo4j"
    password = "loaf-alcohol-theory"

    connect = Article(url, user, password)
    papers_by_journal = connect.get_top10_papers_by_pagerank_by_journal()
    result = {"nodes": papers_by_journal}

    return JsonResponse(result)
