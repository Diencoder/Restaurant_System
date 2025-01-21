from app.models import Table

def get_all_tables():
    """Lấy danh sách tất cả các bàn"""
    return Table.objects.all()

def reserve_table_by_id(table_id):
    """Đặt bàn theo ID"""
    table = Table.objects.get(id=table_id)
    if table.reservation_status == 'Available':
        table.reservation_status = 'Reserved'
        table.save()
        return True, f"Bàn {table.table_number} đã được đặt thành công!"
    return False, f"Bàn {table.table_number} không khả dụng để đặt."
