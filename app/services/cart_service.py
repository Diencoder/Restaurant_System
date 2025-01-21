from app.models import Cart, CartItem  # Import từ thư mục gốc của ứng dụng

def get_user_cart(user):
    """Lấy giỏ hàng của người dùng"""
    cart, created = Cart.objects.get_or_create(user=user)
    return cart

def get_cart_items(cart):
    """Lấy tất cả các món trong giỏ hàng"""
    return cart.items.all()

def add_item_to_cart(user, menu_item):
    """Thêm món ăn vào giỏ hàng"""
    cart, created = Cart.objects.get_or_create(user=user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)
    if not item_created:
        cart_item.quantity += 1
    cart_item.save()
