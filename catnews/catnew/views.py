from django.shortcuts import render
from django.views.generic.base import View
from .models import New


class MainView(View):
    def get(self, request):

        all_news = New.objects.all()
        some_list = []
        for new in all_news:
            title = new.title
            content = new.content
            image = new.image.url
            dic = {
                'title': title,
                'content': content,
                'image': image
            }
            some_list.append(dic)

        return render(request, 'main_page.html', context={'data': some_list})

    def post(self, request):
        nickname = request.POST['nickname']
        title = request.POST['title']
        content = request.POST['content']

        article = New(author=nickname, title=title, content=content)
        article.save()
        return render(request, 'main_page.html')
