from django.db import models
from django.contrib.auth.models import User 
class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    preparation_time = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menu'  # Tên bảng trong MySQL
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey('Menu', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

    def get_total_price(self):
        return self.menu_item.price * self.quantity
class Table(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Trống'),
        ('Occupied', 'Đang sử dụng'),
        ('Reserved', 'Đã đặt trước'),
    ]

    table_number = models.IntegerField(unique=True)  # Số bàn (unique)
    capacity = models.IntegerField()                # Sức chứa
    location = models.CharField(max_length=100)     # Vị trí bàn
    reservation_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Available'
    )  # Trạng thái đặt bàn

    def __str__(self):
        return f"Bàn {self.table_number} - {self.get_reservation_status_display()}"
    class Meta:
        db_table = 'tables'  # Tên bảng SQL