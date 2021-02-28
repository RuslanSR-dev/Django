from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


user = {
    "name": "Иван",
    "middle": "Петрович",
    "surname": "Сидоров",
}


def main(request):
    return render(request, 'index.html')


def about(request):
    text = f"""
    Имя: {user['name']}<br>
    Отчество: {user['middle']}<br>
    Фамилия: {user['surname']}<br>
    """
    return HttpResponse(text)


def show_item(request, id):
    try:
        current_item = Item.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404
    context = {
        "item": current_item
    }
    return render(request, "item.html", context)


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items.html", context)
