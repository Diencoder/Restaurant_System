from app.models import Menu


def get_menu_items_by_category(category):
    """Lấy danh sách món ăn theo danh mục"""
    return Menu.objects.filter(category=category)

def get_menu_item_by_id(item_id):
    """Lấy thông tin món ăn theo ID"""
    return Menu.objects.filter(id=item_id).first()
