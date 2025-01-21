from django.core.paginator import Paginator
from app.models import Menu

def get_menu_items_by_category(category, page_number, items_per_page=10):
    items = Menu.objects.filter(category=category)
    paginator = Paginator(items, items_per_page)
    return paginator.get_page(page_number)
