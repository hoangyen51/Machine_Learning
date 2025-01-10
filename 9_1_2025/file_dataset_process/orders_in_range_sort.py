import pandas as pd


def find_orders_within_range(df, minValue, maxValue, sort):
    # Tính tổng tiền cho từng OrderID
    order_totals = df.groupby('OrderID').apply(
        lambda x: (x['UnitPrice'] * x['Quantity'] * (1 - x['Discount'])).sum()
    ).reset_index(name='Total')  # Tạo DataFrame với cột Total

    # Lọc các hóa đơn trong khoảng giá trị
    filtered_orders = order_totals[
        (order_totals['Total'] >= minValue) & (order_totals['Total'] <= maxValue)
        ]

    # Sắp xếp nếu cần
    if sort == 't':
        filtered_orders = filtered_orders.sort_values(by='Total', ascending=True)

    return filtered_orders


# Đọc dữ liệu từ file CSV
df = pd.read_csv('../dataset/SalesTransactions.csv')

# Nhập thông tin từ người dùng
minValue = float(input('Nhập giá trị min: '))
maxValue = float(input('Nhập giá trị max: '))
sort = input('Sort (t/f): ')

# Lấy kết quả
result = find_orders_within_range(df, minValue, maxValue, sort)

# In kết quả
if not result.empty:
    print(f"Danh sách các hóa đơn trong phạm vi giá trị từ {minValue} đến {maxValue} là:")
    print(result)  # In toàn bộ DataFrame
else:
    print(f"Không tìm thấy hóa đơn nào trong phạm vi giá trị từ {minValue} đến {maxValue}.")
