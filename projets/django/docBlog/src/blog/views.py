from django.shortcuts import render


# Create your views here.
def index(request):
    # print("Le blog")
    return render(request, "blog/index.html") # pour trouver le bon fichier il faut créer un sous dossier DocBlog et un refactoring et idem pour blog


def article(request , article_number):
    # print(article_number)
    if article_number in ["01" , "02"]:
        return render(request, f"blog/article_{article_number}.html")
    return render(request, "blog/article_not_found.html")