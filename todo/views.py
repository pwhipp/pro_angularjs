from django.http import JsonResponse


def get_todo_items(request):
    items = [{"action": "Buy Flowers", "done": False},
             {"action": "Get Shoes", "done": False},
             {"action": "Collect Tickets", "done": True},
             {"action": "Call Joe", "done": False}]
    return JsonResponse(items, safe=False)
